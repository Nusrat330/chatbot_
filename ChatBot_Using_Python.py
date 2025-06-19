def ask_question(question, answer=None, options=None):
    print("\n" + question)
    if options:
        for i, opt in enumerate(options):
            print(f"{chr(65 + i)}) {opt}")
    user_answer = input("Your answer: ").strip()
    if answer:
        if user_answer.lower() == answer.lower():
            print("✅ Correct!")
        else:
            print(f"❌ Incorrect. The correct answer is: {answer}")
    else:
        print(f"Interesting! Let's move to the next question.")


questions = [
    {"question": "What is the output of: print(2 ** 3)?", "answer": "8"},
    {"question": "Which keyword is used to define a function in Python?", "answer": "def"},
    {"question": "Which of these is a mutable data type in Python?", "answer": "list"},
    {"question": "What does HTML stand for?", "answer": "HyperText Markup Language"},
    {"question": "Name a language primarily used for statistical computing.", "answer": "R"},
    {"question": "Which language is known for its use in AI and ML?", "answer": "Python"},
    {"question": "What does SQL stand for?", "answer": "Structured Query Language"},
    {"question": "What is the value of: len('Hello World')?", "answer": "11"},
    {"question": "Which tag is used to create a hyperlink in HTML?", "answer": "a"},
    {"question": "What is the use of 'break' in loops?", "answer": "To exit the loop"},
    {"question": "What does CSS stand for?", "answer": "Cascading Style Sheets"},
    {"question": "Which of the following is a Python web framework?", "answer": "Django"},
    {"question": "Which version control system is most commonly used?", "answer": "Git"},
    {"question": "What is recursion in programming?", "answer": None},
    {"question": "What is the use of 'return' in a function?", "answer": None},
    {"question": "Name a compiled programming language.", "answer": "C"},
    {"question": "What is the purpose of an IDE?", "answer": "To develop and debug code"},
    {"question": "What does OOP stand for?", "answer": "Object Oriented Programming"},
    {"question": "Which keyword is used to create a class in Python?", "answer": "class"},
    {"question": "What is the output of: print('2' + '3')?", "answer": "23"},
    {"question": "Which data structure uses FIFO?", "answer": "Queue"},
    {"question": "Which language runs in the browser?", "answer": "JavaScript"},
    {"question": "What does API stand for?", "answer": "Application Programming Interface"},
    {"question": "Name any Python data structure.", "answer": None},
    {"question": "What is the use of comments in code?", "answer": None}
]

print("🤖 Welcome to the Programming Chatbot!")
for q in questions:
    ask_question(q["question"], q.get("answer"))

print("\n🎉 Thanks for playing! Hope you learned something new.")

