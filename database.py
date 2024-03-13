import pymysql


class Database:
    def __init__(self):
        pass

    def __get_connection(self):
        f = open("db.txt", 'r')
        host_name = f.readline().strip()
        user_name = f.readline().strip()
        password = f.readline().strip()
        db_name = f.readline().strip()
        f.close()
        return pymysql.connect(
            host=host_name,
            port=3306,
            user=user_name,
            passwd=password,
            db=db_name,
            charset='utf8'
        )


    def execute_sql(self, sql):
        try:
            print(sql)
            connection = self.__get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            rows = cursor.fetchall()
            connection.commit()
            return rows
        except Exception as e:
            print(f"""에러 코드: {e.args[0]}""")
            print(f"""에러 메세지: {e.args[1]}""")
        finally:
            connection.close()
