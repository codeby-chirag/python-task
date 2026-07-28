"""This module handles the main file tasks for Task 7.

All command's function call by this file.
"""

import argparse
import os

from compress_stuff import compress_file, decompress_file
from file_manager import (
    copy_file,
    copy_folder,
    curr_dir_file,
    curr_dir_folder,
    current_dir,
    delete_file,
    move_file,
    move_folder,
)
from sort_file import sort_file, sort_folder


def main():
    """Execute the core file processing operations."""
    parser = argparse.ArgumentParser(description="Custom File Manager")

    operation = parser.add_mutually_exclusive_group(required=True)

    operation.add_argument(
        "--list", action="store_true", help="List files and/or folders"
    )

    operation.add_argument("--move", action="store_true", help="Move file or folder")

    operation.add_argument("--copy", action="store_true", help="Copy file or folder")

    operation.add_argument("--delete", action="store_true", help="Delete file")

    operation.add_argument("--sort", action="store_true", help="Sort files or folders")

    operation.add_argument(
        "--compress", action="store_true", help="Compress file or folder"
    )

    operation.add_argument(
        "--decompress", action="store_true", help="Decompress archive"
    )

    parser.add_argument("--filename", type=str, help="New file name")

    parser.add_argument(
        "--file", action="store_true", help="Perform operation on files"
    )

    parser.add_argument(
        "--folder", action="store_true", help="Perform operation on folders"
    )

    parser.add_argument("--path", type=str, help="Path of file or folder")

    parser.add_argument("--destination", type=str, help="Destination path")

    args = parser.parse_args()

    # Convert relative paths to absolute paths automatically
    if args.path:
        parent_path = os.path.abspath(os.path.join("..", args.path))
        if os.path.exists(parent_path) or not os.path.exists(args.path):
            args.path = parent_path
        else:
            args.path = os.path.abspath(args.path)

    if args.destination:
        parent_dest = os.path.abspath(os.path.join("..", args.destination))
        if os.path.exists(parent_dest) or not os.path.exists(args.destination):
            args.destination = parent_dest
        else:
            args.destination = os.path.abspath(args.destination)

    directory = args.path if args.path else os.getcwd()

    # Listing
    if args.list:

        if args.file:
            curr_dir_file(directory)

        elif args.folder:
            curr_dir_folder(directory)

        else:
            current_dir(directory)

    # Moving
    elif args.move:

        if not args.destination:
            parser.error("--destination is required.")

        if not args.path:
            parser.error("--path is required.")

        if args.file:
            move_file(args.path, args.destination)

        elif args.folder:
            move_folder(args.path, args.destination)
        else:
            parser.error("Use either --file or --folder with --move.")

    # Copy
    elif args.copy:

        if not args.destination:
            parser.error("--destination is required.")

        if not args.path:
            parser.error("--path is required.")

        if args.file:
            copy_file(args.path, args.destination)

        elif args.folder:
            copy_folder(args.path, args.destination)
        else:
            parser.error("Use either --file or --folder with --copy.")

    # Delete
    elif args.delete:

        if args.folder:
            print("Folder can't be deleted")

        elif args.file:

            if not args.path:
                parser.error("--path is required.")

            delete_file(args.path)
        else:
            print("User must with --file")

    # Sorting
    elif args.sort:

        if not args.path:
            parser.error("--path is required.")

        if args.file:
            sort_file(args.path)

        elif args.folder:
            sort_folder(args.path)
        else:
            parser.error("Use either --file or --folder with --sort")

    # Compress
    elif args.compress:
        compress_file(args.path)

    # Decompress
    elif args.decompress:
        decompress_file(args.path)


if __name__ == "__main__":
    main()
