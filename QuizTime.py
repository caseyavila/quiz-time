from tkinter import *
import tkinter.ttk as ttk
import json
import random

def WebBlock(URLblock):
    f = open("C:/Windows/System32/drivers/etc/hosts", "a")
    for URL in URLblock:
        f.write("127.0.0.1 {} \n".format(URL))
    f.close()

    f = open("C:/Windows/System32/drivers/etc/hosts", "r")
    print(f.read())


def WebUnBlock():
    with open("C:/Windows/System32/drivers/etc/hosts", "r") as f:
        lines = f.readlines()
    with open("C:/Windows/System32/drivers/etc/hosts", "w") as f:
        for line in lines:
            if line.startswith("127.0.0.1") == False:
                f.write(line)


def TimedUnblock(URLblock):
    from datetime import datetime, timedelta
    endtime = datetime.now() + timedelta(minutes=1)
    while datetime.now() < endtime:
        WebUnBlock()
    if datetime.now() >= endtime:
        WebBlock(URLblock)

def createaddTermWindow():
    addTermWindow = Toplevel()
    addTermWindow.geometry("500x165")
    addTermWindow.title("Add Term")
    addTermWindow.resizable(False, False)

    qLabel = Label(addTermWindow, text="Question:")
    qEntry = Entry(addTermWindow, width=80)
    aLabel = Label(addTermWindow, text="Answer:")
    aEntry = Entry(addTermWindow, width=80)
    btnSubmit = Button(addTermWindow, text="Submit")

    qLabel.grid(row=0, padx=5, pady=5)
    qEntry.grid(row=1, column=0, padx=5, pady=5)
    aLabel.grid(row=2, padx=5, pady=5)
    aEntry.grid(row=3, column=0, padx=5, pady=5)
    btnSubmit.grid(row=4, padx=5, pady=10)

def canvPrint(string):
    frmSets.create_text(175, 100, text=str(string))
    frmSets.update
    frmSets.create_window(175, 200, window = answer)
    frmSets.create_window(175, 250, window = answerBtn)

    
def studySet():
    global totalTerms
    global termList
    global correctCount
    answer.delete(0, 'end')
    correctCount = 0
    termList = setData["sets"][currentSet.get()]
    totalTerms = len(termList) - 1
    canvPrint(termList[totalTerms][0])
    totalTerms = totalTerms - 1
    
def submit():
    global totalTerms
    global correctCount
    if answer.get() == termList[totalTerms + 1][1]:
        frmSets.delete('all')
        frmSets.create_text(175, 300, text="Correct!")
        correctCount += 1
    else:
        frmSets.delete('all')
        frmSets.create_text(175, 300, text="Incorrect!")
    totalTerms = totalTerms - 1
    answer.delete(0, 'end')
    if correctCount == -1:
        frmSets.delete('all')
        frmSets.create_text(175, 300, text="Done with set! {} minutes earned!".format(correctCount))
    else:
        canvPrint(termList[totalTerms][0])
        

def addset():
    pass

setData = ""
with open("data.json") as f:
    for x in f.readlines():
        setData = setData+x

setData = json.loads(setData)

setList = []
for x in setData["sets"]:
    setList.append(x)

root = Tk()

currentSet = StringVar()
currentSet.set("Select Set")

root.geometry("610x425")
root.title("QuizTime")
root.resizable(False, False)

frmSets = Canvas(root, width=350, height=350, borderwidth=5, relief=RAISED, highlightthickness=0)
btnaddTermWindow = Button(root, text="Add Term", command=createaddTermWindow)
opmSets = OptionMenu(root, currentSet, *setList)
opmSets.config(activebackground='#DDDDDD')
studyBtn = Button(root, text="Study Set", height=3, width=20, command=studySet)
answer = Entry(frmSets, width=40)
answerBtn = Button(root, text="Submit", command=submit)
addsetBtn = Button(root, text="Add Set", command=addset)


opmSets.grid(row=0, column=1, columnspan=2)
btnaddTermWindow.grid(row=2, column=1)
frmSets.grid(row=0, column=0, rowspan=3, padx=30, pady=30)
studyBtn.grid(row=1, column=1, columnspan=2)
addsetBtn.grid(row=2, column=2)

root.mainloop()
