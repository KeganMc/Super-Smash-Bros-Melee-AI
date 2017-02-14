import tkinter
import BigProject

window = tkinter.Tk()

# Launch BigProject.py
def BP():
	BigProject

# Set up title and icon
window.title("Super Smash Bros AI")
window.geometry("200x200")
window.wm_iconbitmap('SmashIcon.ico')

# Create and Add widgets
launch = tkinter.Button(window, text = "Launch Bot", command=BP)
launch.pack()


window.mainloop()

