import pymysql
# Constants


class DBConnector:

    # initialize the class (constructor)
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.conn = None

    # create the connection to the MySql
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    # close the connection to the MySql

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

        # add new user to users table

    def adduser(self, user_id, user_name):
        self.connect()
        try:
            with self.conn.cursor() as cursor:

                sql = "INSERT INTO users VALUES (%s, %s, NOW())"
                cursor.execute(sql, (user_id, user_name))
                self.conn.commit()
        finally:
            self.disconnect()

    # return the username by the user_id parameter

    def get_user_name(self, user_id):
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                sql = f"SELECT user_name FROM users WHERE user_id = %s"
                cursor.execute(sql, user_id)
                result = cursor.fetchone()
                if result is not None:
                    return result[0]
                else:
                    return None
        finally:
            self.disconnect()

# update the username by the user_id parameter

    def update_user_name(self, user_id, user_name):
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                sql = f"UPDATE users SET user_name = %s WHERE user_id = %s"
                cursor.execute(sql, (user_name, user_id))
                self.conn.commit()
        finally:
            self.disconnect()

    # delete the username by the user_id parameter

    def delete_user(self, user_id):
        self.connect()
        try:
            with self.conn.cursor() as cursor:
                sql = f"DELETE FROM users WHERE user_id = %s"
                cursor.execute(sql, user_id)
                self.conn.commit()

        finally:
            self.disconnect()


