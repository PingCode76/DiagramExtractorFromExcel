import random
import os.path
import os
import shutil
import xlrd
import turtle
from turtle import *
#from Tkinter import *

from random import randint

import svgwrite
from .SvgTurtle import SvgTurtle
from .diagram import *
from .draw import *

def encode_file(filename, nbDraw, size):
    drawing = svgwrite.Drawing(filename, size=size)
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    drawDiagram(nbDraw)
    drawing.save()

def change_id_function(id_function):
    dataCurrent = formatData(id_function)
    return dataCurrent


def MainDraw():
    numberFunctiontoDraw = countDiagramNumber()
    nbDraw = 0
    print(str(numberFunctiontoDraw) + " fonction a encoer")
    while nbDraw < numberFunctiontoDraw :
        nbDraw = nbDraw + 1
        #change_id_function(nbDraw)
        print("Encodage numéro " + str(nbDraw))
        path="app/static/img/diagram" + str(nbDraw) + ".svg"
        if os.path.exists(path):
            os.remove(path)
        encode_file(path , nbDraw, size=("2000px", "2000px"))
        print('exécution de mainDraw avec encodage ' + str(nbDraw))
        
MainDraw()


