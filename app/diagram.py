import random
import os.path
import os
import shutil
import xlrd
import turtle
from turtle import *
#from Tkinter import *

from random import randint

data = {
        # line : id_function, Sequence, Operation Type, Description, Node1, Node2 
        "a":["1","1","Col","Lorem ipsum dolor sit amet, consectetur adipiscing elit","AX23","BY12"], 
        "b":["1","2","Tra","Donec fringilla, erat non suscipit faucibus, léo mi porta enim","BY12","CF43"],
        "c":["1","3","Tra","Proin quis tortor pharetra, pulvinar sem viate, lobortis","BY12","CG54"],
        "d":["1","4","Fer","Nulla vel mollis sem. Quisque consectetur maximus ornare.","CG54","TR89"],
        "e":["1","5","Fer","Aliquam erat volutpar. Curabitur et magna","CF43","DS09"],
        "f":["2","1","Col","Cras Suscipit hendrerit feugiat Viva porta sed consecta","AB56","KJ65"],
        "g":["2","2","Tra","Ipsum proin quis tortora maxima Aenean lobortis","KJ65","HF32"],
        "h":["2","3","Fer","Laculis euis mod In hac habitasse platea dictumus. Etiam dictum","HF32","ZX12"],
    }

# Count a all name and number of sequence type #OUTPUT : '
def countRectangleSection(data):
    WordList = ''
    RectangleName = []
    for line in data.values():
        WordList = WordList + line[1] + ' ' #1 Select a Sequence type
    for mot in WordList.split():
        if mot in WordList:
            WordList = WordList.replace(mot, '')
            RectangleName.append(mot)
    return RectangleName

#Count a number of label ( entry line in table )
def countlabel(data):
    LabelNumber = 0
    WordList = ''
    for line in data.values():
        WordList = WordList + line[2] + ' '
        LabelNumber = LabelNumber + 1
    return LabelNumber

# SELECT ONE LINE OF DATA  
def selectLineinData(data, numberLine):
    i = 0 
    for line in data.values():
        i = i + 1
        if numberLine == i:
            return line

# find which label belongs to which rectangle    
# output : { rect1:[label1 ,label2], rect2:[label3,label4]}  
def LabelInformation():
    information = {}
    RectangleNumber = countRectangleSection(data) #Rectange number
    for rect in RectangleNumber:
        entry = [] 
        i = 0
        for line in data.values():
            i = i + 1
            if rect == line[1]:
                entry.append(i)
        information.update({ rect : entry })

    print(information)

    return information
    

## TEST for module
#selectLineinData(data, 3)
LabelInformation()
