x = input("Please enter a Paragraph: ")
y = input("You want to update any word? Yes or No: ")

if (y == "Yes"):
    edit_word = input("Which word you want to edit? ")
    new_word = input("Enter new word: ")
    
    if edit_word in x: 
        x = x.replace(edit_word, new_word) 
        print("Updated paragraph:", x)

        delete_word = input("You want to delete any word? Yes or No: ")

        if (delete_word == "Yes"):
            remove_word = input("Which word you want to Delete? ")

            if remove_word in x:
                x = x.replace(remove_word, "")
                print("Updated paragraph:", x)
    else:
        print("Word not found in the paragraph.")




