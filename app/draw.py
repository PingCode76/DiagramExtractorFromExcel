from .diagram import * 

def drawingRectangle(nbDraw):
    x = -1000
    for rectangle in LabelInformation(nbDraw):
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


    turtle.write(txtLabel[0:27]) # 15 first character
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

def drawingNode(xDraw,y,i,nbDraw,nbLabel):
    
    # Import nodes
    nodes = nodeInformation(nbDraw) #output : {node1: [label1, label5], node2:... }
    LabelInfo = LabelInformation(nbDraw)

    # for each nodes
    for node in nodes:

        # out node = i ( label number)
        print("nodes")
        print(node)
        print("nodes[node]")
        print(nodes[node])
        print("nodes entré")
        print(nodes[node][0])
        print("nodes sortie")
        print(nodes[node][1])
        print("i")
        print(i)


        if nodes[node][1] == i : 
    
            print(y)
            # face to face
            if nodes[node][1] == i & nodes[node][0] == i or nbLabel == 1 :
                print("face to face verified")
                turtle.goto(xDraw+275,y+65)
                turtle.down()
                turtle.color('white') # color 
                turtle.pensize(5.5)
                turtle.forward(150) # ( width )
                turtle.pensize(-5.5)
                turtle.up()
 
            # top for bottom 
            if y == 800 and nbLabel != 1 or nbLabel == 1 & nodes[node][0] == i  : 
                print("top for bottom verified")
                turtle.goto(xDraw+273,y+65) # y = 45 
                turtle.down()
                turtle.color('white') # color 
                turtle.rt(59)
                turtle.pensize(5.5)
                turtle.forward(250) # ( width )
                turtle.pensize(-5.5)
                turtle.rt(-59) 
                turtle.up()

            # bottom for top
            if y == 600 and nbLabel != 1 :
                print("bottom for top verified")
                turtle.goto(xDraw+250,y+95)
                turtle.down()
                turtle.color('white') # color 
                turtle.lt(53)
                turtle.pensize(5.5)
                turtle.forward(230) # ( width )
                turtle.pensize(-5.5)
                turtle.lt(-53)
            
                turtle.up()
    return


def drawDiagram(nbDraw):

    labelGroup = LabelInformation(nbDraw)

    xDraw = -1350
    for i in labelGroup:
        #print(labelGroup[i])
        
        # for each rectangle
        drawingRectangle(nbDraw)
        # change pos draw
        xDraw = xDraw + 400
        # count how label
        y = 600
        nbLabel = len(labelGroup[i])
        for i in labelGroup[i]:
            # get txt and node of label
            line = selectLineinData(int(i), nbDraw)


            #print(line)
            txtLabel = line[3] # get txt in DataLine - inject to drawingLabel
            #print(txtLabel)

            # get color of label
            color = checkdifferentsColor(nbDraw)
            
            colorLabel = color[i] # get color - inject to drawingLabel
            #print(color[i])
            
            # get txt node 1
            txtNode1 = line[4] # get txt node 1 - inject to drawingLabel
            # get txt node 
            txtNode2 = line[5] # get txt node 2 - inject to drawingLabel

            if nbLabel == 1:
                y = 800
            drawingLabel(xDraw, y , txtLabel , colorLabel ,txtNode1, txtNode2 )  #inject here

            drawingNode(xDraw,y,i,nbDraw,nbLabel) 
            y = y + 200
            

