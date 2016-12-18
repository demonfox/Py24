from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.numberRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        self.inputVar1 = StringVar()
        self.inputVar2 = StringVar()
        self.inputVar3 = StringVar()
        self.inputVar4 = StringVar()
        self.createWidgets()


    def createWidgets(self):
        self.master.title("24")
        self.pack(fill=BOTH, expand=True)

        firstFrame = Frame(self)
        firstFrame.pack(fill=X, expand=True)

        self.generateRandomProblemButton = Button(firstFrame, text='Random Problem', command=self.generateRandomProblem)
        self.generateRandomProblemButton.pack(padx=5, pady=4, side=LEFT)

        secondFrame = Frame(self)
        secondFrame.pack(fill=X, expand=True)

        self.inputVar1.set('1')
        self.inputVar2.set('1')
        self.inputVar3.set('1')
        self.inputVar4.set('1')

        self.option1 = OptionMenu(secondFrame, self.inputVar1, *self.numberRange)
        self.option1.pack(padx=2, side=LEFT)
        self.option2 = OptionMenu(secondFrame, self.inputVar2, *self.numberRange)
        self.option2.pack(padx=2, side=LEFT)
        self.option3 = OptionMenu(secondFrame, self.inputVar3, *self.numberRange)
        self.option3.pack(padx=2, side=LEFT)
        self.option4 = OptionMenu(secondFrame, self.inputVar4, *self.numberRange)
        self.option4.pack(padx=2, side=LEFT)

        thirdFrame = Frame(self)
        thirdFrame.pack(fill=X, expand=True)

        self.computeButton = Button(thirdFrame, text='Compute', command=self.compute)
        self.computeButton.pack(padx=5, pady=5, side=LEFT)

        self.clearButton = Button(thirdFrame, text='Clear', command=self.clear)
        self.clearButton.pack(padx=5, pady=5, side=RIGHT)

        fourthFrame = Frame(self)
        fourthFrame.pack(fill=X, expand=True)

        self.scrollBar = Scrollbar(fourthFrame)
        self.scrollBar.pack(side=RIGHT, fill=Y)
        self.listBox = Listbox(fourthFrame, width=40, yscrollcommand = self.scrollBar.set, exportselection=False, selectmode='single')
        #self.listBox.bind('<<ListboxSelect>>', self.onGFWListItemSelect)
        self.listBox.pack(padx=5, pady=5, side=LEFT, fill=BOTH, expand=True)
        self.scrollBar.config(command = self.listBox.yview)

        fifthFrame = Frame(self)
        fifthFrame.pack(fill=X, expand=True)
        self.getCheatSheetButton = Button(fifthFrame, text='Get Your Cheat Sheet', command=self.getCheatSheet)
        self.getCheatSheetButton.pack(padx=5, pady=5, side=LEFT)
        self.dumpButton = Button(fifthFrame, text='Dump', command=self.dumpCheatSheet)
        self.dumpButton.pack(padx=5, pady=5, side=RIGHT)

    def generateRandomProblem(self):
        input1 = int(self.inputVar1.get())
        input2 = int(self.inputVar2.get())
        input3 = int(self.inputVar3.get())
        input4 = int(self.inputVar4.get())
        messagebox.showinfo('Adding a new site', '%d, %d, %d, %d' % (input1, input2, input3, input4))
        return

    def compute(self):
        return

    def clear(self):
        return

    def getCheatSheet(self):
        return

    def dumpCheatSheet(self):
        return

app = Application()
app.mainloop()
