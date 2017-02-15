from tkinter import *
import BigProject

window = Tk()

# Launch BigProject.py
def BP():
	BigProject

# Set up title and icon
window.title("Super Smash Bros AI")
window.wm_iconbitmap('SmashIcon.ico')
window.geometry("400x300")

# Create and Add widgets
launch = Button(window, text = "Launch Bot", command=BP)
launch.pack()

window.mainloop()

