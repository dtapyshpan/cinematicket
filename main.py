#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *

from optionsdialog import *
from centralwidget import *

class Cinema(QMainWindow):
  #price for 1-3 rows
  price1 = -1
  #price for 4-7 rows
  price2 = -1
  #price for 8-10 rows
  price3 = -1
  #amount of the rows
  mxrow = 10
  #amount of the columns
  mxcolumn = 20

  def __init__(self):
    super().__init__()
    self.initui()

  def makemenubar(self):
    #options action
    optionaction = QAction(QIcon('icon/options.jpg'), '&Настройки', self)
    optionaction.setShortcut('Ctrl+O')
    optionaction.triggered.connect(self.optiontriggered)
    ############
    #exit action
    exitaction = QAction(QIcon('icon/exit.jpg'), '&Выход', self)
    exitaction.setShortcut('Ctrl+Q')
    exitaction.triggered.connect(qApp.quit)
    ############

    menubar = self.menuBar()
    filemenu = menubar.addMenu('&Файл')
    filemenu.addAction(optionaction)
    filemenu.addAction(exitaction)
    filemenu = menubar.addMenu('&Помощь')

  def initui(self):
    self.makemenubar()
    centralwidget = CentralWidget(Cinema.mxrow, Cinema.mxcolumn)
    self.setCentralWidget(centralwidget)
    self.setMinimumSize(750, 350)
    self.setMaximumSize(750, 350)
    self.setWindowTitle('Кинотеатр')
    self.show()

  def optiontriggered(self):
    option = OptionsDialog(Cinema.price1, Cinema.price2, Cinema.price3)
    result = option.exec_()
    if (result == QDialog.Accepted):
      Cinema.price1, Cinema.price2, Cinema.price3 = option.getprices()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Cinema()                                            
  sys.exit(app.exec_())

