import random
import os.path
import os
import shutil
import xlrd
import turtle
import string
from turtle import *
from collections import Counter
from random import randint
from .utils import *
from math import *
#import utils

def getData():
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
        "i":["3","1","Col","Laculis euis mod In hac habitasse platea dictumus. Etiam dictum","H123","KJ65"], # add
        "j":["3","1","Col","Laculis euis mod In hac habitasse platea dictumus. Etiam dictum","SE44","KJ65"],
        "k":["3","1","Tra","Laculis euis mod In hac habitasse platea dictumus. Etiam dictum","KJ65","SE45"],
        "l":["3","1","Fer","Laculis euis mod In hac habitasse platea dictumus. Etiam dictum","SE45","ERT4"],
        "m":["4","1","Col","hey lorem ipsum lorem in dolor","RG45","TRA2"],
        "n":["4","1","Tra","hey lorem ipsum lorem in dolor","TRA2","ERT4"],
        "o":["1","6","Col","Test Croisement Noeud","EEEE","AAAA"],
        }
    return data

# return data with a current function
def formatData(nbFunction):
    i = 0
    data = getData()
    letter = []
    z = 0
    rows = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # if there is not enough letter, add numbers in front of letters according to the length of the data 
    minLetter = 26
    maxLetter = 51
    sliceVar = len(getData())/26

    # for the 26 letter slices of the alphabet, add the number behind the letter, according to the data
    while z < len(getData()): 
        if z < minLetter:
            letter.append(rows[z])
        elif z > minLetter + 1 & z < maxLetter :
            try:
                letter.append(rows[z - minLetter + 28] + str(z))
            except:
                pass

        z = z + 1

    tableToDelete = []
    for line in data.values():
        if line[0] != str(nbFunction):
            tableToDelete.append(i)
        i = i + 1
    for nb in tableToDelete:
        del data[letter[nb]]
    return data

def countDiagramNumber():
    listData = []
    outputList = []
    data = getData()
    for line in data.values():
        listData.append(line[0])
    for element in listData:
        if element not in outputList:
            outputList.append(element)
    return len(outputList)

# Count a all name and number of sequence type #OUTPUT : '
def countRectangleSection(nbDraw):
    WordList = ''
    RectangleName = []
    dataCurrent = formatData(nbDraw)
    for line in dataCurrent.values():
        WordList = WordList + line[2] + ' ' #1 Select a Sequence type
    for mot in WordList.split():
        if mot in WordList:
            WordList = WordList.replace(mot, '')
            RectangleName.append(mot)
    return RectangleName

#Count a number of label ( entry line in table )
def countlabel(nbDraw):
    LabelNumber = 0
    WordList = ''
    dataCurrent = formatData(nbDraw)
    for line in dataCurrent.values():
        WordList = WordList + line[2] + ' '
        LabelNumber = LabelNumber + 1
    return LabelNumber

# SELECT ONE LINE OF DATA  
def selectLineinData(numberLine, nbDraw):
    i = 0
    dataCurrent = formatData(nbDraw)
    for line in dataCurrent.values():
        i = i + 1
        if numberLine == i:
            return line


# find which label belongs to which rectangle    
# output : { col:[label1 ,label2], tra:[label3,label4]}  
def LabelInformation(nbDraw):
    dataCurrent = formatData(nbDraw)
    information = {}
    RectangleNumber = countRectangleSection(nbDraw)

    nodes = nodeInformation(nbDraw)
    print(nodes) 

    for rect in RectangleNumber:
        entry = [] 
        i = 0
        for line in dataCurrent.values():
            # i = number of label
            i = i + 1
            # if the input line belongs to the rectangle
            if rect == line[2]: 
                entry.append(i)

            #check if the label is correctly placed ( see nodes )
            # m to browse the nodes
            m = 1
            while m < len(nodes):
                
                if i == nodes[m][0] or i == nodes[m][1]:
                    if i == nodes[m + 1][0] or i == nodes[m + 1][1]:
                        # inverse a labels
                        print('label' + str(i) + 'match echange')
                        if len(entry) > 1:
                            entry[0],entry[1] = entry[1],entry[0]
                m = m + 1
        information.update({ rect : entry })
    print(information)
    return information
    
# intern function, do not use in draw.py
def createTableColor(nbDraw):
    i = 0   
    table = []
    dataCurrent = formatData(nbDraw)
    for line in dataCurrent.values():
        i = i + 1 
        # add element in table if not exist
        if line[2] not in table:
            table.append(line[2])
    return table

# output : 1 : red, 2: yellow
def checkdifferentsColor(nbDraw):
    information = {}
    ColorsDifferent = ['green', 'yellow','orange', 'red', 'blue','purple','marron', 'grey', 'black', 'white']
    i = 0   
    table = createTableColor(nbDraw)

    # attribute colors
    dataCurrent = formatData(nbDraw)
    for line in dataCurrent.values():
        i = i + 1
        nbColor = len(table)
        z = 0 
        while z < nbColor:
            if table[z]:
                if line[2] == table[z]:
                    information.update({i: ColorsDifferent[z]})
            z = z + 1
    return information

#output : {node1: [label1, label5], node2:... }
def nodeInformation(nbDraw):
    nodes = {}
    i = 0
    numéroNoeudTable = 0 
    table1 = {}
    table2 = {}
    dataCurrent = formatData(nbDraw)
    for line in dataCurrent.values():
        i = i + 1 
        table1.update({i :line[4]})
        table2.update({i :line[5]})
    for key, value in table1.items():
        for key2, value2 in table2.items():
            if value2 == value:
                numéroNoeudTable = numéroNoeudTable + 1
                nodes.update({numéroNoeudTable : [ key , key2 ]})
    return nodes

