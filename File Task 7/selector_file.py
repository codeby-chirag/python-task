import argparse
import file_manager


def main():

    parser = argparse.ArgumentParser(
        description="Custom File Manager"
    )

    # List operations
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all files and folders"
    )

    parser.add_argument(
        "--list-files",
        action="store_true",
        help="List only files"
    )

    parser.add_argument(
        "--list-folder",
        action="store_true",
        help="List only folders"
    )

    # Move operation
    parser.add_argument(
        "--move",
        action="store_true",
        help="Move file or folder"
    )
    # Copy operation
    parser.add_argument(
        "--copy",
        action="store_true",
        help="copy file or folder"
    )
    # Delete
    parser.add_argument(
        "--delete",
        action="store_true",
        help="delete file"
    )

    # File, Folder and Destination Path
    parser.add_argument(
        "--file",
        type=str,
        help="File path"
    )

    parser.add_argument(
        "--folder",
        type=str,
        help="Folder path"
    )

    parser.add_argument(
        "--destination",
        type=str,
        help="Destination path"
    )

    args = parser.parse_args()

    current_dir_path = "/home/chirag/Python Task/File Task 7"

    # Listing
    if args.list:
        file_manager.current_dir(current_dir_path)

    elif args.list_files:
        file_manager.curr_dir_file(current_dir_path)

    elif args.list_folder:
        file_manager.curr_dir_folder(current_dir_path)

    # Moving
    elif args.move:

        if not args.destination:
            parser.error("--destination is required.")

        if args.file:
            file_manager.move_file(
                args.file,
                args.destination
            )
        elif args.folder:
            file_manager.move_folder(
                args.folder,
                args.destination
            )
        else:
            parser.error(
                "Use either --file or --folder with --move."
            )

    # Copy
    elif args.copy:

        if not args.destination:
            parser.error("--destination is required.")

        if args.file:
            file_manager.copy_file(
                args.file,
                args.destination
            )
        elif args.folder:
            file_manager.copy_folder(
                args.folder,
                args.destination
            )
        else:
            parser.error(
                "Use either --file or --folder with --copy."
            )

    elif args.delete:

        if args.folder:
            print("Folder cant't be deleted")
        elif args.file:
            file_manager.delete_file(
                args.file
            )
        else:
            print("User must with --file")

if __name__ == "__main__":
    main()