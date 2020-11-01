from .diagram import * 

def drawingRectangle(x = -1000):
   
    for rectangle in LabelInformation():
        turtle.color('green')
        turtle.up()
        turtle.goto(x, 400)
        turtle.down()

        #turtle.fillcolor('grey') # background color 
        #turtle.begin_fill() # begin color 

        turtle.forward(350) # ( width )
        turtle.left(90) # 90 degree
        turtle.forward(600) # ( height )
        turtle.left(90) # 90 degree
        turtle.forward(350) # ( width )
        turtle.left(90) # 90 degree
        turtle.forward(600) # ( height )
        turtle.left(90) # 90 degree

        #turtle.end_fill() # end color  
        x = x + 400


def drawingLabel(x,y, txtLabel, colorLabel, txtNode1, txtNode2):  #y = 800 at starting

    #print(x)
    #print(y)

    ## LABEL 

    turtle.color('green') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()
    turtle.fillcolor('white') # background color 
    turtle.begin_fill() # begin color 

    turtle.forward(250) # ( width )
    turtle.left(90) # 90 degree
    turtle.forward(150) # ( height )
    turtle.left(90) # 90 degree
    turtle.forward(250) # ( width )
    turtle.left(90) # 90 degree
    turtle.forward(150) # ( height )
    turtle.left(90) # 90 degree

    turtle.end_fill() # end color 
    turtle.up()
   
    y = y + 45 
    ## NODE
    # NODE LEFT
    turtle.goto(x,y)
    turtle.down()
    turtle.color('blue') # color 
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(25)  
    turtle.end_fill() 

    turtle.goto(x-15,y+17) #go to for write
    turtle.color('white') # color txt
    turtle.write(txtNode1)

    turtle.up()

    # NODE RIGHT
    turtle.goto(x+250,y) # x + width + rayon 
    turtle.down()
    turtle.color('blue')
    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.circle(25) 
    turtle.end_fill() 

    turtle.up()
    turtle.goto(x+235,y+13) #go to for write # test
    turtle.down()
    turtle.color('white') # color txt
    turtle.write(txtNode2)

    turtle.up()
    
    ## WRITE IN "RECTANGLE FOR WRITE"
    x = x + 40 

    turtle.color('black') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()

    turtle.write(txtLabel)
    turtle.up()

    ## COLOR
    x = x - 10  #x 840 -> 860
    y = y + 45 #y #825

    turtle.color('black') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()
    turtle.fillcolor(colorLabel) # background color 
    turtle.begin_fill() # begin color 
    turtle.forward(180) # ( width )
    turtle.left(90) # 90 degree
    turtle.forward(10) # ( height )
    turtle.left(90) # 90 degree
    turtle.forward(180) # ( width )
    turtle.left(90) # 90 degree
    turtle.forward(10) # ( height )
    turtle.left(90) # 90 degree

    turtle.end_fill() # end color 
    turtle.up()

    ##  RECTANGLE FOR WRITE
    y = y - 60 

    turtle.color('black') #color 
    turtle.up()
    turtle.goto(x,y) # pos
    turtle.down()
    turtle.forward(180) # ( width )
    turtle.left(90) # 90 degree
    turtle.forward(50) # ( height )
    turtle.left(90) # 90 degree
    turtle.forward(180) # ( width )
    turtle.left(90) # 90 degree
    turtle.forward(50) # ( height )
    turtle.left(90) # 90 degree
    turtle.up()

def drawingNode():
    nodes = nodeInformation()

    # Import nodes
    # for each nodes
    # Find entry and position
    # Drawing node
    return


def drawDiagram():

    labelGroup = LabelInformation()

    xDraw = -1350
    for i in labelGroup:
        #print(labelGroup[i])
        
        # for each rectangle
        drawingRectangle()
        # change pos draw
        xDraw = xDraw + 400
        # count how label
        y = 600
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
            
            # get txt node 1
            txtNode1 = line[4] # get txt node 1 - inject to drawingLabel
            # get txt node 
            txtNode2 = line[5] # get txt node 2 - inject to drawingLabel

            #print('un label de dessinner')

            drawingLabel(xDraw, y , txtLabel , colorLabel ,txtNode1, txtNode2 )  #inject here
            y = y + 200
            
            #print(i)
        drawingNode()

