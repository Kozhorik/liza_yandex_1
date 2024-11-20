import sqlite3


class Db_QT6():
    def __init__(self):
        self.name = 'result.db'
        self.conn = sqlite3.connect(self.name)

    def add(self, string):
        cur = self.conn.cursor()
        try:
            cur.execute(f"""INSERT INTO result (Name, Result) VALUES ("{string}", 0)""")
            self.conn.commit()
        except BaseException:
            self.conn.close()

    def select_is(self, is_string):
        cur = self.conn.cursor()
        try:
            string = cur.execute(f"""SELECT Name FROM result""").fetchall()
            if (is_string, ) in string:
                return False
            return True
        except BaseException:
            return False

    def data_base_con(self):
        cur = self.conn.cursor()
        string = cur.execute(f"""SELECT Name FROM result""").fetchall()
        return string[-1][0]

    def update_result(self, string_result, string_name):
        cur = self.conn.cursor()
        try:
            cur.execute(f"""UPDATE result set Result = {string_result} WHERE Name = '{string_name}'""")
            self.conn.commit()
        finally:
            self.conn.close()