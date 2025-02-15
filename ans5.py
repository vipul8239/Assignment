import os
import hashlib
import shutil
import json

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicates(directory, min_size=0):
    hashes = {}
    duplicates = {}
    
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            if os.path.getsize(path) >= min_size:
                file_hash = get_file_hash(path)
                if file_hash in hashes:
                    duplicates.setdefault(file_hash, []).append(path)
                else:
                    hashes[file_hash] = path
    
    return duplicates

def handle_duplicates(duplicates, action, move_path=None):
    report = {}
    
    for file_hash, paths in duplicates.items():
        report[file_hash] = paths
        if action == 'delete':
            for file in paths:
                os.remove(file)
                print(f"Deleted: {file}")
        elif action == 'move' and move_path:
            os.makedirs(move_path, exist_ok=True)
            for file in paths:
                shutil.move(file, os.path.join(move_path, os.path.basename(file)))
                print(f"Moved: {file} -> {move_path}")
    
    with open('duplicate_report.json', 'w') as f:
        json.dump(report, f, indent=4)
    print("Report saved as duplicate_report.json")

if __name__ == "__main__":
    directory = input("Enter directory to scan: ")
    min_size = int(input("Enter minimum file size in bytes (0 for no limit): "))
    action = input("Enter action (report/delete/move): ").strip().lower()
    move_path = input("Enter destination directory for duplicates: ") if action == 'move' else None
    
    duplicates = find_duplicates(directory, min_size)
    if duplicates:
        handle_duplicates(duplicates, action, move_path)
    else:
        print("No duplicates found.")
