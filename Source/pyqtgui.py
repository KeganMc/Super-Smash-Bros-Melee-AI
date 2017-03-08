import sys
from PyQt5 import QtGui

class SmashGui(QtGui.QMainWindow):

	def __init__(self):
		super(SmashGui, self).__init__()
		self.initualizeWindow()
		#self.initualizeMenu()
		#self.initualizeButtons()
		#self.initualizeText()
		#self.initualizePlayerSelection()
		self.show()

	def initalizeWindow(self):
		self.parent.setWindowTitle("Super Smash Bros AI")
		self.parent.setGeometry(500, 500, 450, 250)
		w.setWindowIcon(QtGui.QIcon("SmashIcon.ico"))

	def initializeButtons(self):
"""		save = Button(self.parent, text = "Save Bot").grid(row=5, column=1)
		load = Button(self.parent, text = "Load Bot").grid(row=5, column=2)
		launch = Button(self.parent, text = "Launch Bot", command=self.BP).grid(row=5, column=3)"""
		save = QtGui.QPushButton("Save", self)
		#save.clicked.connect(#save function here)
		load = QtGui.QPushButton("Load", self)
		#load.clicked.connect("Load function here)
		launch = QtGui.QPushButton("Launch", self)
		launch.clicked.connect(self.BP)

	# Launch BigProject.py
	def BP(self):
		BigProject

app = QtGui.QApplication(sys.argv)

GUI = SmashGui()

sys.exit(app.exec_())
