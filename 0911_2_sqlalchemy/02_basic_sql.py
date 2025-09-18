# 02_basic_sql.py
from sqlalchemy import create_engine, text

# engineの作成（DB接続の必要情報定義）
engine = create_engine(
    'sqlite:///user.db',
    echo=True # 裏で動作しているSQLを出力する
)

with engine.connect() as con:
    # with文
    # やっていることは以下。
    # con = engine.connect()
    # con.close() <-これを自動的に実行してくれる
    sql = text('''\
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name STRING,
            age INTEGER
        )\
    ''')

    # SQL実行
    con.execute(sql)
    con.commit()

# insert
with engine.connect() as con:   
    sql = text("INSERT INTO user(name,age) VALUES('a', 20)")
    
    # SQL実行
    con.execute(sql)
    con.commit()