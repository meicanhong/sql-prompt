from src.conf.config import DATABASE_CONF
import mysql.connector

class MySQLUtil:
    def __init__(self):
        self.host = DATABASE_CONF['host']
        self.user = DATABASE_CONF['username']
        self.password = DATABASE_CONF['password']
        self.database = DATABASE_CONF['database'] if DATABASE_CONF['database'] else None

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
