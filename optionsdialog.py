from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *
from PyQt5.QtCore import *

class OptionsDialog(QDialog):
  qle1 = None
  qle2 = None
  qle3 = None
  
  def __init__(self, p1, p2, p3):
    super().__init__()
    self.initui(p1, p2, p3)

  def initui(self, p1, p2, p3):
    #labels and line edits init
    qlbl1 = QLabel('Стоимость билетов 1-3 ряд:')
    qlbl2 = QLabel('Стоимость билетов 4-7 ряд:')
    qlbl3 = QLabel('Стоимость билетов 8-10 ряд:')
    intvalidator = QIntValidator(0, 9999999);
    OptionsDialog.qle1 = QLineEdit()
    OptionsDialog.qle1.setValidator(intvalidator)
    OptionsDialog.qle2 = QLineEdit()
    OptionsDialog.qle2.setValidator(intvalidator)
    OptionsDialog.qle3 = QLineEdit()
    OptionsDialog.qle3.setValidator(intvalidator)

    if (p1 != -1):
      OptionsDialog.qle1.setText(str(p1))
      OptionsDialog.qle2.setText(str(p2))
      OptionsDialog.qle3.setText(str(p3))

    #init of the layout
    hlayout1 = QHBoxLayout()
    hlayout1.addStretch(1)
    hlayout1.addWidget(qlbl1)
    hlayout1.addWidget(OptionsDialog.qle1)
    hlayout2 = QHBoxLayout()
    hlayout2.addStretch(1)
    hlayout2.addWidget(qlbl2)
    hlayout2.addWidget(OptionsDialog.qle2)
    hlayout3 = QHBoxLayout()
    hlayout3.addWidget(qlbl3)
    hlayout3.addWidget(OptionsDialog.qle3)
    hlayout3.addStretch(1)
   
    #init of the (ok and cancel) buttons
    buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                               Qt.Horizontal, self)
    buttons.accepted.connect(self.accept)
    buttons.rejected.connect(self.reject)

    #init layout for buttons
    hlayout4 = QHBoxLayout()
    hlayout4.addStretch(1)
    hlayout4.addWidget(buttons)

    #main layout init
    vlayout = QVBoxLayout()
    vlayout.addLayout(hlayout1)
    vlayout.addLayout(hlayout2)
    vlayout.addLayout(hlayout3)
    vlayout.addLayout(hlayout4)
    vlayout.addStretch(1)

    self.setLayout(vlayout)
    
  def getprices(self):
    if (OptionsDialog.qle1.text() == ""):
      return (-1, -1, -1)
    if (OptionsDialog.qle2.text() == ""):
      return (-1, -1, -1)
    if (OptionsDialog.qle3.text() == ""):
      return (-1, -1, -1)
    return (int(OptionsDialog.qle1.text()), int(OptionsDialog.qle2.text()), int(OptionsDialog.qle3.text()))

