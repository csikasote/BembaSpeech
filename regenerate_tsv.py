import os

# Define your folders
bem_folder = "/mnt/workspace/BembaSpeech/bem"
audio_folder = os.path.join(bem_folder, "audio")

# Files to fix
tsv_files = [
    os.path.join(bem_folder, "train.tsv"),
    os.path.join(bem_folder, "dev.tsv"),
    os.path.join(bem_folder, "test.tsv"),
]

def fix_paths(tsv_path):
    fixed_lines = []
    with open(tsv_path, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) < 2:
                # Skip malformed lines or handle differently if needed
                continue
            old_path = parts[0]
            transcription = '\t'.join(parts[1:])  # In case transcription has tabs
            
            # Extract only the filename from old_path
            filename = os.path.basename(old_path)
            
            # Construct new full path on your system
            new_path = os.path.join(audio_folder, filename)
            
            # Build fixed line
            fixed_line = new_path + '\t' + transcription
            fixed_lines.append(fixed_line)
    
    # Overwrite the original TSV with fixed paths
    with open(tsv_path, 'w', encoding='utf-8') as f:
        for line in fixed_lines:
            f.write(line + '\n')
    print(f"Fixed paths in {tsv_path}")

if __name__ == "__main__":
    for tsv in tsv_files:
        fix_paths(tsv)
