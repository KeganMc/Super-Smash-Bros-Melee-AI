import sys
from PyQt5 import QtGui

class SmashGui(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initualizeWindow()
		#self.initualizeMenu()
		#self.initualizeButtons()
		#self.initualizeText()
		#self.initualizePlayerSelection()
		#self.show()

	def initalizeWindow(self):
		self.parent.setWindowTitle("Super Smash Bros AI")
		self.parent.setGeometry(500, 500, 450, 250)
		w.setWindowIcon(QtGui.QIcon("SmashIcon.ico"))

window = QtGui.QWidget()

SmashGui(window)

sys.exit(app.exec_())
