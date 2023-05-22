from src.util.mysql import MySQLUtil


def get_databases():
    sql = "show databases;"
    return MySQLUtil().execute_sql(sql)


def get_tables(database: str):
    sql = f"show tables from {database};"
    return MySQLUtil().execute_sql(sql)


def get_create_table(database: str, table: str):
    sql = f"show create table {database}.{table};"
    return MySQLUtil().execute_sql(sql)


if __name__ == '__main__':
    databases = get_databases()
    for database in databases:
        tables = get_tables(database[0])
        for table in tables:
            create_table = get_create_table(database[0], table[0])
            print(create_table[0][1] + '\n')
