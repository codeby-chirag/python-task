import argparse
import file_manager

def main():
    parser = argparse.ArgumentParser(description="Custom file manager tool.")

    parser.add_argument(
        '--list',
        action='store_true', 
        help="List all files and folders in the directory"
    )
    parser.add_argument(
        '--list--files',
        action='store_true', 
        help="List files in the directory"
    )
    parser.add_argument(
        '--list--folder',
        action='store_true', 
        help="List folders in the directory"
    )

    # Arguments for moving files and folder
    # python3 "selector_file.py" --move --file "/home/chirag/Python Task/File Task 7/hello.txt" --destination "/home/chirag/Python Task/Task 1 to 5"
    parser.add_argument(
        "--move", 
        action="store_true", 
        help="Trigger the move operation"
    )
    parser.add_argument(
        "--file", 
        type=str, 
        help="Path of the file to move"
    )
    parser.add_argument(
        "--folder", 
        type=str, 
        help="Path of the file to move"
    )
    parser.add_argument(
        "--destination", 
        type=str, 
        help="Destination path for the file"
    )

    args = parser.parse_args()

    current_dir_path = "/home/chirag/Python Task/File Task 7"

    # Listing triggers
    if args.list:
        file_manager.current_dir(current_dir_path)

    elif args.list__files: 
        file_manager.curr_dir_file(current_dir_path)

    elif args.list__folder:
        file_manager.curr_dir_folder(current_dir_path)

    # Move file
    if args.movefile:
        if not args.file or not args.destination:
            parser.error("--move requires both --file and --destination.")
        
        file_manager.move_file(args.file, args.destination)

    # Move Folder
    if args.movefolder:
        if not args.file or not args.destination:
            parser.error("--move requires both --folder and --destination.")
        
        file_manager.move_folder(args.folder, args.destination)

if __name__ == "__main__":
    main()
