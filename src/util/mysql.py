import mysql.connector


class MySQLUtil:
    host = "localhost"
    user = "root"
    password = "danny"
    database = "employees"

    def __init__(self, host="localhost", user="root", password="danny", database="employees"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_sql(self, sql: str):
        connect = self.get_connection()
        cursor = connect.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            results = [list(result) for result in results]
            return results
        finally:
            cursor.close()
            connect.close()


if __name__ == '__main__':
    mysql_util = MySQLUtil()
    sql = "show tables from employees;"
    result = mysql_util.execute_sql(sql)
    print(result)
