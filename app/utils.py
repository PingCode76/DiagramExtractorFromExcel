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

def encode_file(filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    drawDiagram()
    drawing.save()


numberFunctiontoDraw = countDiagramNumber()
nbDraw = 0
print(str(numberFunctiontoDraw) + " fonction a encoer")
while nbDraw < numberFunctiontoDraw :
    print("Encodage numéro" + str(nbDraw))
    path="app/static/img/diagram" + str(nbDraw + 1) + ".svg"
    if os.path.exists(path):
        os.remove(path)
    encode_file(path , size=("2000px", "2000px"))
    nbDraw = nbDraw + 1


