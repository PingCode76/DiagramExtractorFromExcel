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
def drawingNode(xDraw,y,i,nbDraw,VariablespositionLabels,nbLabel):
    # Import nodes
    nodes = nodeInformation(nbDraw) #output : {node1: [label1, label5], node2:... }
    print(nodes)
    LabelInfo = LabelInformation(nbDraw)
    print(VariablespositionLabels)

    print('les noeuds')
    print(nodes)
    # for each nodes
    for node in nodes: #
        # out node = i ( label number)
        # obtenir une position x

        print("Label position x")
        print(VariablespositionLabels['label'+str(i)+'x'])
    
        # obtenir une position y
        print("Label position y")
        print(VariablespositionLabels['label'+str(i)+'y'])
        

        #while i > nbLabel:
        if i - 2 > nbLabel:
            # actual label 
            print("position premier label")
            labelFirstX = VariablespositionLabels['label'+str(nodes[node][1])+'x'] # pos x of out node
            labelFirstY = VariablespositionLabels['label'+str(nodes[node][1])+'y'] # pos y of out node 
            
            # labelpremierY = VariablespositionLabels['label'+str(i)+'y'] # ? 
            turtle.up()
            turtle.color('red') 
            turtle.pensize(5.5)
            turtle.goto(labelFirstX + 272 , labelFirstY + 65) # pos start 
            turtle.down()
            turtle.pensize(-5.5)

            # pos finish label 
            print("position deuxiéme label")
            labelSecondX = VariablespositionLabels['label'+str(nodes[node][0])+'x'] # pos x of in node
            labelSecondY = VariablespositionLabels['label'+str(nodes[node][0])+'y'] # pos y of in node
            
            turtle.color('green') 
            turtle.pensize(5.5)
            turtle.goto(labelSecondX-25,labelSecondY+ 60) # pos finish
            #turtle.goto(30,30) # test
            turtle.pensize(-5.5)
            turtle.up()
        #else:

            

    return


def drawDiagram(nbDraw):
    labelGroup = LabelInformation(nbDraw)
    xDraw = -1350
    VariablespositionLabels = {}
    for i in labelGroup:
        #print(labelGroup[i])
        # for each rectangle
        drawingRectangle(nbDraw)
        xDraw = xDraw + 400
        y = 600
        nbLabel = len(labelGroup[i])
        for i in labelGroup[i]:
            # get txt and node of label
            # add y and y data in labelVariableXY

            textnbLabel = "label" + str(i)
            print(textnbLabel)
            #VariablespositionLabels.update = ({textnbLabel + 'x': xDraw, textnbLabel + 'y': y})
            VariablespositionLabels[textnbLabel + 'x'] = xDraw
            VariablespositionLabels[textnbLabel + 'y'] = y

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
            
            drawingLabel(xDraw, y , txtLabel , colorLabel ,txtNode1, txtNode2 )  #inject here
            drawingNode(xDraw,y,i,nbDraw, VariablespositionLabels,nbLabel) 
            y = y + 200