import sys
import BigProject
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QPushButton, qApp
from PyQt5.QtGui import QIcon

#class SmashGui(QWidget)
class SmashGui(QMainWindow):

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
		save = QPushButton("Save Bot", self)
		load = QPushButton("Load Bot", self)
		launch = QPushButton("Launch Bot", self)

		launch.move(100, 20)
		load.move(200, 20)
		save.move(300, 20)

		launch.clicked.connect(self.BP)
		load.clicked.connect(self.load)
		save.clicked.connect(self.save)

	def initializeMenu(self):
		exitAction = QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit Application')
		exitAction.triggered.connect(qApp.quit)

		aboutAction = QAction('&About', self)
		aboutAction.setStatusTip('About')
		aboutAction.triggered.connect(self.about)	

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')

		fileMenu.addAction(exitAction)
		fileMenu.addAction(aboutAction)

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
