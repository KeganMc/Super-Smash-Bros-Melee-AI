from tkinter import *
import BigProject

window = Tk()

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

# Launch BigProject.py
def BP():
	BigProject

# Set up title and icon
window.title("Super Smash Bros AI")
window.geometry("200x200")
window.wm_iconbitmap('SmashIcon.ico')

myframe = Frame(window)
myframe.pack(fill=BOTH, expand=YES)
mycanvas = ResizingCanvas(myframe,width=0, height=0, bg="cyan", highlightthickness=0)
mycanvas.pack(fill=BOTH, expand=YES)

# Create and Add widgets
launch = Button(window, text = "Launch Bot", command=BP)
launch.pack()

# tag all of the drawn widgets
mycanvas.addtag_all("all")
window.mainloop()

