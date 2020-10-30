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

# Count a different word in Sequence for know the number of section to create
def countRectangleSection(data):
    differentWord = 0
    WordList = ''
    for line in data.values():
        WordList = WordList + line[2] + ' '
    for mot in WordList.split():
        if mot in WordList:
            differentWord = differentWord + 1
            WordList = WordList.replace(mot, '')
    return differentWord

#Count a number of label ( entry line in table )
def countlabel(data):
    LabelNumber = 0
    WordList = ''
    for line in data.values():
        WordList = WordList + line[2] + ' '
        LabelNumber = LabelNumber + 1
    return LabelNumber

# SELECT ONE LINE OF DATA 
# TODO: verify this function 
def selectLineinData(data, numberLine):
    i = 0 
    for line in data.values():
        i = i + 1
        if numberLine == i:
            print(line)
            return line

# More information for each RectangleSection    
# output : { rect1:[a,b], rect2:[c,d]}  
# TODO : use countRectangleSection(data)
def LabelInformation():
    information = {}
    i = 0 
    RectangleNumber = countRectangleSection(data)
    while i < RectangleNumber:
        # TODO: for loop .... ( search key line (a,b,c..) with correct rect ) ( use selectLineinData)
        information.update({ i:['a']})
        i = i + 1 
    print(information)

    return information
    

## TEST for module
selectLineinData(data, 3)
