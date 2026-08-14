import csv

def validate_username():
    with open("Test Module/Files/users.csv", "r") as f:
        user_name = input("Enter your user name: ").lower().strip()
        
        for line in f:
            user_data = line.split(",")

            if user_name == user_data[0].lower().strip():
                password = input("Enter Password: ").strip()
                if password == user_data[1].strip():
                    return True
                else:    
                    print(" Password does not match.")
                    return False
        
        print(" Username not found.")
        return False

def run_quiz():
    user_answers = []
    score = 0
    
    with open("Test Module/Files/questions.csv", "r") as q:
        for line in q:   
            que_data = [item.strip() for item in line.split(",")]
            
            if not que_data or len(que_data) < 6:
                continue
                
            question = que_data[0]
            options = que_data[1:5]
            correct_answer = que_data[5]

            print(f"\n {question}")
            
            for idx, option in enumerate(options, start=1):
                print(f"   {idx}. {option}")
            
            user_ans = input("Write your answer (or option number): ").strip()
            user_answers.append(user_ans)
            
            try:
                is_numeric_match = (user_ans.isdigit() and options[int(user_ans)-1].lower() == correct_answer.lower())
            except IndexError:
                is_numeric_match = False
                
            is_text_match = (user_ans.lower() == correct_answer.lower())

            if is_text_match or is_numeric_match:
                print(" Correct!")
                score += 1
            else:
                print(f" Incorrect! The right answer was: {correct_answer}")

                
    print("\n" + "="*30)
    print(f" Quiz Finished!")
    print(f" Your Answers: {user_answers}")
    print(f" Your Total Score: {score}")

if validate_username():
    print("\n User Verified! Starting your quiz")
    run_quiz()
