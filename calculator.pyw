# calculator.pyw

"""calculator.pyw
A simply GUI calculator from Zelle's Python Programming"""

from graphics import *
from button import Button


class Calculator:
	# This class makes a simple GUI calculator

	
	def __init__(self):
		# create window for the calculator
		win = GraphWin("Calculator")
		win.setCoords(0,0,6,7)
		win.setBackground("light blue")
		self.win = win
		# create widgets
		self.__createButtons()
		self.__createDisplay()

		
	def __createButtons(self):
		# create list of buttons
		# start with all standard sized buttons
		# buttonSpecs gives center coords and label of buttons
		buttonSpecs = [(2,1,'0'), (3,1,'.'),
						(1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
						(1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
						(1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')]
		self.buttons = []
		
		for (cx,cy,label) in buttonSpecs:
			self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))
		# create the larger = button
		self.buttons.append(Button(self.win, Point(4.5,1), 1.75, .75, "="))
		# activate all buttons
		for b in self.buttons:
			b.activate()
			
	
	def __createDisplay(self):
		bg = Rectangle(Point(.5,5.5), Point(5.5,6.5))
		bg.setFill('white')
		bg.draw(self.win)
		text = Text(Point(3,6), "")
		text.draw(self.win)
		text.setFace("courier")
		text.setStyle("bold")
		text.setSize(16)
		self.display = text

		
	def getButton(self):
		# wait for a button to be clicked, returns label of clicked button
		while True:
			p = self.win.getMouse()
			for b in self.buttons:
				if b.clicked(p):
					return b.getLabel()
	
	
	def processButton(self, key):
		# update calculator display for keypress
		text = self.display.getText()
		if key == 'C':
			self.display.setText("")
		elif key == '<-':
			# backspace, slice off last character
			self.display.setText(text[:-1])
		elif key == '=':
			# evaluate expression and diplay result
			# the try...except catches errors in formula
			# being evaluated
			try: 
				result = eval(text)
			except:
				result = 'ERROR'
			self.display.setText(str(result))
		else:
			# normal keypress, append to end of display
			self.display.setText(text+key)
			
	
	def run(self):
		# infinite 'event loop' to process button clicks
		while True:
			key = self.getButton()
			self.processButton(key)
			
			
if __name__ == '__main__':
	# create calculator object
	theCalc = Calculator()
	
	# call calculator's run method
	theCalc.run()
