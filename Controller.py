import pymysql.cursors

class Controller:

    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='twitter',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


    def solicitar(self):
        try:
            with self.connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `tweet`"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)

        finally:
            self.connection.close()
