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

def drawingNode(xDraw,y,NumberOfLabel):
    # Import nodes
    nodes = nodeInformation() #output : {node1: [label1, label5], node2:... }
    LabelInfo = LabelInformation()

    #print(" nodes" )
    #print(nodes) #output : {node1: [label1, label5], node2:... }

    #print(" label info" )
    #print(LabelInfo) 

    # for each nodes
    for node in nodes: # 
        #print(" nodes i" )
        #print( nodes[node] ) # i = chaque noeuds node i [ label x , label y ]

        print("LabelInfo")
        print(LabelInfo)  # pour le rectangle 1 on a le label 1 et 6 , 2->2 & 7 
        print(LabelInfo['1']) # rectangle 1 
        print(LabelInfo['1'][0]) # Premier Label Numero 6 du premier rectangle 
        print(LabelInfo['1'][1]) # Deuxiéme label du premier rectangle
       
       # good 
        print("nodes")
        print(nodes) # le noeud i doit etre relié au label x et y 

        print("nodes numéro 2 a l'entré ")
        print(nodes[2][0])   #nodes[numéro du noeud], [0entré/1sortie]

        print("nodes numéro 2 a la sortie ")
        print(nodes[2][1])
        
        #print(" NumberOfLabel" )
        #print(NumberOfLabel) # doit etre le numéro de ligne dans le tableau 
            
        # Si le numéro de la ligne du tableau  est égal a un numéro de la ligne qui provient de node alors , on rejouint les deux labels 
            #if NumberOfLabel == lineNode[i]:
        if nodes[node][1] == LabelInfo['1'][0]: # le noeud 1 doit etre relié au label x et y 
            print("hello condition vérifier")
    
            # Drawing node
            # LINK
            # LABEL 1  #get position label 1 
            #print (xDraw)
            #print (y) 
            turtle.goto(xDraw+250,y)
            turtle.down()
            turtle.color('red') # color 
            turtle.circle(35)  
            turtle.forward(150) # ( width )
            turtle.circle(35)  
            #turtle.end_fill() 
            turtle.up()
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

            #print(line)
            txtLabel = line[3] # get txt in DataLine - inject to drawingLabel
            #print(txtLabel)

            # get color of label
            color = checkdifferentsColor()
            colorLabel = color[i] # get color - inject to drawingLabel
            #print(color[i])
            
            # get txt node 1
            txtNode1 = line[4] # get txt node 1 - inject to drawingLabel
            # get txt node 
            txtNode2 = line[5] # get txt node 2 - inject to drawingLabel

            drawingLabel(xDraw, y , txtLabel , colorLabel ,txtNode1, txtNode2 )  #inject here

            # TEST for get label line 
            NumberOfLabel = 2 # get line of label ( drawing node ) retrouver la ligne qu'on trouve dans node 1 : [1,5] retrouver 1 et 5 
            #print(NumberOfLabel)
            #print("line") 
            #print(line)

            drawingNode(xDraw,y,NumberOfLabel) 
            y = y + 200
            
            #print(i)
