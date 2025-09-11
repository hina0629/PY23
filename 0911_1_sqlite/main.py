# 0911_sqlite
# SQLite…簡易RDB。
# Android,MacOS,Pythonでは、
# デフォルトで組み込まれています。
import sqlite3

# DB接続
con = sqlite3.connect('0911_1_sqlite\\sample.db')

# カーソル取得
cur = con.cursor()

# \ → 改行コードを消す
# IF NOT EXISTS → もしあったら作らない（なかったら作る）
sql = '''\
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name STRING
)\
'''
# SQL分の実行
cur.execute(sql)

# commitで確定
con.commit()

# insert
sql = "INSERT INTO user(name) VALUES('a')"
# sql = 'INSERT INTO user(name) VALUES(\'a\')' でもいい

# SQL分の実行
cur.execute(sql)

# commitで確定
# con.commit()

# rollbackでキャンセル
con.rollback()

# select は、execute後、
# curを用いて、結果を取得する。
sql = 'SELECT * FROM user'

# SQL分の実行
cur.execute(sql)

# 抽出系(SELECT)において、
# commitとrollbackは不要。

# forで引っこ抜けた行数分
# 繰り返す
# for row in cur:
#     print(row)

# やってみよう！
# 以下のフォーマットで出力
# ID = 1, Name = a
# ID = 2, Name = a
for row in cur:
    print(f"ID = {row[0]}, Name = {row[1]}")

# sample.dbを普通に開くと文字化けしているのはバイナリーファイルだから
# DB切断
con.close()