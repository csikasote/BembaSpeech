import os

# Set your root folder where your data files live
root_folder = "/mnt/workspace/BembaSpeech"

# Set your current local audio folder path
audio_folder = os.path.join(root_folder, "bem", "audio")

def fix_paths_in_file(filepath):
    print(f"Processing: {filepath}")
    fixed_lines = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split('\t')
            if len(parts) < 2:
                # Skip or keep as-is if malformed
                fixed_lines.append(line.strip())
                continue
            old_path = parts[0]
            transcription = '\t'.join(parts[1:])  # Support tabs in transcription
            
            # Extract filename only
            filename = os.path.basename(old_path)
            
            # Construct new path
            new_path = os.path.join(audio_folder, filename)
            
            # Rebuild line
            fixed_line = new_path + '\t' + transcription
            fixed_lines.append(fixed_line)
    
    # Overwrite original file with fixed lines
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in fixed_lines:
            f.write(line + '\n')
    print(f"Fixed paths in {filepath}")

def fix_all_files_in_folder(root):
    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if file.endswith('.csv') or file.endswith('.tsv'):
                full_path = os.path.join(dirpath, file)
                fix_paths_in_file(full_path)

if __name__ == "__main__":
    fix_all_files_in_folder(root_folder)
