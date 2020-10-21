"""
program colorpicker.py
"""

from breezypythongui import EasyFrame
import tkinter.colorchooser

class ColorPicker(EasyFrame):
	def __init__(self):
		"""displays the results of picking a color."""
		EasyFrame.__init__(self, title = "Color Chooser Demo")

		# Labels and output fields
		self.addLabel(text = "R", row = 0, column = 0)
		self.addLabel(text = "G", row = 1, column = 0)
		self.addLabel(text = "B", row = 2, column = 0)
		self.addLabel(text = "Color", row = 3, column = 0)

		self.r = self.addIntegerField(value = 0, row = 0, column = 1)
		self.g = self.addIntegerField(value = 0, row = 1, column = 1)
		self.b = self.addIntegerField(value = 0, row = 2, column = 1)
		self.hex = self.addTextField(text = "#000000", row = 3, column = 1, width = 10)

		self.canvas = self.addCanvas(row = 0, column = 2, rowspan = 4, width = 50, background = "#000000")

		self.addButton(text = "Choose Color", row = 4, column = 0, columnspan = 3, command = self.chooseColor)

	def chooseColor(self):
		"""pops up a color chooser from the OS and outputs the result"""
		colorTuple = tkinter.colorchooser.askcolor()
		if not colorTuple[0]:
			return
		((r, g, b), hexString) = colorTuple
		self.r.setNumber(int(r))
		self.g.setNumber(int(g))
		self.b.setNumber(int(b))
		self.hex.setText(hexString)
		self.canvas["background"] = hexString

def main():
	"""instantiates and pops up the window"""
	ColorPicker().mainloop()

main()