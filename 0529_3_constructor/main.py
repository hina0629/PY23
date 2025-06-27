# construct 建築する
# コンストラクタ
#  インスタンス化の際に動作するメソッド
#  初期化の用途にて利用される
# [定義書式]
# def __init__(self):
# Initialize 初期化する
class User:
    def __init__(self):
        print('コンストラクタ')

# このタイミングで動作するから user.__init__() いらない
uesr = User()
        # ↑↑↑↑↑これでコンストラクタが動作する

# コンストラクタ & 引数
#  コンストラクタはメソッドなので、引数を渡せる
class User:
    def __init__(self, a):
        print(a)

uesr = User(123)

# コンストラクタにてreturnは記述しない。
class User:
    def __init__(self):
        # return 1 → これはだめ
        return # あまりないけど、あるとしてもこれくらい

uesr = User()