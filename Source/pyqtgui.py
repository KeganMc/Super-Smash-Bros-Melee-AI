import sys
import BigProject
import webbrowser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

global load
global save
global training
global mName
global botRelations
global player1
global player1Agent
global player2
global player2Agent
global player3
global player3Agent
global player4
global player4Agent


#class SmashGui(QWidget)
class SmashGui(QMainWindow):

	def __init__(self):
		super().__init__()
		global load
		global save
		global training
		global mName
		global player1
		global player1Agent
		global player2
		global player2Agent
		global player3
		global player3Agent
		global player4
		global player4Agent

		load = False
		save = ''
		training = False
		mName = ''
		player1 = 'None'
		player2 = 'None'
		player3 = 'None'
		player4 = 'None'
		player1Agent = False
		player2Agent = False
		player3Agent = False
		player4Agent = False

		self.initializeWindow()
		self.initializeMenu()
		self.initializeButtons()
		self.initializeText()
		self.initializePlayerSelection()
		self.show()

	def initializeWindow(self):
		self.setWindowTitle("Super Smash Bros AI")
		self.setGeometry(300, 200, 900, 500)
		self.setWindowIcon(QIcon("SmashIcon.png"))
		self.smashPix = QLabel(self)
		pixmap = QPixmap("SmashIcon.png")
		self.smashPix.setScaledContents(True)
		self.smashPix.setPixmap(pixmap.scaled(200,200))
		self.smashPix.resize(200,200)
		self.smashPix.move(350,75)

	def initializeButtons(self):
		self.save = QPushButton("Save", self)
		self.save.move(400,450)
		self.save.setFixedWidth(100)
		self.save.setFixedHeight(50)
		self.save.clicked.connect(self.saveMenu)
		self.load = QPushButton("Load", self)
		self.load.move(300,450)
		self.load.setFixedWidth(100)
		self.load.setFixedHeight(50)
		self.load.clicked.connect(self.loadMenu)
		self.launch = QPushButton("Launch", self)
		self.launch.move(500,450)
		self.launch.setFixedWidth(100)
		self.launch.setFixedHeight(50)
		self.launch.clicked.connect(self.launchApp)

	def initializeMenu(self):
		self.mainMenu = self.menuBar()
		self.fileMenu = self.mainMenu.addMenu('File')

		self.exitButton = QAction('Exit', self)
		self.exitButton.setShortcut('Ctrl+Q')
		self.exitButton.setStatusTip('Exit Application')
		self.exitButton.triggered.connect(self.onExit)

		self.aboutButton = QAction('About', self)
		self.aboutButton.setStatusTip('About Application')
		#aboutAction.triggered.connect(self.about)

		self.fileMenu.addAction(self.aboutButton)
		self.fileMenu.addAction(self.exitButton)

	def initializeText(self):
		font = QFont("SansSerif",18,QFont.Bold)
		self.playerOne = QLabel(self, text = "Player 1: ")
		self.playerOne.move(50, 100)
		self.playerOne.setFont(font)
		self.playerTwo = QLabel(self, text = "Player 2: ")
		self.playerTwo.move(600, 100)
		self.playerTwo.setFont(font)
		self.playerThree = QLabel(self, text = "Player 3: ")
		self.playerThree.move(50, 200)
		self.playerThree.setFont(font)
		self.playerFour = QLabel(self, text = "Player 4: ")
		self.playerFour.move(600, 200)
		self.playerFour.setFont(font)

	def initializePlayerSelection(self):
		self.playerOneSelection = QComboBox(self)
		self.playerOneSelection.addItems(["None", "Team 1", "Team 2", "Team 3", "Team 4"])
		self.playerOneSelection.move(150,100)
		self.playerOneSelection.currentIndexChanged.connect(lambda:self.checkComboState(self.playerOneSelection, 1))
		self.playerOneCheck = QCheckBox("AI Agent", self)
		self.playerOneCheck.move(150,150)
		self.playerOneCheck.stateChanged.connect(lambda:self.checkBtnState(self.playerOneCheck, self.playerOneCheck.text()+"1"))
		self.playerTwoSelection = QComboBox(self)
		self.playerTwoSelection.addItems(["None", "Team 1", "Team 2", "Team 3", "Team 4"])
		self.playerTwoSelection.move(700,100)
		self.playerTwoSelection.currentIndexChanged.connect(lambda:self.checkComboState(self.playerTwoSelection, 2))
		self.playerTwoCheck = QCheckBox("AI Agent", self)
		self.playerTwoCheck.move(700,150)
		self.playerTwoCheck.stateChanged.connect(lambda:self.checkBtnState(self.playerTwoCheck, self.playerTwoCheck.text()+"2"))
		self.playerThreeSelection = QComboBox(self)
		self.playerThreeSelection.addItems(["None", "Team 1", "Team 2", "Team 3", "Team 4"])
		self.playerThreeSelection.move(150,200)
		self.playerThreeSelection.currentIndexChanged.connect(lambda:self.checkComboState(self.playerThreeSelection, 3))
		self.playerThreeCheck = QCheckBox("AI Agent", self)
		self.playerThreeCheck.move(150,250)
		self.playerThreeCheck.stateChanged.connect(lambda:self.checkBtnState(self.playerThreeCheck, self.playerThreeCheck.text()+"3"))
		self.playerFourSelection = QComboBox(self)
		self.playerFourSelection.addItems(["None", "Team 1", "Team 2", "Team 3", "Team 4"])
		self.playerFourSelection.move(700,200)
		self.playerFourSelection.currentIndexChanged.connect(lambda:self.checkComboState(self.playerFourSelection, 4))
		self.playerFourCheck = QCheckBox("AI Agent", self)
		self.playerFourCheck.move(700,250)
		self.playerFourCheck.stateChanged.connect(lambda:self.checkBtnState(self.playerFourCheck, self.playerFourCheck.text()+"4"))
		self.trainingCheck = QCheckBox("Train the Bot?", self)
		self.trainingCheck.move(395,350)
		self.trainingCheck.stateChanged.connect(lambda:self.checkBtnState(self.trainingCheck, self.trainingCheck.text()))

	def checkBtnState(self, button, buttonText):
		global player1Agent
		global player2Agent
		global player3Agent
		global player4Agent
		global training

		if buttonText == "AI Agent1":
			if button.isChecked() == True:
				player1Agent = True
			else:
				player1Agent = False
		elif buttonText == "AI Agent2":
			if button.isChecked() == True:
				player2Agent = True
			else:
				player2Agent = False
		elif buttonText == "AI Agent3":
			if button.isChecked() == True:
				player3Agent = True
			else:
				player3Agent = False
		elif buttonText == "AI Agent4":
			if button.isChecked() == True:
				player4Agent = True
			else:
				player4Agent = False
		elif buttonText == "Train the Bot?":
			if button.isChecked() == True:
				training = True
			else:
				training = False

	def checkComboState(self, dropDown, index):
		global player1
		global player2
		global player3
		global player4

		if index == 1:
			player1 = dropDown.currentText()
		elif index == 2:
			player2 = dropDown.currentText()
		elif index == 3:
			player3 = dropDown.currentText()
		else:
			player4 = dropDown.currentText()

	def createBotRelations(self):
		global player1
		global player2
		global player3
		global player4
		global player1Agent
		global player2Agent
		global player3Agent
		global player4Agent

		player1List = []
		player2List = []
		player3List = []
		player4List = []
		relations = []

		if player1 != "None":
			if player1Agent:
				player1List.append(1)
				if player2 != "None":
					if player2 != player1:
						player1List.append(2)
					else:
						player1List.append(3)
				else:
					player1List.append(0)
				if player3 != "None":
					if player3 != player1:
						player1List.append(2)
					else:
						player1List.append(3)
				else:
					player1List.append(0)
				if player4 != "None":
					if player4 != player1:
						player1List.append(2)
					else:
						player1List.append(3)
				else:
					player1List.append(0)
				relations.append(player1List)
		if player2 != "None":
			if player2Agent:
				if player1 != "None":
					if player1 != player2:
						player2List.append(2)
					else:
						player2List.append(3)
				else:
					player2List.append(0)
				player2List.append(1)
				if player3 != "None":
					if player3 != player2:
						player2List.append(2)
					else:
						player2List.append(3)
				else:
					player2List.append(0)
				if player4 != "None":
					if player4 != player2:
						player2List.append(2)
					else:
						player2List.append(3)
				else:
					player2List.append(0)
				relations.append(player2List)
		if player3 != "None":
			if player3Agent:
				if player1 != "None":
					if player1 != player3:
						player3List.append(2)
					else:
						player3List.append(3)
				else:
					player3List.append(0)
				if player2 != "None":
					if player2 != player3:
						player3List.append(2)
					else:
						player3List.append(3)
				else:
					player3List.append(0)
				player3List.append(1)
				if player4 != "None":
					if player4 != player3:
						player3List.append(2)
					else:
						player3List.append(3)
				else:
					player3List.append(0)
				relations.append(player3List)
		if player4 != "None":
			if player4Agent:
				if player1 != "None":
					if player1 != player4:
						player4List.append(2)
					else:
						player4List.append(3)
				else:
					player4List.append(0)
				if player2 != "None":
					if player2 != player4:
						player4List.append(2)
					else:
						player4List.append(3)
				else:
					player4List.append(0)
				if player3 != "None":
					if player3 != player4:
						player4List.append(2)
					else:
						player4List.append(3)
				else:
					player4List.append(0)
				player4List.append(1)
				relations.append(player4List)
		return relations

	# Launch BigProject.py
	def launchApp(self):
		global load
		global save
		global training
		global mName

		if mName == '':
			loadInput = QInputDialog.getText(self, "New Training Model", "Please enter a name for the new model", QLineEdit.Normal, "")
			if loadInput[1] == False:
				return None
			elif loadInput[0] != "":
				mName = loadInput[0]
				

		botRelations = self.createBotRelations()

		self.bigProject = BigProject
		print(botRelations)
		print(training)
		print(load)
		print(mName)
		self.bigProject.runBots(botRelations, training, load, mName, True)

		#BigProject

	def saveMenu(self):
		print("save")


	def loadMenu(self):
		global load
		global mName

		loadDialog = QFileDialog()
		loadDialog.setFileMode(QFileDialog.AnyFile)
		#loadDialog.setFilter() --FILTER FOR TENSOR files

		if loadDialog.exec_():
			print('inside')
			load = True
			mName = loadDialog.selectedFiles()

	def onExit(self):
		self.close

app = QApplication(sys.argv)

GUI = SmashGui()

sys.exit(app.exec_())
