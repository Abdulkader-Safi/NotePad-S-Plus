import tkinter
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

class Notepad_S_Plus:

	notepad = Tk()

	# window width and hight
	winWidth = 300
	winHeight = 300

	textArea = Text(notepad)
	
	menuBar = Menu(notepad)
	fileMenu = Menu(menuBar, tearoff=0)
	editMenu = Menu(menuBar, tearoff=0)
	helpMenu = Menu(menuBar, tearoff=0)

	scrollbar = Scrollbar(textArea)
	fileOpen = None

	def __init__(self, **kwargs):
		# Title
		self.notepad.title('Untitled - NotePad S-Plus')
		
		# Set icon 
		try: 
				self.notepad.wm_iconbitmap("NotePad S-Plus.ico") 
		except: 
				pass
		
		#set windows size default 300x300
		try:
			self.winWidth = kwargs['width']
		except KeyError:
			pass
		try:
			self.winHeight = kwargs['height']
		except KeyError:
			pass

		# Create a Notepad windows and set size
		self.notepad.geometry('%dx%d' % (self.winWidth, self.winHeight)) 

		# To make the textarea auto resizable 
		self.notepad.grid_rowconfigure(0, weight=1)
		self.notepad.grid_columnconfigure(0, weight=1)

		# place textArea
		self.textArea.grid(sticky=N+E+S+W)

		# Add open new file
		self.fileMenu.add_command(label='New', command=self.newFile)
		# To open a already existing file 
		self.fileMenu.add_command(label="Open", command=self.openFile)
		# Add save current file
		self.fileMenu.add_command(label='Save', command=self.saveFile)
		# To create a line in the dialog		 
		self.fileMenu.add_separator()										 
		self.fileMenu.add_command(label="Exit", command=self.quitApplication) 
		
		self.menuBar.add_cascade(label="File", menu=self.fileMenu)

		# To give a feature of cut 
		self.editMenu.add_command(label="Cut", command=self.cut)
		# to give a feature of copy	 
		self.editMenu.add_command(label="Copy", command=self.copy)
		# To give a feature of paste 
		self.editMenu.add_command(label="Paste", command=self.paste)
		
		self.menuBar.add_cascade(label="Edit", menu=self.editMenu)

		# To create a feature of description of the notepad 
		self.helpMenu.add_command(label="About", command=self.showAbout)

		self.menuBar.add_cascade(label="Help", menu=self.helpMenu) 

		self.notepad.config(menu=self.menuBar)

		# Scrollbar will adjust automatically according to the content
		self.scrollbar.pack(side=RIGHT, fill=Y)		 
		self.scrollbar.config(command=self.textArea.yview)	 
		self.textArea.config(yscrollcommand=self.scrollbar.set)





	# Add newFile function
	def newFile(self):
		self.notepad.title("Untitled - NotePad S-Plus") 
		self.fileOpen = None
		self.textArea.delete(1.0,END)
	
	# Add openFile function
	def openFile(self):
		self.fileOpen = askopenfilename(defaultextension=".txt",
										filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt"),
										("python","*.py")])
		if self.fileOpen == "":
			# if no file selected to open
			self.fileOpen = None
		else:
			# set the window title
			self.notepad.title(os.path.basename(self.fileOpen) + " - NotePad S-Plus") 
			# open the file

			file = open(self.fileOpen, 'r')
			self.textArea.insert(1.0, file.read())
			file.close()



	# Add savefile function
	def saveFile(self):
		if self.fileOpen == None:
			# Save as new file
			self.fileOpen = asksaveasfilename(defaultextension=".txt",
										filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt"),
										("python","*.py")])
			if self.fileOpen == "":
				# if no file selected to open
				self.fileOpen = None
			else:
				# svae the file
				file = open(self.fileOpen, 'w')
				file.write(self.textArea.get(1.0,END))
				file.close()

				# Change the window title 
				self.notepad.title(os.path.basename(self.fileOpen) + " - NotePad S-Plus")

		else:
			file = open(self.fileOpen, 'w')
			file.write(self.textArea.get(1.0,END))
			file.close()

	# Add quit function
	def quitApplication(self):
		self.notepad.destroy()

	# Add cut function
	def cut(self):
		self.textArea.event_generate('<<Cut>>')
	
	# Add cut function
	def copy(self): 
		self.textArea.event_generate("<<Copy>>") 

	# Add cut function
	def paste(self): 
		self.textArea.event_generate("<<Paste>>") 
	

	# Add showAbout function
	def showAbout(self):
		showinfo("NotePad S-Plus","Notepad mini project built by Abdulkader Safi")

	# Run main application
	def run(self): 
		self.notepad.mainloop()


# Run main application 
notepad = Notepad_S_Plus(width=800, height=500)
notepad.run()