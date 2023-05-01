import os
from pathlib import Path

def generate_tree_structure(start_path, padding='', print_files=True):
    path = Path(start_path)
    files = []
    dirs = []
    for entry in os.scandir(path):
        if entry.is_file():
            files.append(padding + '- ' + entry.name)
        elif entry.is_dir():
            dirs.append(padding + '|- ' + entry.name)
            subfiles = generate_tree_structure(entry.path, padding + '|  ', print_files)
            files.extend(subfiles)

    if print_files:
        return dirs + files
    else:
        return dirs

tree = generate_tree_structure('ds_features')
for line in tree:
    print(line)