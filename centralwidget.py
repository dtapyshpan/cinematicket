from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *

from place import *

class CentralWidget(QWidget):
  #places in cinema
  places = None

  def __init__(self, mxrow, mxcolumn):
    super().__init__()
    CentralWidget.places = [[0 for x in range(mxcolumn + 3)] for x in range(mxrow + 3)]
    self.initui(mxrow, mxcolumn)
    
  #init main user interface
  def initui(self, mxrow, mxcolumn):
    grid = QGridLayout()
    self.setLayout(grid)
    #init first row
    for column in range(1, mxcolumn + 3):
      if (column <= mxcolumn):
        lbl = QLabel(str(column))
        grid.addWidget(lbl, 0, column)
      if (column == mxcolumn + 1):
        lbl = QLabel(str('Осталось\nмест'))
        grid.addWidget(lbl, 0, column)
      if (column == mxcolumn + 2):
        lbl = QLabel(str('Макс\nгруппа'))
        grid.addWidget(lbl, 0, column)

    #init first column and places (check boxes)
    for row in range(1, mxrow + 1):
      lbl = QLabel(str(row))
      grid.addWidget(lbl, row, 0)
      for column in range(1, mxcolumn + 1):
        cplace = Place(row, column)
        if (row >= 1 and row <= 3):
          cplace.setStyleSheet("background-color: lightgreen;")
        elif (row >= 4 and row <= 7):
          cplace.setStyleSheet("background-color: yellow;")
        else:
          cplace.setStyleSheet("background-color: lightblue;")
        #cplace.stateChanged.connect(cplace.placestatechange)
        cplace.stateChanged.connect(self.gotplace)
        grid.addWidget(cplace, row, column)
        CentralWidget.places[row][column] = cplace
      lbl1 = QLabel(str(mxcolumn))
      grid.addWidget(lbl1, row, mxcolumn + 1)
      lbl2 = QLabel(str(mxcolumn))
      grid.addWidget(lbl2, row, mxcolumn + 2)
  
  def gotplace(self, x, y):
    print("hehe")

