import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *

from place import *

class CentralWidget(QWidget):
  #places in cinema
  places = None
  #grid layout
  grid = None
  #rows in cinema
  mxrow = None
  #places in one row
  mxcolumn = None

  def __init__(self, mxrow, mxcolumn):
    super().__init__()
    CentralWidget.places = [[0 for x in range(mxcolumn + 1)] for x in range(mxrow + 1)]
    CentralWidget.mxrow = mxrow
    CentralWidget.mxcolumn = mxcolumn
    self.initui(mxrow, mxcolumn)
    
  #init main user interface
  def initui(self, mxrow, mxcolumn):
    CentralWidget.grid = QGridLayout()
    self.setLayout(CentralWidget.grid)
    #init first row
    for column in range(1, mxcolumn + 3):
      if (column <= mxcolumn):
        lbl = QLabel(str(column))
        CentralWidget.grid.addWidget(lbl, 0, column)
      if (column == mxcolumn + 1):
        lbl = QLabel(str('Осталось\nмест'))
        CentralWidget.grid.addWidget(lbl, 0, column)
      if (column == mxcolumn + 2):
        lbl = QLabel(str('Макс\nгруппа'))
        CentralWidget.grid.addWidget(lbl, 0, column)

    #init first column and places (check boxes)
    for row in range(1, mxrow + 1):
      lbl = QLabel(str(row))
      CentralWidget.grid.addWidget(lbl, row, 0)
      for column in range(1, mxcolumn + 1):
        cplace = Place(row, column)
        if (row >= 1 and row <= 3):
          cplace.setStyleSheet("background-color: lightgreen;")
        elif (row >= 4 and row <= 7):
          cplace.setStyleSheet("background-color: yellow;")
        else:
          cplace.setStyleSheet("background-color: lightblue;")
        cplace.stateChanged.connect(self.gotplace)
        CentralWidget.grid.addWidget(cplace, row, column)
        CentralWidget.places[row][column] = cplace
      lbl1 = QLabel(str(mxcolumn))
      CentralWidget.grid.addWidget(lbl1, row, mxcolumn + 1)
      lbl2 = QLabel(str(mxcolumn))
      CentralWidget.grid.addWidget(lbl2, row, mxcolumn + 2)

  def gotplace(self):
    for row in range(1, len(CentralWidget.places)):
      freeplaces = 0
      maxgroup = 0
      currgroup = 0
      for col in range(1, len(CentralWidget.places[row])):
        if (CentralWidget.places[row][col].isChecked() == True):
          if (currgroup > maxgroup):
            maxgroup = currgroup
          currgroup = 0
        else:
          freeplaces += 1
          currgroup += 1
      if (currgroup > maxgroup):
        maxgroup = currgroup
      CentralWidget.grid.itemAtPosition(row, CentralWidget.mxcolumn + 1).widget().setText(str(freeplaces))
      CentralWidget.grid.itemAtPosition(row, CentralWidget.mxcolumn + 2).widget().setText(str(maxgroup))

  def getreport(self, price1, price2, price3):
    amounttickets = 0
    amountmoney = 0
    for row in range(1, len(CentralWidget.places)):
      for col in range(1, len(CentralWidget.places[row])):
        if (CentralWidget.places[row][col].isChecked() == True):
          amounttickets += 1
          if (row >= 1 and row <= 3):
            amountmoney += price1
          elif (row >= 4 and row <= 7):
            amountmoney += price2
          else:
            amountmoney += price3
    return (amounttickets, amountmoney)

