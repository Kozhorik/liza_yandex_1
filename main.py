import sys

import io
from PyQt6 import *
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import *
from db_qt6 import Db_QT6

db_base = Db_QT6()


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('des.ui', self)

        self.pushButton.clicked.connect(self.add_data_base)

    def add_data_base(self):
        try:
            n = self.textEdit.toPlainText()
            print(n)
            db_base.add(n)
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
