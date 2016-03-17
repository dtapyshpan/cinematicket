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
  #main scene
  centralwidget = None
  #error message
  errorprice = None
  #report msg
  reportmsg = None
  #report msg1
  reportmsg1 = None
  #report msg2
  reportmsg2 = None
  #about msg
  aboutmsg = None
  #user guide msg
  userguidemainmsg = None
  userguidemsg = None

  def __init__(self):
    super().__init__()
    Cinema.errorprice = "Установите цены на билеты"
    Cinema.reportmsg = "Отчет"
    Cinema.reportmsg1 = "Количество проданных билетов: "
    Cinema.reportmsg2 = "Сумма выручки: "
    Cinema.aboutmsg = "По всем вопросам обращаться: pushpop[at]mail[dot]ru"
    Cinema.userguidemainmsg = "Руководство пользователя"
    Cinema.userguidemsg = "1. Установите цену на билеты (Файл -> Настройки)\n2. Нажатием левой кнопки мышки отмечайте проданные билеты"
    self.initui()
   
  def makemenubar(self):
    #options action
    optionaction = QAction(QIcon('icon/options.jpg'), '&Настройки', self)
    optionaction.setShortcut('Ctrl+Н')
    optionaction.triggered.connect(self.optiontriggered)
    ############
    #report action
    reportaction = QAction(QIcon('icon/report.png'), '&Отчет', self)
    reportaction.setShortcut('Ctrl+О')
    reportaction.triggered.connect(self.reporttriggered)
    ############
    #exit action
    exitaction = QAction(QIcon('icon/exit.jpg'), '&Выход', self)
    exitaction.setShortcut('Ctrl+В')
    exitaction.triggered.connect(qApp.quit)
    ############
    #user guide action
    userguideaction = QAction(QIcon('icon/user-guide.png'), 'Р&уководство пользователя', self)
    userguideaction.setShortcut('Ctrl+У')
    userguideaction.triggered.connect(self.userguidetriggered)
    ############
    #about action
    aboutaction = QAction(QIcon('icon/about.png'), 'О п&рограмме', self)
    aboutaction.setShortcut('Ctrl+Р')
    aboutaction.triggered.connect(self.abouttriggered)
    ############

    menubar = self.menuBar()
    filemenu = menubar.addMenu('&Файл')
    filemenu.addAction(optionaction)
    filemenu.addAction(reportaction)
    filemenu.addAction(exitaction)
    filemenu = menubar.addMenu('&Помощь')
    filemenu.addAction(userguideaction)
    filemenu.addAction(aboutaction)

  def initui(self):
    self.makemenubar()
    Cinema.centralwidget = CentralWidget(Cinema.mxrow, Cinema.mxcolumn)
    self.setCentralWidget(Cinema.centralwidget)
    self.setMinimumSize(750, 350)
    self.setMaximumSize(750, 350)
    self.setWindowTitle('Кинотеатр')
    self.show()

  def optiontriggered(self):
    option = OptionsDialog(Cinema.price1, Cinema.price2, Cinema.price3)
    result = option.exec_()
    if (result == QDialog.Accepted):
      Cinema.price1, Cinema.price2, Cinema.price3 = option.getprices()

  def reporttriggered(self):
    if (Cinema.price1 == -1 or Cinema.price2 == -1 or Cinema.price3 == -1):
      msgBox = QMessageBox()
      msgBox.setText(Cinema.errorprice)
      msgBox.setStandardButtons(QMessageBox.Ok);
      msgBox.exec_();
      return

    amouttickets, amountmoney = Cinema.centralwidget.getreport(Cinema.price1, Cinema.price2, Cinema.price3)

    msgBox = QMessageBox()
    msgBox.setText(Cinema.reportmsg)
    msgBox.setInformativeText(Cinema.reportmsg1 + str(amouttickets) + "\n" + Cinema.reportmsg2 + str(amountmoney))
    msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Ok)
    ret = msgBox.exec_()
    if (ret == QMessageBox.Save):
      fname, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'Text format (*.txt)')
      print(fname)
      fname += ".txt"
      f = open(fname, 'w')
      line1 = Cinema.reportmsg1 + str(amouttickets)
      line2 = Cinema.reportmsg2 + str(amountmoney)
      f.write(line1 + '\n')
      f.write(line2 + '\n')
      f.close()

  def userguidetriggered(self):
    msgBox = QMessageBox()
    msgBox.setText(Cinema.userguidemainmsg)
    msgBox.setInformativeText(Cinema.userguidemsg)
    msgBox.setStandardButtons(QMessageBox.Ok);
    msgBox.exec_();
    
  def abouttriggered(self):
    msgBox = QMessageBox()
    msgBox.setText(Cinema.aboutmsg)
    msgBox.setStandardButtons(QMessageBox.Ok);
    msgBox.exec_();

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = Cinema()                                            
  sys.exit(app.exec_())

