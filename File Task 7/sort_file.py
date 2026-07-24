import argparse
import datetime

import file_manager
import selector_file

def main():
    parser = argparse.ArgumentParser(description="Custom File Manager")

    parser.add_argument(
        "--sort",
        action="store_true",
        help="sort the file or folder"
    )
    parser.add_argument(
        "--file",
        action="store_true",
        help="sort files"
    )
    parser.add_argument(
        "--folder",
        action="store_true",
        help="sort files"
    )

    args = parser.parse_args()

    if args.sort:

        if not args.file:
            parser.error("--file is required")

        if args.file:
            file_manager.sort_file(
                args.file
            )
        elif args.folder:
            file_manager.sort_folder(
                args.folder
            )
        else:
            parser.error(
                "Use either --file or --folder with --sort"
            )

