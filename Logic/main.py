from PyQt5.QtWidgets import QApplication
from Logic.A22_login_form import Log_In
import sys


app = QApplication(sys.argv)
ex = Log_In()
ex.show()
sys.exit(app.exec())