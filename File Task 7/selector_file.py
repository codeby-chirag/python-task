import file_manager

current_dir_path = "/home/chirag/Python Task/File Task 7"

command = input("Enter command you want tp perform: ")



if command == "--list":
    file_manager.current_dir(current_dir_path)

elif command == "* --list --ﬁle":
    file_manager.curr_dir_file(current_dir_path)

elif command == "* --list --folder":
    file_manager.curr_dir_folder(current_dir_path)

elif command == "* --move --ﬁle":
    destination_path = input("Enter path in which you want to move the file: ")
    file_pattern = input("Enter file Pattern or Name: ")

    file_manager.move_file(current_dir_path, file_pattern, destination_path)

elif command == "* --move --folder":
    destination_path = input("Enter path in which you want to move the folder: ")
    folder_pattern = input("Enter folder Pattern or Name: ")

    file_manager.move_file(current_dir_path, folder_pattern, destination_path)

elif command == "* --copy --ﬁle":
    destination_path = input("Enter path in which you want to copy: ")
    file_pattern = input("Enter file Pattern or Name: ")

    file_manager.copy_file(current_dir_path, file_pattern, destination_path) 

elif command == "* --copy --folder":
    destination_path = input("Enter path in which you want to copy: ")
    folder_pattern = input("Enter folder Pattern or Name: ")

    file_manager.copy_folder(current_dir_path, folder_pattern, destination_path) 

elif command == "* --delete ﬁle_name":
    file_pattern = input("Enter file Name: ")

    file_manager.rem_file(current_dir_path, file_pattern) 

