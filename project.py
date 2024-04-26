def load_questions(file_name):
    questions = []
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            i = 0
            while i < num_lines:
                question = lines[i].strip()
                if i + 5 < num_lines:  # Ensure there are enough lines for a full question set
                    options = [lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip()]
                    answer = lines[i+5].strip()
                    questions.append((question, options, answer))
                    i += 6  # Move to the next question
                else:
                    print(f"Error: Incomplete question set starting at line {i}")
                    break
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return questions

def select_quiz():
    print("Select a quiz:")
    print("1. HTML Quiz")
    print("2. CSS Quiz")
    print("3. JavaScript Quiz")
    print("4. Aptitude Quiz")
    choice = input("Enter your choice (1-4): ")
    return choice

def administer_quiz(questions):
    score = 0
    for i, (question, options, answer) in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

    print(f"You scored {score} out of {len(questions)}")

if __name__ == "__main__":
    quiz_choice = select_quiz()
    
    if quiz_choice == '1':
        file_name = "html_questions.txt"
    elif quiz_choice == '2':
        file_name = "css_questions.txt"
    elif quiz_choice == '3':
        file_name = "javascript_questions.txt"
    elif quiz_choice == '4':
        file_name = "aptitude_questions.txt"
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
        exit()

    # Load questions from the selected file
    quiz_questions = load_questions(file_name)
    
    # Administer the quiz
    administer_quiz(quiz_questions)
