from tkinter import *
from tkinter.ttk import *

self = Tk()
self.geometry('700x700')
self.title = 'Calculator'

strInput = StringVar()
global operation
operation = ''


def showTxtBtn(namBtn):
    global operation
    txtBtn = namBtn['text']
    operation += txtBtn
    strInput.set(operation)


def doIt():
    global operation
    sum = str(eval(operation))
    strInput.set(sum)
    operation = ''


def toThePowerOfNumber():
    global operation
    operation = operation + '**2'
    toPower = str(eval(operation))
    strInput.set(toPower)
    operation = ''

def delete():

    strInput.set('')

def divideOneToNum():
    global operation
    operation = str('1/'+ operation)
    strInput.set(str(eval(operation)))
    operation = ''

# -------------------------------------------------------------------------------------------------

style = Style()
style.configure('styBtnNumbers', font=('Arial', 10))

takeOperation = Label(self, font=('Arial', 15, 'bold'), state="disable", background='pink', width=47,
                      textvariable=strInput)
takeOperation.grid(columnspan=5, rowspan=2)

widtheBtnNum = 20
heightBtnNum = 10

styleBtn = Style()
styleBtn.configure('W.TButton', heigth=50)

# put numbers
numOne = Button(self, text='1', width=widtheBtnNum, command=lambda: showTxtBtn(numOne))
numOne.grid(column=1, row=8)
numTwo = Button(self, text='2', width=widtheBtnNum, command=lambda: showTxtBtn(numTwo))
numTwo.grid(column=2, row=8)
numThree = Button(self, text='3', width=widtheBtnNum, command=lambda: showTxtBtn(numThree))
numThree.grid(column=3, row=8)
numFour = Button(self, text='4', width=widtheBtnNum, command=lambda: showTxtBtn(numFour))
numFour.grid(column=1, row=7)
numFive = Button(self, text='5', width=widtheBtnNum, command=lambda: showTxtBtn(numFive))
numFive.grid(column=2, row=7)
numSix = Button(self, text='6', width=widtheBtnNum, command=lambda: showTxtBtn(numSix))
numSix.grid(column=3, row=7)
numSeven = Button(self, text='7', width=widtheBtnNum, command=lambda: showTxtBtn(numSeven))
numSeven.grid(column=1, row=6)
numEight = Button(self, text='8', width=widtheBtnNum, command=lambda: showTxtBtn(numEight))
numEight.grid(column=2, row=6)
numNine = Button(self, text='9', width=widtheBtnNum, command=lambda: showTxtBtn(numNine))
numNine.grid(column=3, row=6)
numBackSlash = Button(self, text='/', width=widtheBtnNum, command=lambda: showTxtBtn(numBackSlash))
numBackSlash.grid(column=3, row=9)
numZero = Button(self, text='0', width=widtheBtnNum, command=lambda: showTxtBtn(numZero))
numZero.grid(column=2, row=9)

# btn (delete)
btnDel = Button(self, text='Del', width=widtheBtnNum, command=lambda : delete())
btnDel.grid(column=4, row=4)

# btn (c)
btnC = Button(self, text='', width=widtheBtnNum)
btnC.grid(column=3, row=4)

# btn (ce)
btnCE = Button(self, text='', width=widtheBtnNum)
btnCE.grid(column=2, row=4)

# btn (percent)
btnPerecent = Button(self, text='%', width=widtheBtnNum, command=lambda: showTxtBtn(btnPerecent))
btnPerecent.grid(column=1, row=4, )

# btn (divide)
btnDivide = Button(self, text='', width=widtheBtnNum, command=lambda: showTxtBtn(btnDivide))
btnDivide.grid(column=4, row=5)

# btn (multiplication)
btnMulti = Button(self, text='*', width=widtheBtnNum, command=lambda: showTxtBtn(btnMulti))
btnMulti.grid(column=4, row=6)

# btn (minus)
btnMinus = Button(self, text='-', width=widtheBtnNum, command=lambda: showTxtBtn(btnMinus))
btnMinus.grid(column=4, row=7)

# btn (plus)
btnPlus = Button(self, text='+', width=widtheBtnNum, command=lambda: showTxtBtn(btnPlus))
btnPlus.grid(column=4, row=8)

# btn (Turn to minus or positive)
btnTurnMinusOrPositive = Button(self, text='-/+', width=widtheBtnNum)
btnTurnMinusOrPositive.grid(column=1, row=9)

# btn (DivideOnetoNumber)
btnDivideOnetoNumber = Button(self, text='1/n', width=widtheBtnNum, command=lambda: divideOneToNum())
btnDivideOnetoNumber.grid(column=1, row=5)

# btn (Logarithm of two)
btnLogarithmOfTwo = Button(self, text=' ', width=widtheBtnNum)
btnLogarithmOfTwo.grid(column=3, row=5)

# btn (PowerTwo)
btnPowerTwo = Button(self, text='n to the power of two', width=widtheBtnNum, command=toThePowerOfNumber)
btnPowerTwo.grid(column=2, row=5)

# btn (equal)
btnEqual = Button(self, text='=', width=widtheBtnNum, command=doIt)
btnEqual.grid(column=4, row=9)

# # make Button with loop
#
# operNumFirstClm = {'percent':'%', 'btnDivideOnetoNumber':'1/n', 'numSeven':'7',  'numFour':'4','numOne': '1', 'btnTurnMinusOrPositive':'-/+'}
# operNumSecondClm = {'btnCE':'CE', 'btnPowerTwo':'n to the power of two', 'numEight':'8',  'numFive': '5',  'numTwo': '2',  'numZero': '0'}
# operNumThirdClm = {'btnC':'C', 'btnTheRootN':'the root n', 'numSeven':'7', 'numFour':'4', 'numOne':'1', '-/+'}
# operNumFourdtClm = {'Del', 'divide', '*', '-', '+', '='}
#
# for oper in operNumFirstClm:

self.mainloop()
# ------------------------------------------
