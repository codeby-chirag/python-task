"""Do the operations for file and folder like list, move, copy, delete."""

import glob
import os
import shutil


def current_dir(path):
    """List everything inside directory."""
    print(os.listdir(path))


def curr_dir_file(path):
    """List files inside directory."""
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)


def curr_dir_folder(path):
    """List folder inside directory."""
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    print(folders)


def move_file(source, destination):
    """Move files from one directory other directory."""
    try:
        allfiles = glob.glob(source)

        if not allfiles:
            print(f"No file matched: {source}")
            return

        destination = os.path.abspath(destination)

        for file_path in allfiles:

            if not os.path.isfile(file_path):
                print(f"{source} is not File")
                continue

            dst_path = os.path.join(destination, os.path.basename(file_path))

            shutil.move(file_path, dst_path)
            print(f"Moved: {file_path} -> {dst_path}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def move_folder(source, destination):
    """Move folder from one directory other directory."""
    try:
        allfolders = glob.glob(source)

        if not allfolders:
            print(f"No folder matched: {source}")
            return

        for folder_path in allfolders:

            if not os.path.isdir(folder_path):
                print(f"{source} is not Folder")
                continue

            dst_path = os.path.join(destination, os.path.basename(folder_path))

            shutil.move(folder_path, dst_path)
            print(f"Moved: {folder_path} -> {dst_path}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def copy_file(source, destination):
    """Copy file from one directory other directory."""
    try:
        allfiles = glob.glob(source)

        if not allfiles:
            print(f"No file matched: {source}")
            return

        for file_path in allfiles:

            if not os.path.isfile(file_path):
                print(f"{source} is not File")
                continue

            dst_path = os.path.join(destination, os.path.basename(file_path))

            shutil.copy(file_path, dst_path)
            print(f"Copied: {file_path} -> {dst_path}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def copy_folder(source, destination):
    """Copy folder from one directory other directory."""
    try:
        allfolders = glob.glob(source)

        if not allfolders:
            print(f"No folder matched: {source}")
            return

        for folder_path in allfolders:

            if not os.path.isdir(folder_path):
                print(f"{source} is not Folder")
                continue

            dst_path = os.path.join(destination, os.path.basename(folder_path))

            shutil.copytree(folder_path, dst_path)
            print(f"Copied: {folder_path} -> {dst_path}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def delete_file(source):
    """Delete file from directory."""
    try:
        allfile = glob.glob(source)

        if not allfile:
            print(f"No file matched: {source}")
            return

        for file in allfile:
            if os.path.isdir(file):  # Cleaned path resolution
                print(f"{file} is a folder and can't be deleted")
                continue

            os.remove(file)  # Fixed W0120 by bringing code inside loop
            print(f"File deleted from -> {file}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")
