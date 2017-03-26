from tkinter import *
import BigProject

class smashGui(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initualizeWindow()
		self.initualizeMenu()
		self.initualizeButtons()
		self.initualizeText()
		self.initualizePlayerSelection()

	def initualizeWindow(self):
		self.parent.title("Super Smash Bros AI")
		self.parent.tk.iconbitmap(self,default='SmashIcon.ico')
		self.parent.geometry("400x300")
		##self.parent.eval('tk::PlaceWindow %s center' % self.parent.winfo_toplevel())
		self.parent.configure(background = "#FFFFFF")

	def initualizeMenu(self):
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)

		fileMenu = Menu(menubar)
		fileMenu.add_command(label="About")
		fileMenu.add_command(label="Exit", command=self.onExit)

		menubar.add_cascade(label="File", menu=fileMenu)

	def initualizeButtons(self):
		# Create and Add widgets
		save = Button(self.parent, text = "Save Bot").grid(row=5, column=1)
		load = Button(self.parent, text = "Load Bot").grid(row=5, column=2)
		launch = Button(self.parent, text = "Launch Bot", command=self.BP).grid(row=5, column=3)

	def initualizeText(self):
		playerOne = Label(self.parent, text = "Player 1: ").grid(row=0, column=0)
		playerTwo = Label(self.parent, text = "Player 2: ").grid(row=1, column=0)
		playerThree = Label(self.parent, text = "Player 3: ").grid(row=2, column=0)
		playerFour = Label(self.parent, text = "Player 4: ").grid(row=3, column=0)

	def initualizePlayerSelection(self):
		variableOne = StringVar(self.parent)
		variableOne.set("None")
		variableTwo = StringVar(self.parent)
		variableTwo.set("None")
		variableThree = StringVar(self.parent)
		variableThree.set("None")
		variableFour = StringVar(self.parent)
		variableFour.set("None")

		playerOneSelection = OptionMenu(self.parent, variableOne, "None", "Human", "AI").grid(row=0, column=1)
		playerTwoSelection = OptionMenu(self.parent, variableTwo, "None", "Human", "AI").grid(row=1, column=1)
		playerThreeSelection = OptionMenu(self.parent, variableThree, "None", "Human", "AI").grid(row=2, column=1)
		playerFourSelection = OptionMenu(self.parent, variableFour, "None", "Human", "AI").grid(row=3, column=1)


	# Launch BigProject.py
	def BP():
		BigProject


	def onExit(self):
		self.quit()


window = Tk()
smashGui(window)
window.mainloop()
