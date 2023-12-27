import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create the main window
window = tkinter.Tk()
window.title("Catch me if you can")

# Create a canvas inside the main window
canvas = tkinter.Canvas(window, width=800, height=600, bg="Light Blue")
canvas.pack(fill=tkinter.BOTH, expand=True)

# Create a label and place it at the top center of the canvas
label = tkinter.Label(canvas, text="Are you a loser?", font=('consolas', 40), bg='lightblue')
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

# Function called when "yes" button is clicked
def catchme():
    button.config(text="then catch me if you can :)", font=('consolas', 40), command=teleport)

# Function called when "no" button is clicked
def for_real():
    yes.config(text="I knew")

# Function to teleport the "no" button to a random position
def teleport():
    button.place(x=random.randint(0, 100), y=random.randint(0, 100))
    button.config(text="no", command=catchme)
    button.config(bg=random.choice(["red", "blue", "green", "yellow", "pink"]))

# Create the "yes" button, set its appearance, and place it at a specific position on the canvas
yes = tkinter.Button(canvas, text="yes", font=('consolas', 40), command=for_real)
yes.place(relx=0.3, rely=0.8, anchor=tkinter.CENTER)

# Create the "no" button, set its aёppearance, and place it at a specific position on the canvas
button = tkinter.Button(canvas, text="no", font=('consolas', 40), command=teleport)
button.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)

# Start the main event loop
window.mainloop()
