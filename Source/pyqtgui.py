import sys
from PyQt4 import QtGui

class SmashGui(QtGui.QMainWindow):

	def __init__(self):
		super(SmashGui, self).__init__()
		self.initualizeWindow()
		self.initualizeMenu()
		#self.initualizeButtons()
		#self.initualizeText()
		#self.initualizePlayerSelection()
		self.show()

	def initalizeWindow(self):
		self.parent.setWindowTitle("Super Smash Bros AI")
		self.parent.setGeometry(500, 500, 450, 250)
		w.setWindowIcon(QtGui.QIcon("SmashIcon.ico"))

	def initializeButtons(self):
		save = QtGui.QPushButton("Save", self)
		#save.clicked.connect(#save function here)
		load = QtGui.QPushButton("Load", self)
		#load.clicked.connect("Load function here)
		launch = QtGui.QPushButton("Launch", self)
		launch.clicked.connect(self.BP)

	def initializeMenu(self):
		fileAction = QtGui.QAction("New Game")
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(fileAction)
		aboutMenu = mainMenu.addMenu('&About')

	# Launch BigProject.py
	def BP(self):
		BigProject

app = QtGui.QApplication(sys.argv)

GUI = SmashGui()

sys.exit(app.exec_())
