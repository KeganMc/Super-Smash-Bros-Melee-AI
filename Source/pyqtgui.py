import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtGui
"""
class SmashGui(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.initualizeWindow()
		self.initualizeMenu()
		self.initualizeButtons()
		self.initualizeText()
		self.initualizePlayerSelection()

	def initualizeWindow(self)
		self.parent.setWindowTitle("Super Smash Bros AI")
		self.parent.resize(250, 150)
		self.parent.move(300, 300)
"""
		
app = QApplication(sys.argv)

w = QWidget()
w.resize(250, 250)
w.move(300, 300)
w.show()
w.setWindowIcon(QtGui.QIcon("SmashIcon.ico"))

sys.exit(app.exec_())
