def run_quiz():
    print("=================================")
    print("   WELCOME TO THE TECH QUIZ!     ")
    print("=================================")
    
    # Questions, options, and correct answers (1-indexed)
    questions = [
        {
            "prompt": "What does CPU stand for?",
            "options": ["1. Central Process Unit", "2. Central Processing Unit", "3. Computer Personal Unit", "4. Control Processing Unit"],
            "answer": 2
        },
        {
            "prompt": "Which language is primarily used for Machine Learning and AI today?",
            "options": ["1. Python", "2. HTML", "3. SQL", "4. CSS"],
            "answer": 1
        },
        {
            "prompt": "What is the extension of a Python file?",
            "options": [".pt", ".pyt", ".py", ".pn"],
            "answer": 3
        }
    ]
    
    score = 0
    
    # Loop through each question
    for i, q in enumerate(questions):
        print(f"\nQuestion {i + 1}: {q['prompt']}")
        for option in q["options"]:
            print(option)
            
        try:
            choice = int(input("Enter your option number (1-4): "))
            if choice == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print("❌ Wrong!")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1 and 4.")

    # Final Score Display
    print("\n=================================")
    print(f" Quiz Over! Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent job! Perfect score!")
    else:
        print("👍 Good effort! Keep learning and coding!")
    print("=================================")

if __name__ == "__main__":
    run_quiz()
  
