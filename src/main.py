from src.util.chatgpt import ChatGPT
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
    chatgpt = ChatGPT()
    chatgpt.ask("")
    database = 'employees'
    tables = get_tables(database)
    ddls = []
    for table in tables:
        create_table = get_create_table(database, table[0])
        ddls.append(create_table[0][1])

    ddls = '\n'.join(ddls)
    chatgpt.ask("我要你扮演一个专业DBA。我将提供给你数据表结构以及我的需求，你的目标是给我可执行的SQL语句，无需做任何额外解释，只返回可执行的SQL语句。")
    chatgpt.ask("这是我的表结构 \n" + ddls)
    chatgpt.ask("我想要查询所有员工的姓名，薪水，以及部门名称。")

