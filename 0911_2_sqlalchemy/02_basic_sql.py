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

# insert（サニタイジングなし）
# with engine.connect() as con:   
#     sql = text("INSERT INTO user(name,age) VALUES('a', 20)")
    
#     # SQL実行
#     result = con.execute(sql)
#     con.commit()

#     print(f'挿入件数：{result.rowcount}')

# insert（サニタイジングあり）
# with engine.connect() as con: 
#     sql = text("INSERT INTO user(name,age) VALUES(:name, :age)")
    
#     # SQL実行
#     result = con.execute(sql, {'name':'b', 'age':21})
#     con.commit()

#     print(f'挿入件数：{result.rowcount}')

# update
with engine.connect() as con: 
    sql = text("UPDATE user SET age=:age WHERE name=:name")
    
    # SQL実行
    result = con.execute(sql, {'age':22, 'name':'a'})
    con.commit()

    print(f'更新件数：{result.rowcount}')

# delete
with engine.connect() as con: 
    sql = text("DELETE FROM user WHERE name=:name")
    
    # SQL実行
    result = con.execute(sql, {'name':'b'})
    con.commit()

    print(f'削除件数：{result.rowcount}')

# select
with engine.connect() as con:   
    sql = text("SELECT * FROM user")
    
    # SQL実行
    rows = con.execute(sql)

    for row in rows:
        print(f'id:{row.id}, name:{row.name}, age:{row.age}')