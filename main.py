import sys
from random import choice, sample

from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import *
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
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
    "10": "10.jpg"
}

LIST_FILE_NAME = [i for i in DICT_FILE_NAME.keys()]


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('u i/main_window.ui', self)

        database = QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('result.db')
        database.open()
        model = QSqlTableModel(self, database)
        model.setTable('result')
        model.select()
        self.table.setModel(model)

        self.list_image_random = []

        self.pushButton_2.clicked.connect(self.close_window)
        self.setWindowIcon(QIcon('images/anton.jpg'))
        self.pushButton.clicked.connect(self.add_data_base)
        self.flag_close = True

    def add_data_base(self):
        try:
            string = self.textEdit.toPlainText()
            if db_base.select_is(string) and string != ' ':
                db_base.add(string)
                self.pushButton.setText("Вперед")
                self.pushButton.clicked.connect(self.open_window)
            else:
                self.pushButton.setText("Введите другое имя!")

        except BaseException:
            self.pushButton.setText("Введите другое имя!")

    def open_window(self):
        main_window.show()

    def open_window_2(self):
        main_window.show()

    def close_window(self):
        self.close()


class Main_window(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ui/window_image.ui', self)
        self.setWindowIcon(QIcon('images/anton.jpg'))

        self.cnt = 0
        self.element_list = []

        self.flag1 = True
        self.flag2 = True
        self.flag3 = True
        self.flag4 = True
        self.flag5 = True
        self.flag6 = True
        self.flag7 = True
        self.flag8 = True
        self.flag9 = True
        self.flag10 = True

        self.flag_1 = True
        self.flag_2 = True
        self.flag_3 = True
        self.flag_4 = True
        self.flag_5 = True
        self.flag_6 = True
        self.flag_7 = True
        self.flag_8 = True
        self.flag_9 = True
        self.flag_10 = True

        self.random_element_1 = self.random_()
        self.random_element_2 = self.random_()
        self.random_element_3 = self.random_()
        self.random_element_4 = self.random_()
        self.random_element_5 = self.random_()
        self.random_element_6 = self.random_()
        self.random_element_7 = self.random_()
        self.random_element_8 = self.random_()
        self.random_element_9 = self.random_()
        self.random_element_10 = self.random_()

        self.list_random_element_1 = choice(self.random_element_1)
        self.list_random_element_2 = choice(self.random_element_2)
        self.list_random_element_3 = choice(self.random_element_3)
        self.list_random_element_4 = choice(self.random_element_4)
        self.list_random_element_5 = choice(self.random_element_5)
        self.list_random_element_6 = choice(self.random_element_6)
        self.list_random_element_7 = choice(self.random_element_7)
        self.list_random_element_8 = choice(self.random_element_8)
        self.list_random_element_9 = choice(self.random_element_9)
        self.list_random_element_10 = choice(self.random_element_10)

        self.img = self.label
        self.img.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_1)]}"))
        self.img2 = self.label_2
        self.img2.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img3 = self.label_3
        self.img3.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img4 = self.label_4
        self.img4.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img5 = self.label_5
        self.img5.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_2)]}"))
        self.img6 = self.label_6
        self.img6.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img7 = self.label_7
        self.img7.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img8 = self.label_8
        self.img8.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img9 = self.label_9
        self.img9.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_3)]}"))
        self.img10 = self.label_10
        self.img10.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img11 = self.label_11
        self.img11.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img12 = self.label_12
        self.img12.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img21 = self.label_21
        self.img21.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_6)]}"))
        self.img22 = self.label_22
        self.img22.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img23 = self.label_23
        self.img23.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img24 = self.label_24
        self.img24.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img13 = self.label_13
        self.img13.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_4)]}"))
        self.img14 = self.label_14
        self.img14.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img15 = self.label_15
        self.img15.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img16 = self.label_16
        self.img16.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img17 = self.label_17
        self.img17.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_5)]}"))
        self.img18 = self.label_18
        self.img18.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img19 = self.label_19
        self.img19.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img20 = self.label_20
        self.img20.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img25 = self.label_25
        self.img25.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_7)]}"))
        self.img26 = self.label_26
        self.img26.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img27 = self.label_27
        self.img27.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img28 = self.label_28
        self.img28.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img29 = self.label_29
        self.img29.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_8)]}"))
        self.img30 = self.label_30
        self.img30.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img31 = self.label_31
        self.img31.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img32 = self.label_32
        self.img32.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img33 = self.label_33
        self.img33.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_9)]}"))
        self.img34 = self.label_34
        self.img34.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img35 = self.label_35
        self.img35.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img36 = self.label_36
        self.img36.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.img37 = self.label_37
        self.img37.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_10)]}"))
        self.img38 = self.label_38
        self.img38.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img39 = self.label_39
        self.img39.setPixmap(QPixmap(f"images/фон2.jpg"))
        self.img40 = self.label_40
        self.img40.setPixmap(QPixmap(f"images/фон2.jpg"))

        self.pushButton_5.clicked.connect(self.random_element_func_1)
        self.pushButton_6.clicked.connect(self.random_element_func_2)
        self.pushButton_7.clicked.connect(self.random_element_func_3)
        self.pushButton_8.clicked.connect(self.random_element_func_4)
        self.pushButton_9.clicked.connect(self.random_element_func_5)
        self.pushButton_37.clicked.connect(self.random_element_func_6)
        self.pushButton_38.clicked.connect(self.random_element_func_7)
        self.pushButton_39.clicked.connect(self.random_element_func_8)
        self.pushButton_40.clicked.connect(self.random_element_func_9)
        self.pushButton_41.clicked.connect(self.random_element_func_10)

        self.pushButton.clicked.connect(self.run1)
        self.pushButton_2.clicked.connect(self.run2)
        self.pushButton_3.clicked.connect(self.run3)

        self.pushButton_10.clicked.connect(self.run4)
        self.pushButton_11.clicked.connect(self.run5)
        self.pushButton_12.clicked.connect(self.run6)

        self.pushButton_14.clicked.connect(self.run7)
        self.pushButton_15.clicked.connect(self.run8)
        self.pushButton_13.clicked.connect(self.run9)

        self.pushButton_16.clicked.connect(self.run12)
        self.pushButton_17.clicked.connect(self.run10)
        self.pushButton_18.clicked.connect(self.run11)

        self.pushButton_19.clicked.connect(self.run15)
        self.pushButton_20.clicked.connect(self.run13)
        self.pushButton_21.clicked.connect(self.run14)

        self.pushButton_22.clicked.connect(self.run18)
        self.pushButton_23.clicked.connect(self.run16)
        self.pushButton_24.clicked.connect(self.run17)

        self.pushButton_25.clicked.connect(self.run21)
        self.pushButton_26.clicked.connect(self.run19)
        self.pushButton_27.clicked.connect(self.run20)

        self.pushButton_28.clicked.connect(self.run24)
        self.pushButton_29.clicked.connect(self.run22)
        self.pushButton_30.clicked.connect(self.run23)

        self.pushButton_31.clicked.connect(self.run27)
        self.pushButton_32.clicked.connect(self.run25)
        self.pushButton_33.clicked.connect(self.run26)

        self.pushButton_35.clicked.connect(self.run28)
        self.pushButton_36.clicked.connect(self.run29)
        self.pushButton_34.clicked.connect(self.run30)

        self.pushButton_4.clicked.connect(self.exit)

    def random_(self):
        self.element_list = [i for i in LIST_FILE_NAME]
        element_1, element_2, element_3 = sample(self.element_list, 3)
        return [element_1, element_2, element_3]

    def random_element_func_1(self):
        try:
            self.img.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_1.remove(self.list_random_element_1)
            self.img2.setPixmap(QPixmap(
                f"images/{DICT_FILE_NAME[self.random_element_1[0]]}"))
            self.img3.setPixmap(QPixmap(
                f"images/{DICT_FILE_NAME[self.random_element_1[1]]}"))
            self.img4.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[self.list_random_element_1]}"))
            self.flag_1 = False

        except BaseException:
            self.pushButton_5.setText("Вы играли")

    def random_element_func_2(self):
        try:
            self.img5.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_2.remove(self.list_random_element_2)
            self.img6.setPixmap(QPixmap(
                f"images/{DICT_FILE_NAME[self.random_element_2[1]]}"))
            self.img7.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[self.list_random_element_2]}"))
            self.img8.setPixmap(QPixmap(
                f"images/{DICT_FILE_NAME[self.random_element_2[0]]}"))
            self.flag_2 = False

        except BaseException:
            self.pushButton_6.setText("Вы играли")

    def random_element_func_3(self):
        try:
            self.img9.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_3.remove(self.list_random_element_3)
            self.img10.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[self.random_element_3[0]]}"))
            self.img11.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[self.random_element_3[1]]}"))
            self.img12.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[self.list_random_element_3]}"))
            self.flag_3 = False

        except BaseException:
            self.pushButton_7.setText("Вы играли")

    def random_element_func_4(self):
        try:
            self.img13.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_4.remove(self.list_random_element_4)
            self.img14.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_4[1])]}"))
            self.img15.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_4)]}"))
            self.img16.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_4[0])]}"))
            self.flag_4 = False

        except BaseException:
            self.pushButton_8.setText("Вы играли")

    def random_element_func_5(self):
        try:
            self.img17.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_5.remove(self.list_random_element_5)
            self.img18.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_5)]}"))
            self.img19.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_5[0])]}"))
            self.img20.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_5[1])]}"))
            self.flag_5 = False

        except BaseException:
            self.pushButton_9.setText("Вы играли")

    def random_element_func_6(self):
        try:
            self.img21.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_6.remove(self.list_random_element_6)
            self.img22.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_6[1])]}"))
            self.img23.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_6)]}"))
            self.img24.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_6[0])]}"))
            self.flag_6 = False

        except BaseException:
            self.pushButton_37.setText("Вы играли")

    def random_element_func_7(self):
        try:
            self.img25.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_7.remove(self.list_random_element_7)
            self.img26.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_7)]}"))
            self.img27.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_7[0])]}"))
            self.img28.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_7[1])]}"))
            self.flag_7 = False

        except BaseException:
            self.pushButton_38.setText("Вы играли")

    def random_element_func_8(self):
        try:
            self.img29.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_8.remove(self.list_random_element_8)

            self.img30.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_8[1])]}"))
            self.img31.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_8)]}"))
            self.img32.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_8[0])]}"))
            self.flag_8 = False

        except BaseException:
            self.pushButton_39.setText("Вы играли")

    def random_element_func_9(self):
        try:
            self.img33.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_9.remove(self.list_random_element_9)
            self.img34.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_9)]}"))
            self.img35.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_9[0])]}"))
            self.img36.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_9[1])]}"))
            self.flag_9 = False

        except BaseException:
            self.pushButton_40.setText("Вы играли")

    def random_element_func_10(self):
        try:
            self.img37.setPixmap(QPixmap(f"images/фон.jpg"))
            self.random_element_10.remove(self.list_random_element_10)
            self.img38.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_10[1])]}"))
            self.img39.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.list_random_element_10)]}"))
            self.img40.setPixmap(QPixmap(f"images/{DICT_FILE_NAME[str(self.random_element_10[0])]}"))
            self.flag_10 = False

        except BaseException:
            self.pushButton_41.setText("Вы играли")

    def run1(self):
        if not self.flag_1:
            self.flag1 = False
            self.cnt += 0

    def run2(self):
        if not self.flag_1:
            self.flag1 = False
            self.cnt += 0

    def run3(self):
        if not self.flag_1 and self.flag1:
            self.flag1 = False
            self.cnt += 1
            self.textBrowser.setText("1")

    def run4(self):
        if not self.flag_2:
            self.flag2 = False
            self.cnt += 0

    def run5(self):
        if not self.flag_2 and self.flag2:
            self.flag2 = False
            self.cnt += 1
            self.textBrowser_2.setText("1")

    def run6(self):
        if not self.flag_2:
            self.flag2 = False
            self.cnt += 0

    def run7(self):
        if not self.flag_3:
            self.flag3 = False
            self.cnt += 0

    def run9(self):
        if not self.flag_3 and self.flag3:
            self.flag3 = False
            self.cnt += 1
            self.textBrowser_3.setText("1")

    def run8(self):
        if not self.flag_3:
            self.flag3 = False
            self.cnt += 0

    def run10(self):
        if not self.flag_4:
            self.flag4 = False
            self.cnt += 0

    def run11(self):
        if not self.flag_4 and self.flag4:
            self.flag4 = False
            self.cnt += 1
            self.textBrowser_4.setText("1")

    def run12(self):
        if not self.flag_4:
            self.flag4 = False
            self.cnt += 0

    def run13(self):
        if not self.flag_5 and self.flag5:
            self.flag5 = False
            self.cnt += 1
            self.textBrowser_5.setText("1")

    def run14(self):
        if not self.flag_5:
            self.flag5 = False
            self.cnt += 0

    def run15(self):
        if not self.flag_5:
            self.flag5 = False
            self.cnt += 0

    def run16(self):
        if not self.flag_6:
            self.flag6 = False
            self.cnt += 0

    def run17(self):
        if not self.flag_6 and self.flag6:
            self.flag6 = False
            self.cnt += 1
            self.textBrowser_6.setText("1")

    def run18(self):
        if not self.flag_6:
            self.flag6 = False
            self.cnt += 0

    def run19(self):
        if not self.flag_7 and self.flag7:
            self.flag7 = False
            self.cnt += 1
            self.textBrowser_7.setText("1")

    def run20(self):
        if not self.flag_7:
            self.flag6 = False
            self.cnt += 0

    def run21(self):
        if not self.flag_7:
            self.flag6 = False
            self.cnt += 0

    def run22(self):
        if not self.flag_8:
            self.flag8 = False
            self.cnt += 0

    def run23(self):
        if not self.flag_8 and self.flag8:
            self.flag8 = False
            self.cnt += 1
            self.textBrowser_8.setText("1")

    def run24(self):
        if not self.flag_8:
            self.flag8 = False
            self.cnt += 0

    def run25(self):
        if not self.flag_9 and self.flag9:
            self.flag9 = False
            self.cnt += 1
            self.textBrowser_9.setText("1")

    def run26(self):
        if not self.flag_9:
            self.flag9 = False
            self.cnt += 0

    def run27(self):
        if not self.flag_9:
            self.flag9 = False
            self.cnt += 0

    def run28(self):
        if not self.flag_10:
            self.flag10 = False
            self.cnt += 0

    def run29(self):
        if not self.flag_10 and self.flag10:
            self.flag10 = False
            self.cnt += 1
            self.textBrowser_10.setText("1")


    def run30(self):
        if not self.flag_10:
            self.flag10 = False
            self.cnt += 0

    def exit(self):
        try:
            element = int(self.textBrowser.toPlainText()) + int(self.textBrowser_2.toPlainText()) + int(
                self.textBrowser_3.toPlainText()) + int(
                self.textBrowser_4.toPlainText()) + int(self.textBrowser_5.toPlainText()) + int(
                self.textBrowser_6.toPlainText()) + int(
                self.textBrowser_7.toPlainText()) + int(self.textBrowser_8.toPlainText()) + int(
                self.textBrowser_9.toPlainText()) + int(
                self.textBrowser_10.toPlainText())
            db_base.update_result(element, db_base.data_base_con())
        except BaseException as e:
            print(e)

        finally:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    main_window = Main_window()
    ex.show()
    sys.exit(app.exec())
