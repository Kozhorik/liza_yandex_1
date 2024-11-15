import sys
import time

from PyQt6 import *
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import *
from db_qt6 import Db_QT6


db_base = Db_QT6()
DICT_FILE_NAME = {
    "1": "1.jpg",
    "2": "2.jpg",
    "3": "3.jpg",
    "4": "4.jpg",
    "5": "5.jpg",
    "6": "6.jpg",
    "7": "7.jpg",
    "8": "8.jpg",
    "9": "9.jpg",
    "10": "10.jpg",
    "11": "11.jpg",
}


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('des.ui', self)

        self.pushButton_2.clicked.connect(self.close_window)
        self.pushButton.clicked.connect(self.add_data_base)

    def add_data_base(self):
        try:
            string = self.textEdit.toPlainText()
            if db_base.select_is(string):
                db_base.add(string)
                self.pushButton.setText("Вперед")
                self.pushButton.clicked.connect(self.go_1)
            else:
                pass

        except BaseException as e:
            print(e)

    def go_1(self):
        main_window.show()

    def close_window(self):
        self.close()


class Main_window(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('untitled1.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    main_window = Main_window()
    ex.show()
    sys.exit(app.exec())
