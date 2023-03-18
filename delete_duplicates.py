import os
import hashlib
from collections import defaultdict

def find_duplicates(directory):
    file_hashes = defaultdict(list)
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)
            file_hashes[file_hash].append(file_path)
    return [paths for paths in file_hashes.values() if len(paths) > 1]

def hash_file(file_path, block_size=65536):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        block = file.read(block_size)
        while len(block) > 0:
            hasher.update(block)
            block = file.read(block_size)
    return hasher.hexdigest()

def delete_duplicate_files(duplicates):
    for duplicate_files in duplicates:
        for file_path in duplicate_files[1:]:
            os.remove(file_path)
            print(f'Deleted: {file_path}')

if __name__ == '__main__':
    folder_path = input('Enter the folder path: ')
    duplicate_files = find_duplicates(folder_path)
    
    if duplicate_files:
        delete_duplicate_files(duplicate_files)
        print('Duplicates deleted successfully!')
    else:
        print('No duplicate files found.')