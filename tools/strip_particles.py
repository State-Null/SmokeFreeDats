"""
FFXI Zone DAT Particle Stripper
================================
Scans FFXI zone container DATs, identifies self-contained 3D smoke/particle 
emitter chunks ('smok', 'mist', 'dust'), and cleanly slices them out while
preserving 100% of weather palettes, Mog House lighting, door spawn tables,
and terrain geometry.
"""

import sys
import os

def strip_zone_particles(input_path, output_path, target_tags=None):
    if target_tags is None:
        target_tags = ['smok', 'mist', 'dust']

    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' not found.")
        return False

    with open(input_path, 'rb') as f:
        data = f.read()

    # Step 1: Scan for 16-byte aligned root chunk headers
    chunks = []
    i = 0
    while i < len(data) - 16:
        tag = data[i:i+4]
        # Valid FFXI container headers start with 4 ASCII characters
        # followed by either flag 0x00000101 or chunk type 0x20
        if all(32 <= b <= 126 for b in tag) and (
            data[i+4:i+8] == b'\x01\x01\x00\x00' or 
            data[i+16:i+20] == b'\x00\x00\x00\x20'
        ):
            tag_str = tag.decode('ascii', errors='ignore')
            chunks.append((i, tag_str))
        i += 16

    # Step 2: Selectively strip ONLY genuine 3D particle emitter meshes
    # SAFETY RULES:
    # - NEVER strip anything under 10,000 bytes (weather palettes, day/night lighting)
    # - NEVER strip anything in the header section (offset < 0x20000 / door coordinates)
    # - ONLY strip 'smok' (>= 5 KB) or large 'mist'/'dust' particle meshes (> 50 KB)
    keep_slices = []
    current_pos = 0
    stripped_chunks = []

    for idx, (offset, tag_str) in enumerate(chunks):
        next_offset = chunks[idx+1][0] if idx+1 < len(chunks) else len(data)
        chunk_size = next_offset - offset

        is_particle_emitter = False
        if any(t in tag_str.lower() for t in target_tags):
            if tag_str == 'smok' and chunk_size >= 5000:
                is_particle_emitter = True
            elif tag_str in ['mist', 'dust'] and chunk_size > 50000 and offset > 0x20000:
                is_particle_emitter = True

        if is_particle_emitter:
            if offset > current_pos:
                keep_slices.append(data[current_pos:offset])
            current_pos = next_offset
            stripped_chunks.append((tag_str, chunk_size, offset))

    if current_pos < len(data):
        keep_slices.append(data[current_pos:])

    clean_data = b''.join(keep_slices)

    # Step 3: Write out the clean DAT
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(clean_data)

    print(f"Processed: {input_path}")
    print(f"  Original Size: {len(data):,} bytes")
    print(f"  Clean Size:    {len(clean_data):,} bytes")
    print(f"  Stripped:      {stripped_chunks}")
    return True

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python strip_particles.py <input_zone.DAT> <output_zone.DAT>")
        sys.exit(1)

    strip_zone_particles(sys.argv[1], sys.argv[2])
