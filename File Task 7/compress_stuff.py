"""Compress and Decompress the folder."""

import shutil
from pathlib import Path


def compress_file(path):
    """Compress the given directory."""
    dir_path = Path(path)

    if not dir_path.exists():
        print(f"Error: Path '{path}' does not exist.")
        return
    
    if not dir_path.is_dir():
            print(f"Error: Path '{path}' is not a directory.")
            return

    archive_name = dir_path.name

    # Creates the zip file
    shutil.make_archive(archive_name, "zip", dir_path)
    print(f"Successfully compressed '{dir_path.name}' into '{archive_name}.zip'")
    
def decompress_file(archive_path, extract_to=None):
    """Decompress the given directory."""
    archive_file = Path(archive_path)

    if not archive_file.exists():
        print(f"Error: Archive file '{archive_path}' does not exist.")
        return
    
    if not archive_file.is_file():
            print(f"Error: Path '{archive_path}' is not a file.")
            return
    
    try:
        shutil.unpack_archive(archive_file, extract_to, "zip")
        print(f"Successfully decompressed '{archive_path}'.")
    except shutil.ReadError:
        print(f"Error: '{archive_path}' is not a valid ZIP archive.")
