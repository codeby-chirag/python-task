import argparse
import os

import compress_stuff
import file_manager
import sort_file


def main():

    parser = argparse.ArgumentParser(description="Custom File Manager")

    # List operations
    parser.add_argument(
        "--list", action="store_true", help="List all files and folders"
    )

    # Move operation
    parser.add_argument("--move", action="store_true", help="Move file or folder")
    # Copy operation
    parser.add_argument("--copy", action="store_true", help="copy file or folder")
    # Delete
    parser.add_argument("--delete", action="store_true", help="delete file")
    # Sort
    parser.add_argument("--sort", action="store_true", help="sort the file or folder")
    # Compress
    parser.add_argument("--compress", action="store_true", help="Compress folders")
    parser.add_argument(
        "--filename", action="store_true", help="new file name which you want to give"
    )
    parser.add_argument("--decompress", action="store_true", help="DeCompress folders")

    # File, Folder and Destination Path
    parser.add_argument(
        "--file", action="store_true", help="Perform operation on files"
    )

    parser.add_argument(
        "--folder", action="store_true", help="Perform operation on folders"
    )

    parser.add_argument("--path", type=str, help="Path of file or folder")

    parser.add_argument("--destination", type=str, help="Destination path")

    args = parser.parse_args()

    # current_dir_path = "/home/chirag/Python Task/File Task 7"
    directory = args.path if args.path else os.getcwd()

    # Listing
    if args.list:

        if args.file:
            file_manager.curr_dir_file(directory)

        elif args.folder:
            file_manager.curr_dir_folder(directory)

        else:
            file_manager.current_dir(directory)

    # Moving
    elif args.move:

        if not args.destination:
            parser.error("--destination is required.")

        if not args.path:
            parser.error("--path is required.")

        if args.file:
            file_manager.move_file(args.path, args.destination)

        elif args.folder:
            file_manager.move_folder(args.path, args.destination)
        else:
            parser.error("Use either --file or --folder with --move.")

    # Copy
    elif args.copy:

        if not args.destination:
            parser.error("--destination is required.")

        if not args.path:
            parser.error("--path is required.")

        if args.file:
            file_manager.copy_file(args.path, args.destination)

        elif args.folder:
            file_manager.copy_folder(args.path, args.destination)
        else:
            parser.error("Use either --file or --folder with --copy.")

    # Delete
    elif args.delete:

        if args.folder:
            print("Folder can't be deleted")

        elif args.file:

            if not args.path:
                parser.error("--path is required.")

            file_manager.delete_file(args.path)
        else:
            print("User must with --file")

    # Sorting
    elif args.sort:

        if not args.path:
            parser.error("--path is required.")

        if args.file:
            sort_file.sort_file(args.path)

        elif args.folder:
            sort_file.sort_folder(args.path)
        else:
            parser.error("Use either --file or --folder with --sort")

    # Compress
    elif args.compress:
        compress_stuff.compress_file(args.path)
    
    # Decompress
    elif args.decompress:
        compress_stuff.decompress_file(args.path)


if __name__ == "__main__":
    main()
