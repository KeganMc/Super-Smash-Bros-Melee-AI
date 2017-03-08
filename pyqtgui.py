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

app = QtGui.QApplication(sys.argv)

GUI = SmashGui()

sys.exit(app.exec_())
