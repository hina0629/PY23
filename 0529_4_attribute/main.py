#  属性 … アトリビュート ※他言語ではフィールドやプロパティともいう
#           そのものが持つ、データのこと。※名詞
# [定義書式]
# def __init__(self):
#     コンストラクタで、selfを用いて定義していく。
#     self.アトリビュート名1 = 初期値
#     self.アトリビュート名2 = 初期値 ※必要数分記述OK

# self … 自分。自身。自己。
# ということで、インスタンス化によって
# 出来上がったもの。の、その物”自身”を表すのがself

class User:
    def __init__(self):
        self.id = 0
        self.name = 'no name'
        self.address = ''
        tel = '090' # self がないと、ローカル変数 
        # ローカル変数 → そのブロックの中だけ有効

# アトリビュート値の操作
# [利用書式]
# インスタンス.アトリビュート名
# ()がついていたら処理(メソッド)を探しに行く
# ()ついてなかったらデータ(アトリビュート)を探しに行く
user = User()
# ↓ 上書き
user.id = 123
user.address = '東京'
# 123 no name 東京 と出力
print(user.id, user.name, user.address)
# print(user.tel) ← 無い

# アトリビュートはコンストラクタで定義が基本
# でも、言語仕様的にはコンストラクタでなくても可
# （保守性上、やらないほうがいい）
class User:
    def a(self):
        self.aaa = 0
        self.bbb = 0     

user = User()
# print(user.aaa) → これできない
user.a()    # aメソッドを呼んで、始めて
print(user.aaa) # ← これが動く（やらないほうがいい。__init__でやるべき）

# また、外部からの追加も可（やらないほうがいい）
user.ccc = 999
print(user.ccc)
# aaa を変えたいのにスペルミスで aab にしたら aab というアトリビュートが作られちゃう
user.aab = 'ddd'
print(user.aaa)

# -------------------------------------------------------------------------------------- #
#                                          0605                                          #
# -------------------------------------------------------------------------------------- #

print("")

# アトリビュートはdelで削除可能
del user.aab
# print(user.aab)

# コンストラクタ引数にて初期化
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

user1 = User(100, 'aaa')
user2 = User(200, 'bbb')

# アトリビュートは、インスタンスごとに保存される
print(user1.id)
print(user1.name)
print(user2.id)
print(user2.name)

# 保存されてるデータ(アトリビュート)は、自分の持ち物なので、自分で使える
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def print_name(self):
        print(f'My name is {self.name}')

user1 = User(100, 'aaa')
user1.print_name()

# アトリビュートの利用指針
#   その物が保持し続けるべきデータがある時のみ、アトリビュートとする
#   ※基本はローカル変数