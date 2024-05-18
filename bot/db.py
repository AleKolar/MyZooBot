import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def user_exist(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchall()
            return bool(len(res))

    def add_user(self, user_id):
        with self.connection:
            if user_id  == None:
                return self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
            else:
                return False



