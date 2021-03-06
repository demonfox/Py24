from tkinter import *
import configparser
import threading
import random
import tkinter.messagebox as messagebox

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        #self.numberRange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.inputStart = int(self.config['General']['InputRangeStart'])
        self.inputEnd = int(self.config['General']['InputRangeEnd'])

        self.inputIntList = range(self.inputStart, self.inputEnd+1)
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

        self.inputVar1.set(self.inputStart)
        self.inputVar2.set(self.inputStart)
        self.inputVar3.set(self.inputStart)
        self.inputVar4.set(self.inputStart)

        self.option1 = OptionMenu(secondFrame, self.inputVar1, *self.inputIntList)
        self.option1.pack(padx=2, side=LEFT)
        self.option2 = OptionMenu(secondFrame, self.inputVar2, *self.inputIntList)
        self.option2.pack(padx=2, side=LEFT)
        self.option3 = OptionMenu(secondFrame, self.inputVar3, *self.inputIntList)
        self.option3.pack(padx=2, side=LEFT)
        self.option4 = OptionMenu(secondFrame, self.inputVar4, *self.inputIntList)
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
        random.seed()
        input1 = str(random.randint(self.inputStart, self.inputEnd))
        input2 = str(random.randint(self.inputStart, self.inputEnd))
        input3 = str(random.randint(self.inputStart, self.inputEnd))
        input4 = str(random.randint(self.inputStart, self.inputEnd))
        self.inputVar1.set(input1)
        self.inputVar2.set(input2)
        self.inputVar3.set(input3)
        self.inputVar4.set(input4)
        return

    def compute(self):
        input1 = int(self.inputVar1.get())
        input2 = int(self.inputVar2.get())
        input3 = int(self.inputVar3.get())
        input4 = int(self.inputVar4.get())
        inputs = ((input1, str(input1)), (input2, str(input2)), (input3, str(input3)), (input4, str(input4)))
        self.solution = ''
        if (self.calculate(inputs)):
            self.listBox.insert(END, '%d, %d, %d, %d - %s' % (inputs[0][0], inputs[1][0], inputs[2][0], inputs[3][0], self.solution))
        else:
            self.listBox.insert(END, '%d, %d, %d, %d - %s' % (inputs[0][0], inputs[1][0], inputs[2][0], inputs[3][0], 'No solution'))
        return

    def calculate(self, inputs):
        #messagebox.showinfo('Adding a new site', '%d, %d, %d, %d' % (inputs[0], inputs[1], inputs[2], inputs[3]))
        if (len(inputs) == 1):
            if (self.isclose(24.0, inputs[0][0])):
                self.solution = inputs[0][1]
                return True
        else:
            combinations = self.generateCombination(inputs)
            # print(combinations)
            for i in combinations:
                if (self.calculate(i)):
                    return True
        return

    # there is a math.isclose() in Python 3.5, may switch to that once I upgrade
    def isclose(self, a, b, eps=0.0001):
        # print('%d' % b)
        return abs(a - b) <= eps

    def generateCombination(self, inputs):
        result = []
        for i in range(len(inputs) - 1):
            for j in range(i+1, len(inputs)):
                # print('%d %d' % (i, j))
                operand1 = inputs[i]
                operand2 = inputs[j]
                combination = []
                for k in range(len(inputs)):
                    if (k != i) and (k != j):
                        combination.append(inputs[k])
                
                combination.append(((operand1[0] + operand2[0]), '(' + operand1[1] + '+' + operand2[1] + ')'))
                result.append(list(combination))
                del combination[-1]
                
                combination.append(((operand1[0] - operand2[0]), '(' + operand1[1] + '-' + operand2[1] + ')'))
                result.append(list(combination))
                del combination[-1]
                

                combination.append(((operand2[0] - operand1[0]), '(' + operand2[1] + '-' + operand1[1] + ')'))
                result.append(list(combination))
                del combination[-1]
                
                combination.append(((operand1[0] * operand2[0]), '(' + operand1[1] + '*' + operand2[1] + ')'))
                result.append(list(combination))
                del combination[-1]
                
                if (operand2[0] != 0):
                    combination.append(((operand1[0] / operand2[0]), '(' + operand1[1] + '/' + operand2[1] + ')'))
                    result.append(list(combination))
                    del combination[-1]
                
                if (operand1[0] != 0):
                    combination.append(((operand2[0] / operand1[0]), '(' + operand2[1] + '/' + operand1[1] + ')'))
                    result.append(list(combination))
                    del combination[-1]

        return result

    def clear(self):
        self.listBox.delete(0, END)
        return

    def getCheatSheet(self):
        t = threading.Thread(target=self.calculateAll)
        t.daemon = True
        t.start()
        return

    def calculateAll(self):
        for i in range(self.inputStart, self.inputEnd+1):
            for j in range(self.inputStart, self.inputEnd+1):
                for k in range(self.inputStart, self.inputEnd+1):
                    for l in range(self.inputStart, self.inputEnd+1):
                        self.inputVar1.set(i)
                        self.inputVar2.set(j)
                        self.inputVar3.set(k)
                        self.inputVar4.set(l)
                        self.compute()
        return

    def dumpCheatSheet(self):
        with open('solution.txt', 'w') as f:
            for index in range(self.listBox.size()):
                f.write(self.listBox.get(index))
                f.write('\n')
        return

app = Application()
app.mainloop()
