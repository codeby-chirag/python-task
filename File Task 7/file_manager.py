import os
import glob 
import shutil

def current_dir(path):
    print(os.listdir(path))


def curr_dir_file(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)


def curr_dir_folder(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    print(folders)


def move_file(source, pattern, destination):
    allfiles = glob.glob(os.path.join(source, pattern), recursive=True)
    print("Files to move", allfiles)

    for file_path in allfiles:
        dst_path = os.path.join(destination, os.path.basename(file_path))
        shutil.move(file_path, dst_path)
        print(f"Moved {file_path} -> {dst_path}")

def move_folder(source, pattern, destination):
    allfolder = glob.glob(os.path.join(source, pattern), recursive=True)

    for folder_path in allfolder:
        dst_path = os.path.join(destination, os.path.basename(folder_path))
        shutil.move(folder_path, dst_path)
        print(f"Moved {folder_path} -> {dst_path}")


def copy_file(source, pattern, destination):
    allfiles = glob.glob(os.path.join(source, pattern), recursive=True)

    for file_path in allfiles:
            dst_path = os.path.join(destination, os.path.basename(file_path))
            shutil.copy(file_path, dst_path)
            print(f"Moved {file_path} -> {dst_path}")

def copy_folder(source, pattern, destination):
    allfolder = glob.glob(os.path.join(source, pattern), recursive=True)

    for folder_path in allfolder:
        dst_path = os.path.join(destination, os.path.basename(folder_path))
        shutil.copytree(folder_path, dst_path)
        print(f"Moved {folder_path} -> {dst_path}")

def rem_file(source, pattern):
    file = glob.glob(os.path.join(source, pattern), recursive=True)

    for f in file:
        if os.path.isdir(os.path.join(source, pattern)):
                print(f"{pattern} is a folder and can't be delete")
        else:        
            os.remove(f)
            print(f"File {pattern} delete from -> {source}")






