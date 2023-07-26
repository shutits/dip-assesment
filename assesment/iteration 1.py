import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SurveyApp(tk.Tk):
    def __init__(self, questions):
        super().__init__()
        self.title("Shaha Fitness") #giving my first webpage a name
        self.geometry("1000x800") #resizing the messagebox for the webpage
        self.questions = questions
        self.answers = []
#setting up the function for the user's survey
        self.current_question = 0

        self.question_label = tk.Label(self, text=self.questions[self.current_question][0])
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()

        self.radio_buttons = []
        for i, option in enumerate(self.questions[self.current_question][1]):
            radio_button = tk.Radiobutton(self, text=option, variable=self.var, value=i+1)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.next_button = ttk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

#creating a pop-up warning message which will disappear after 3 seconds
    def warning(self):
        warning_label = tk.Label(text='Please select an option', fg='red')
        warning_label.pack(pady=5)
        self.after(3000, warning_label.destroy) #after 3 seconds, the pop up disappear

    def next_question(self):
        answer = self.var.get()
        if answer:
            self.answers.append(answer)
            self.current_question += 1
            self.var.set("")

            if self.current_question < len(self.questions):
                self.question_label.config(text=self.questions[self.current_question][0])
                self.update_radio_buttons()
            else:
                self.show_results()
        else:
            self.warning()

    def update_radio_buttons(self):
        for radio_button, option in zip(self.radio_buttons, self.questions[self.current_question][1]):
            radio_button.config(text=option)

    def show_results(self):
        self.question_label.pack_forget()
        self.next_button.pack_forget()
        for radio_button in self.radio_buttons:
            radio_button.pack_forget()

        result_label = tk.Label(self, text="Survey Results:")
        result_label.pack(pady=20)

        for i, answer in enumerate(self.answers):
            answer_label = tk.Label(self, text="Question {}: Option {}".format(i + 1, answer))
            answer_label.pack()

        destroy_button = ttk.Button(self, text="Proceed to your program", command=self.destroy_window)
        destroy_button.pack(pady=10)

    def destroy_window(self):
        self.destroy()

def show_webpage():
    # Creating the main window for my fitness webpage
    root = tk.Tk()
    root.title("Shaha Fitness")

    # resiszing the picture that will be used on the webpage
    image = Image.open(r"arnie.jpg")
    image = image.resize((1000, 800), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Creating a label to display the image used on the webpage
    label_image = ttk.Label(root, image=photo)
    label_image.pack(pady=10)

    # Customizing the motivational quote for my webpage
    quote = "Don't stop until you're proud"
    label_quote = ttk.Label(root, text=quote, font=("Helvetica", 16))
    label_quote.pack(pady=10)

    #  creating the function to destroy the current window and move to the next page
    def destroy_window():
        root.destroy()
        show_next_page()

    # Creating the "Next" button for the first desktop of the webpage
    next_button = ttk.Button(root, text="Next", command=destroy_window)
    next_button.pack(pady=10)

    root.mainloop()

#survey questions for the user
def show_next_page():
    survey_questions = [
        ("Question #1: How many days a week would you like to train? ", ["3 day", "4 days", "5 days", "6 days"]),
        ("Question #2: What's your favourite muscle group to train?", ["Chest", "Back", "Legs", "Arms"]),
        ("Question #3: What's your preferred cardio exercise?", ["Running", "Cycling", "Swimming", "Jumping rope"]),
        ("Question #4: What rep range do you like to work at?", ["6-8 (Strength Training)", "8-12 (Hypertrophy Training)", "12-15 (Muscle Endurance)", "15+ (Training till failure)"]),
    ]
    survey_app = SurveyApp(survey_questions)
    survey_app.mainloop()

if __name__ == "__main__":
    show_webpage()

def create_push_pull_legs_page():
    # Create the main window for the Push-Pull-Legs webpage for iteration 1
    root = tk.Tk()
    root.title("Shaha Fitness")

    # Creating the push section
    push_label = ttk.Label(root, text="Push Section", font=("Helvetica", 16))
    push_label.pack(pady=20)

    push_exercises = [
        "Bench Press",
        "Overhead Press",
        "Push-ups",
        "Tricep Dips",
        "Incline Dumbell Press",
        "Decline Barbell Press",
        "Chest Press",
        "Chest Flies/ Pec Deck",
        "Tricep Extensions",
    ]
    push_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12))
    for exercise in push_exercises:
        push_listbox.insert(tk.END, exercise)
    push_listbox.pack()

    # pull section
    pull_label = ttk.Label(root, text="Pull Section", font=("Helvetica", 16))
    pull_label.pack(pady=20)

    pull_exercises = [
        "Pull-ups",
        "Barbell Rows",
        "Lat Pulldowns",
        "Bicep Curls",
        "Ez Bar Curls",
        "Hammer Curls",
        "Seated Rows",
        "Dumbell Rows",
        "Dumbell Shrugs",
        "Wide Grip Rows",
    ]
    pull_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12))
    for exercise in pull_exercises:
        pull_listbox.insert(tk.END, exercise)
    pull_listbox.pack()

    # legs section
    legs_label = ttk.Label(root, text="Legs Section", font=("Helvetica", 16))
    legs_label.pack(pady=20)

    legs_exercises = [
        "Squats",
        "Deadlifts",
        "Lunges",
        "Leg Press",
        "Legs Extension",
        "Leg Curls",
        "Seated Calf Raises",
        "Goblet Squats",
    ]
    legs_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12))
    for exercise in legs_exercises:
        legs_listbox.insert(tk.END, exercise)
    legs_listbox.pack()

    root.mainloop()

if __name__ == "__main__":
    create_push_pull_legs_page()