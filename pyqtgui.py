import sys
import BigProject
from PyQt4 import QtGui

class SmashGui(QtGui.QMainWindow):

	def __init__(self):
		super(SmashGui, self).__init__()
		self.setGeometry(500, 500, 450, 250)
		self.setWindowTitle("Super Smash Bros AI")
		self.setWindowIcon(QtGui.QIcon('SmashIcon.ico'))
		self.show()
		#self.initualizeMenu()
		self.initualizeButtons()
		#self.initualizeText()
		#self.initualizePlayerSelection()

	def initualizeButtons(self):
		# Create buttons
		# btn.move(x,y)
		save = QtGui.QPushButton("Save", self)
		load = QtGui.QPushButton("Load", self)
		launch = Button("Launch Bot", self)
		launch.clicked.connect(self.BP())

	# Launch BigProject.py
	def BP():
		BigProject


	def onExit(self):
		self.quit()

app = QtGui.QApplication(sys.argv)

GUI = SmashGui()

sys.exit(app.exec_())
