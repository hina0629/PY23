# 03_sql_injection.py
from sqlalchemy import create_engine, text

# engineの作成（DB接続の必要情報定義）
engine = create_engine(
    'sqlite:///user.db',
    echo=True
)

id = 2
# インジェクションコード
# id = '2'でも動く
# id = '999 OR 1=1'
# id=999？それか1=1？　1=1はtrueだから表示される

# select
with engine.connect() as con: 
    # セキュリティ上文字列連結はNG！
    # sql = text(f"SELECT * FROM user WHERE id={id}")

    # サニタイジング（無害化）するには、
    # プレースホルダ（仮置き場）（:KeyName）を利用する。
    sql = text("SELECT * FROM user WHERE id=:id")
    
    # SQL実行 第２引数にて、仮置き場に値をセットする
    rows = con.execute(sql, {'id': id})

    for row in rows:
        print(f'id:{row.id}, name:{row.name}, age:{row.age}')


name = 'a'

# select
with engine.connect() as con: 
    # SQL文のルールとして、文字データは
    # 「シングルコーテーション(')」でくくる必要がある。
    # sql = text(f"SELECT * FROM user WHERE name='{name}'")
    # rows = con.execute(sql)
    # プレースホルダを利用した場合、
    # 文字データを「シングルコーテーション(')」でくくる。
    # のルールは、自動的に行うため、不要。
    # というか、くくると動かない。
    # sql = text("SELECT * FROM user WHERE name=':name'") <-これは動かない。

    sql = text("SELECT * FROM user WHERE name=:name")
    rows = con.execute(sql, {'name': name})
    
    for row in rows:
        print(f'id:{row.id}, name:{row.name}, age:{row.age}')