import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def show_webpage():
    # Create the main application window
    root = tk.Tk()
    root.title("Motivational Webpage")

    # Load and resize the image
    image = Image.open("C:\Users\shubh\Downloads\arnie.jpg")
    image = image.resize((800, 600), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)

    # Creating a label to display the image
    label_image = ttk.Label(root, image=photo)
    label_image.pack(pady=10)

    # Customizing my motivational quote for the webpage
    quote = "Your motivational quote goes here."
    label_quote = ttk.Label(root, text=quote, font=("Helvetica", 16))
    label_quote.pack(pady=10)

    # Run the GUI application
    root.mainloop()

if __name__ == "__main__":
    show_webpage()
