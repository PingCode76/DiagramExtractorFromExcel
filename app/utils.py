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

def encode_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func()
    drawing.save()

def exportDraw():
    # path of diagram (svg) 
    path="app/static/img/diagram.svg"
    # If file doesn't exist 
    if os.path.exists(path):
            # Delete old app/static/img/diagram.svg
            os.remove(path) # specifying the path of the file for delete old diagram
    print("File deleted successfully")
    # encode drawDiagram from draw.py
    encode_file(drawDiagram, path , size=("2000px", "2000")) 
    
    #shutil.move('./' + os.path.abspath(os.path.dirname(__file__)) + '/diagram.svg', 'static/img/diagram.svg')
    #print('Draw exported in svg.')
exportDraw() #export when diagram is deleted

