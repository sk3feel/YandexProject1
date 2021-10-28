import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import sqlite3


class Teacher_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('A12_teacher_form.ui', self)
        self.setWindowTitle('DutyManager')

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Teacher_Form()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())