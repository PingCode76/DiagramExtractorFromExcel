from .diagram import * 

def drawingRectangle(x = -1000):
    #print(nbRectangleInDiagram) # 3 

    for rectangle in LabelInformation():
        turtle.color('green')
        turtle.up()
        turtle.goto(x, 400)
        turtle.down()

        #turtle.fillcolor('grey') # background color 
        #turtle.begin_fill() # begin color 

        turtle.forward(300) #Forward turtle by 150 units ( width )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(600) #Forward turtle by 80 units ( height )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(300) #Forward turtle by 150 units ( width )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(600) #Forward turtle by 80 units ( height )
        turtle.left(90) #Turn turtle by 90 degree

        #turtle.end_fill() # end color  
        x = x + 400

def drawingLabel(x,y, txtLabel, colorLabel):  #y = 800 at starting
    #print(x)
    #print(y)
    #x = -900#x -900
    turtle.color('green') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()
    turtle.fillcolor('white') # background color 
    turtle.begin_fill() # begin color 

    turtle.forward(150) #Forward turtle by 150 units ( width )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(100) #Forward turtle by 80 units ( height )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(150) #Forward turtle by 150 units ( width )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(100) #Forward turtle by 80 units ( height )
    turtle.left(90) #Turn turtle by 90 degree

    turtle.end_fill() # end color 
    turtle.up()
   
    #x = -900#x
    y = y + 25 #y # 800 

    #node left
    turtle.goto(x,y)
    turtle.down()
    turtle.color('blue') # color 
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(25) #50 good 
    turtle.end_fill() 
    turtle.up()

    #node right 
    turtle.goto(x+150,y) # n + width + rayon 
    turtle.down()
    turtle.color('blue')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(25) #50 good 
    turtle.end_fill() 
    turtle.up()
    
    # Rectangle Write
    x = x + 40 #x -900 + 60 = -840

    turtle.color('black') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()

    turtle.write(txtLabel)
    turtle.up()

    # color # depend data 
    x = x - 10  #x 840 -> 860
    y = y + 45 #y #825

    turtle.color('black') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()
    turtle.fillcolor(colorLabel) # background color 
    turtle.begin_fill() # begin color 
    turtle.forward(70) #Forward turtle by 150 units ( width )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(10) #Forward turtle by 80 units ( height )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(70) #Forward turtle by 150 units ( width )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(10) #Forward turtle by 80 units ( height )
    turtle.left(90) #Turn turtle by 90 degree

    turtle.end_fill() # end color 
    turtle.up()

    # Rectangle Write
    #x = -860 #x
    y = y - 50 #y 

    turtle.color('black') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()
    turtle.forward(70) #Forward turtle by 150 units ( width )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(30) #Forward turtle by 80 units ( height )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(70) #Forward turtle by 150 units ( width )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.forward(30) #Forward turtle by 80 units ( height )
    turtle.left(90) #Turn turtle by 90 degree
    turtle.up()



def drawDiagram():

    labelGroup = LabelInformation()

    xDraw = -1320   # -900 normal
    for i in labelGroup:
        #print(labelGroup[i])
        # for each rectangle
        drawingRectangle()
        # change pos draw
        xDraw = xDraw + 400

        # count how label
        y = 700 
        nbLabel = len(labelGroup[i])
        for i in labelGroup[i]:

            # get txt and node of label
            line = selectLineinData(i) 
            print(line)
            txtLabel = line[3] # get txt in DataLine - inject to drawingLabel
            print(txtLabel)

            # get color of label
            color = checkdifferentsColor()
            colorLabel = color[i] # get color - inject to drawingLabel
            print(color[i])
            
            #print('un label de dessinner')
            drawingLabel(xDraw, y , txtLabel , colorLabel )  #inject here
            y = y + 150 
            #print(i)