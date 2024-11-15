import sqlite3


class Db_QT6():
    def __init__(self):
        self.name = 'db1.db'
        self.conn = sqlite3.connect('db1.db')

    def add(self, string):
        cur = self.conn.cursor()
        try:
            cur.execute(f"""INSERT INTO result (Name, Result) VALUES ("{string}", 0)""")
            self.conn.commit()
        finally:
            pass
            # self.conn.close()

    def select_is(self, is_string):
        cur = self.conn.cursor()
        try:
            string = cur.execute(f"""SELECT Name FROM result""").fetchall()
            if is_string not in string:
                return True
            return False
        finally:
            pass
            # self.conn.close()
