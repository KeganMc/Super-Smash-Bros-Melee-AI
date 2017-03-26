import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class SmashGui(QWidget):

	def __init__(self):
		super().__init__()
		self.initializeWindow()
		#self.initualizeMenu()
		self.initializeButtons()
		#self.initualizeText()
		#self.initualizePlayerSelection()
		self.show()

	def initializeWindow(self):
		self.setWindowTitle("Super Smash Bros AI")
		self.setGeometry(500, 500, 450, 250)
		self.setWindowIcon(QIcon("SmashIcon.ico"))

	def initializeButtons(self):
		save = QPushButton("Save", self)
		save.clicked.connect(self.save)
		load = QPushButton("Load", self)
		load.clicked.connect(self.load)
		launch = QPushButton("Launch", self)
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

	def save(self):
		print('Save pushed')

	def load(self):
		print('Load pushed')

app = QApplication(sys.argv)

GUI = SmashGui()

sys.exit(app.exec_())
