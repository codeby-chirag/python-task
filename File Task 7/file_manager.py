"""Do the operations for file and folder like list, move, copy, delete."""

import os
import shutil


def validate_directory(path):
    if not os.path.exists(path):
        print(f"Error: '{path}' does not exist.")
        return False

    if not os.path.isdir(path):
        print(f"Error: '{path}' is not a directory.")
        return False

    return True

def current_dir(path):
    """List everything inside directory."""
    if not validate_directory(path):
        return

    print(os.listdir(path))


def curr_dir_file(path):
    """List files inside directory."""
    if not validate_directory(path):
        return
    
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if files:
        print(files)
    else:
        print("No file found.")


def curr_dir_folder(path):
    """List folder inside directory."""
    if not validate_directory(path):
        return
    
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    if  folders:
        print(folders)
    else:
        print("No folder found.")


def move_file(source, destination):
    """Move files from one directory other directory."""
    try:
        if not os.path.exists(destination):
            print(f"Error: '{destination}' does not exist.")
            return

        if not os.path.isdir(destination):
            print(f"Error: '{destination}' is not a directory.")
            return
        
        if not os.path.exists(source):
            print(f"No file matched: {source}")
            return

        if not os.path.isfile(source):
            print(f"{source} is not File")
            return

        destination = os.path.abspath(destination)
        dst_path = os.path.join(destination, os.path.basename(source))

        shutil.move(source, dst_path)
        print(f"Moved: {source} -> {dst_path}")
        
    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def move_folder(source, destination):
    """Move folder from one directory other directory."""
    try:
        if not os.path.exists(destination):
            print(f"Error: '{destination}' does not exist.")
            return

        if not os.path.isdir(destination):
            print(f"Error: '{destination}' is not a directory.")
            return
        
        if not os.path.exists(source):
            print(f"No folder matched: {source}")
            return

        if not os.path.isdir(source):
            print(f"{source} is not Folder")
            return

        dst_path = os.path.join(destination, os.path.basename(source))

        shutil.move(source, dst_path)
        print(f"Moved: {source} -> {dst_path}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def copy_file(source, destination):
    """Copy file from one directory other directory."""
    try:
        if not os.path.exists(destination):
            print(f"Error: '{destination}' does not exist.")
            return

        if not os.path.isdir(destination):
            print(f"Error: '{destination}' is not a directory.")
            return
                
        if not os.path.exists(source):
            print(f"No file matched: {source}")
            return

        if not os.path.isfile(source):
            print(f"{source} is not File")
            return

        dst_path = os.path.join(destination, os.path.basename(source))

        shutil.copy(source, dst_path)
        print(f"Copied: {source} -> {dst_path}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def copy_folder(source, destination):
    """Copy folder from one directory other directory."""
    try:
        if not os.path.exists(destination):
            print(f"Error: '{destination}' does not exist.")
            return

        if not os.path.isdir(destination):
            print(f"Error: '{destination}' is not a directory.")
            return
        
        if not os.path.exists(source):
            print(f"No folder matched: {source}")
            return

        if not os.path.isdir(source):
            print(f"{source} is not Folder")
            return

        dst_path = os.path.join(destination, os.path.basename(source))

        shutil.copytree(source, dst_path)
        print(f"Copied: {source} -> {dst_path}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")


def delete_file(source):
    """Delete file from directory."""
    try:
        if not os.path.exists(source):
            print(f"No file matched: {source}")
            return

        if os.path.isdir(source):
            print(f"{source} is a folder and can't be deleted")
            return

        os.remove(source)
        print(f"File deleted from -> {source}")

    except OSError as e:  # Fixed W0718
        print(f"Error: {e}")