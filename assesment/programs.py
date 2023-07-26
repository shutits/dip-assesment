import tkinter as tk
from tkinter import ttk

def create_push_pull_legs_page():
    # Create the main window for the Push-Pull-Legs webpage for iteration 1
    root = tk.Tk()
    root.title("Push-Pull-Legs Workout")

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
