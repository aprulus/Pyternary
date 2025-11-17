import time
from pynput.keyboard import Controller, Key

#ngl I did this just because I prefer it being called Keyboard
keyboard=Controller()

#Change these to customize how the grammar of your code would work,
#along with what specific things you want it to press.
currentFile="Pyternary/PyternaryCodes/TestZero.txt"
splitterDelimiter=','
commentDelimiter=':'
varFunctSetter="#"
unknownNewPlace="%"
jumpButton="d"
leftButton=Key.left
rightButton=Key.right
clickingSpeed=0.04

#Variables that you shouldn't need to change
varDict={}
everyLines=[]
trueFunctionsList=["none","in","out","load","set","addn","subn","multn","divn","uload",
                   "uset","add","sub","mult","div","jump","jumpz","jumpnz","jumpof",
                   "jumpuf","comp","push","pop","call","return","swap","halt"]
trueFunctions={"none":0,"in":1,"out":2,"load":3,"set":4,"addn":5,"subn":6,"multn":7,"divn":8,"uload":9,
               "uset":10,"add":11,"sub":12,"mult":13,"div":14,"jump":15,"jumpz":16,"jumpnz":17,"jumpof":18,
               "jumpuf":19,"comp":20,"push":21,"pop":22,"call":23,"return":24,"swap":25,"halt" :26}

#Converts a number to the deternary format, for easy integration when necessary
def convertToDeternary(num):
    higherOne=num//27
    lowerOne=num%27
    returner=str(higherOne)+","+str(lowerOne)
    return returner

#These Press the Required buttons to accomplish the macro
def jumpPress(amount):
    for i in range(amount):
        keyboard.press(jumpButton)
        time.sleep(clickingSpeed)
        keyboard.release(jumpButton)
        time.sleep(clickingSpeed)

def leftPress(amount):
    for i in range(amount):
        keyboard.press(leftButton)
        time.sleep(clickingSpeed)
        keyboard.release(leftButton)
        time.sleep(clickingSpeed)

def rightPress(amount):
    for i in range(amount):
        keyboard.press(rightButton)
        time.sleep(clickingSpeed)
        keyboard.release(rightButton)
        time.sleep(clickingSpeed)

#Main Function that runs the Macro
def main():
    #Reads the file and will store each line in a list to be read
    with open(currentFile,'r') as File:
        for i, line in enumerate(File, start=0):
            line=line.replace(' ','').replace('\n','').replace('\r','')
            if commentDelimiter in line:
                line=line[0:line.index(commentDelimiter)]
            line=line.split(splitterDelimiter)
            if line[0][0]==varFunctSetter:
                varDict[line[0]]=i
                print(line[0],"set to line",i)
                line=line[1:]
                everyLines.append(line)
            else:
                everyLines.append(line)
    time.sleep(4)
    rightPress(1)
    counter=0
    for line in everyLines:
        #Input the Command Selector
        jumpAmount=0
        if line[0].isnumeric():
            jumpamount=int(line[0])
            jumpPress(jumpamount)
        elif line[0] in trueFunctions:
            jumpamount=trueFunctions[line[0]]
            jumpPress(jumpamount)
        else:
            print("Unknown Command:",line[0])
        #Move to the Upper Data Selector
        rightPress(1)
        if len(line)<3:
            if line[1].isnumeric():
                jumpAmounts=int(line[1])
            elif line[1] in varDict:
                jumpAmounts=varDict[line[1]]
            elif "%"in line[1]:
                nextFree=len(everyLines)+int(line[1][1:])
                jumpAmounts=nextFree
            else:
                print("Unknown Data:",line[1])
                jumpAmounts=0
            jumpAmount=convertToDeternary(jumpAmounts)
        elif len(line)==3:
            if line[1].isnumeric():
                upperData=int(line[1])
            else:
                print("Unknown Upper Data:",line[1])
                upperData=0
            if line[2].isnumeric():
                lowerData=int(line[2])
            else:
                print("Unknown Lower Data:",line[2])
                lowerData=0
            jumpAmount=str(upperData)+","+str(lowerData)
        else:
            print("Too many data inputs:",line)
            jumpAmount="0,0"
        #Input the Data Values
        jumpAmount=jumpAmount.split(',')
        jumpPress(int(jumpAmount[0]))
        rightPress(1)
        jumpPress(int(jumpAmount[1]))
        #Go Back To The Line Selector
        leftPress(3)
        #Move on to the next line
        jumpPress(1)
        #Go to the Command Selector
        rightPress(1)
        print(counter,trueFunctionsList[jumpamount].upper(),"(",jumpAmount,")")
        counter+=1
    print("Finished")
main()