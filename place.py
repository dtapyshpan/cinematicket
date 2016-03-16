from PyQt5.QtWidgets import *
from PyQt5.QtGui import  *

class Place(QCheckBox):
  row = -1
  column = -1

  def __init__(self, rpos, cpos):
    super().__init__()
    Place.row = rpos
    Place.column = cpos

