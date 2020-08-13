from tkinter import *

root = Tk()

appTitle = Label(text="Trappi")

statusText = StringVar()
statusText.set("Press a button to trigger a trap")

feedbackLabel = Label(textvariable=statusText)

def buttonClicked(switchNumber):
    statusText.set("I clicked the " + str(switchNumber))

## Setup Buttons
myButton1 = Button(root, text="Trap 1", command=lambda: buttonClicked(1))
myButton2 = Button(root, text="Trap 2", command=lambda: buttonClicked(2))
myButton3 = Button(root, text="Trap 3", command=lambda: buttonClicked(3))

exitButton = Button(root, text="Exit", command=root.quit)

## Add controls to GUI
appTitle.grid(row=0, column=1)
feedbackLabel.grid(row=1, column=0, columnspan=3, sticky=W+E)

myButton1.grid(row=2, column=0)
myButton2.grid(row=2, column=1)
myButton3.grid(row=2, column=2)

exitButton.grid(row=5, column=0)

root.mainloop()
