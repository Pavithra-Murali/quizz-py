import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    {"question": "What is the capital of India?",
     "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
     "answer": "Delhi"},

    {"question": "Who developed Python?",
     "options": ["Elon Musk", "Guido van Rossum", "Linus Torvalds", "Bill Gates"],
     "answer": "Guido van Rossum"},

    {"question": "Which year was Python created?",
     "options": ["1991", "1989", "2000", "2010"],
     "answer": "1991"},

    {"question": "Which keyword is used to define a function in Python?",
     "options": ["func", "define", "def", "function"],
     "answer": "def"},

    {"question": "Which of these is a Python data type?",
     "options": ["Float", "Real", "Decimal", "Double"],
     "answer": "Float"},

    {"question": "What does GUI stand for?",
     "options": ["General User Interface", "Graphical User Interface", "Graphical Utility Interface", "None of these"],
     "answer": "Graphical User Interface"},

    {"question": "What symbol is used for comments in Python?",
     "options": ["//", "/* */", "#", "--"],
     "answer": "#"},

    {"question": "Which function is used to get user input in Python?",
     "options": ["scanf()", "input()", "get()", "read()"],
     "answer": "input()"},

    {"question": "Which loop is not available in Python?",
     "options": ["for", "while", "do-while", "None of these"],
     "answer": "do-while"},

    {"question": "Which operator is used for exponentiation in Python?",
     "options": ["^", "**", "//", "++"],
     "answer": "**"},

    {"question": "What does IDE stand for?",
     "options": ["Internal Development Environment", "Integrated Development Environment", "Intelligent Design Editor", "Integrated Data Environment"],
     "answer": "Integrated Development Environment"},

    {"question": "Which company developed Java?",
     "options": ["Oracle", "Sun Microsystems", "Google", "Microsoft"],
     "answer": "Sun Microsystems"},

    {"question": "What does HTML stand for?",
     "options": ["Hyperlinks and Text Markup Language", "Home Tool Markup Language", "Hyper Text Markup Language", "None of these"],
     "answer": "Hyper Text Markup Language"},

    {"question": "Which tag is used to create a hyperlink in HTML?",
     "options": ["<a>", "<link>", "<href>", "<hyper>"],
     "answer": "<a>"},

    {"question": "Which one is a version control system?",
     "options": ["Git", "Java", "Python", "MySQL"],
     "answer": "Git"},

    {"question": "Which file format is Python script saved as?",
     "options": [".js", ".py", ".java", ".exe"],
     "answer": ".py"},

    {"question": "Which module in Python is used for math operations?",
     "options": ["random", "os", "math", "sys"],
     "answer": "math"},

    {"question": "Which of these is not a Python IDE?",
     "options": ["PyCharm", "VS Code", "NetBeans", "Jupyter Notebook"],
     "answer": "NetBeans"},

    {"question": "What is the output of print(2 * 3 ** 2)?",
     "options": ["36", "18", "12", "None"],
     "answer": "18"},

    {"question": "Which keyword is used to handle exceptions in Python?",
     "options": ["catch", "error", "except", "try-catch"],
     "answer": "except"}

]

current_q = 0
score = 0

# Setup window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 14))
question_label.pack(pady=20)

selected_option = tk.StringVar()

radio_buttons = []
for _ in range(4):
    btn = tk.Radiobutton(root, text="", variable=selected_option, value="", font=("Arial", 12))
    btn.pack(anchor="w")
    radio_buttons.append(btn)

def load_question():
    q = questions[current_q]
    question_label.config(text=q["question"])
    selected_option.set(None)  # clear previous
    for i, opt in enumerate(q["options"]):
        radio_buttons[i].config(text=opt, value=opt)

def next_question():
    global current_q, score
    chosen = selected_option.get()
    if not chosen:
        messagebox.showwarning("Oops!", "Please select an option!")
        return
    if chosen == questions[current_q]["answer"]:
        score += 1
    current_q += 1
    if current_q >= len(questions):
        messagebox.showinfo("Quiz Completed", f"Your score: {score}/{len(questions)}")
        root.destroy()
    else:
        load_question()

submit_btn = tk.Button(root, text="Submit", command=next_question, font=("Arial", 12))
submit_btn.pack(pady=20)

load_question()  # load the first question

root.mainloop()
