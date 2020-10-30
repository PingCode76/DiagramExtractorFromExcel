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

def drawDiagram():
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
    print('drawing diagram...')

    #write("mon_texte",False,align='Left',font=('Arial',16,'normal')).

    # draw here
    turtle.color('black')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90) 
    turtle.circle(120)

    #turtle.bye()

def encode_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    drawing.add(drawing.rect(fill='white', size=("100%", "100%")))

    drawing.add(drawing.line((440, 280), (1180, 280), stroke='#0f0', stroke_width=7))
    #drawing.__init__(filename=u'static/noname.svg')
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func()
    drawing.save()

    # The SVG file have a form, but this form is not displaying in webpage


def exportDraw():
    encode_file(drawDiagram, 'app/static/img/diagram.svg', size=("500px", "500px"))
    #shutil.move('./' + os.path.abspath(os.path.dirname(__file__)) + '/diagram.svg', 'static/img/diagram.svg')
    print('Draw exported in svg.')

exportDraw()

