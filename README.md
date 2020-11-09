# DiagrameExtractorFromExcel

from data provided by the user, the application is able to create and organize a UML activity diagram

## Use the app 

1. you must clone the project, and download the necessary libraries on your computer (see install chapter).
2. fill in the data at your disposal in the dictionary found in utils.py
3. run a python server and connect to 127.0.0.1:5000 URL
4. Click on generate the diagram

## Generality

Launch a python server:

    python run.py

install the necessary library

    - pip install flask
    - pip install xlrd
    - pip install turtle
    - pip install svgwrite

## How does the app work?

The application works with python and the flask micro-framework. Turtle.py is used for drawing, and SVGwrite is used for exporting drawings to SVG, which will be displayed on web templates.

- The data to transform and draw, are in utils.py
- Diagram.py takes care of formatting the data
- Draw.py takes care of drawing the shapes, according to the data transmitted by diagram.py
- views.py is the application routing file
- base.html/index.html/result.html are template files, no algorithmic element at this
- the generated SVG can be found in static/img/
- run.py is the entry point of the application

## Algorithm

![alt text](https://github.com/PingCode76/DiagramExtractorFromExcel/blob/File/diagramFlowCode.png)

