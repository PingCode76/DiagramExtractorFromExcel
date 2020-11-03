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


#numberFunctiontoDraw = countDiagramNumber()
#nbDraw = 1

path="app/static/img/diagram1.svg"
encode_file(path , size=("2000px", "2000"))


