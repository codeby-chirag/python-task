import os
import glob
import shutil

def current_dir(path):
    print(os.listdir(path))


def curr_dir_file(path):
    files = [
        f for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]
    print(files)


def curr_dir_folder(path):
    folders = [
        f for f in os.listdir(path)
        if os.path.isdir(os.path.join(path, f))
    ]
    print(folders)


def move_file(source, destination):
    try:
        allfiles = glob.glob(source)

        if not allfiles:
            print(f"No file matched: {source}")
            return

        for file_path in allfiles:

            if not os.path.isfile(file_path):
                continue

            dst_path = os.path.join(
                destination,
                os.path.basename(file_path)
            )

            shutil.move(file_path, dst_path)
            print(f"Moved: {file_path} -> {dst_path}")

    except Exception as e:
        print(f"Error: {e}")


def move_folder(source, destination):
    try:
        allfolders = glob.glob(source)

        if not allfolders:
            print(f"No folder matched: {source}")
            return

        for folder_path in allfolders:

            if not os.path.isdir(folder_path):
                continue

            dst_path = os.path.join(
                destination,
                os.path.basename(folder_path)
            )

            shutil.move(folder_path, dst_path)
            print(f"Moved: {folder_path} -> {dst_path}")

    except Exception as e:
        print(f"Error: {e}")

def copy_file(source, destination):
    try:
        allfiles = glob.glob(source)

        if not allfiles:
            print(f"No file matched: {source}")
            return

        for file_path in allfiles:

            if not os.path.isfile(file_path):
                continue

            dst_path = os.path.join(
                destination,
                os.path.basename(file_path)
            )

            shutil.copy(file_path, dst_path)
            print(f"Copied: {file_path} -> {dst_path}")

    except Exception as e:
        print(f"Error: {e}")

def copy_folder(source, destination):
    try:
        allfolders = glob.glob(source)

        if not allfolders:
            print(f"No folder matched: {source}")
            return

        for folder_path in allfolders:

            if not os.path.isdir(folder_path):
                continue

            dst_path = os.path.join(
                destination,
                os.path.basename(folder_path)
            )

            shutil.copytree(folder_path, dst_path)
            print(f"Copied: {folder_path} -> {dst_path}")

    except Exception as e:
        print(f"Error: {e}")

def delete_file(source):
    try:
        allfile = glob.glob(source)

        if not allfile:
            print(f"No file matched: {source}")
            return

        for file in allfile:
            if os.path.isdir(os.path.join(source)):
                print(f"{source} is a folder and can't be delete")
        else:        
            os.remove(file)
            print(f"File delete from -> {source}")

    except Exception as e:
            print(f"Error: {e}")

# Sort command which SORT and make directory and move into that directory

