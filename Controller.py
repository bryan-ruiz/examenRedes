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
                sql = "SELECT * FROM `tweet`"
                cursor.execute(sql)
                results = cursor.fetchall()
                return results

        finally:
            self.connection.close()
