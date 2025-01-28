from db.mysql_session import init_mysql
from db.sqlite_session import init_sqlite
from db.base_class import Base
# 导入所有表
from models import user, auth


class InitDB():
    def __init__(self, db_name):
        if db_name == "sqlite":
            self.engine, self.sessionLocal = init_sqlite()
        elif db_name == "mysql":
            self.engine, self.sessionLocal = init_mysql()

    def create_all(self):
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    try:
        db = InitDB("mysql")
        db.create_all()
    except Exception as e:
        print(e)
