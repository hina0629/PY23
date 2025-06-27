# Member
#  物が持っている特性のこと
# 以下2つがある
#  属性 … アトリビュート ※他言語ではフィールドやプロパティともいう
#           そのものが持つ、データのこと。※名詞
#  振る舞い … メソッド
#           そのものが持つ、処理のこと。※動詞
# 属性と振る舞い合わせてmenberという

# 振る舞い(メソッド)
# [定義書式]
# def メソッド名(self [, 引数[, 引数…]]):
# 呼び出されたらhelloと出力
class User:
    # ここで関数を定義すれば、
    # それがメソッド(処理)となる
    def hello(self):    # self は必須
        print('hello')

# メソッド呼び出し
# [呼び出し書式]
# インスタンス.メソッド名()
# JSの例）
# window.alert("error");

# インスタンス化
user = User()

user.hello() # hello 出力
# メソッド(≒関数)呼び出し(正しくはメッセージを投げる)は、「括弧」が必要！
# メソッド呼出し時、定義側のselfは気にしない。(selfは勝手に渡る)

# 引数
class User:
    def hello(self, name):
        print(f'hello{name}')
    # 第1引数のselfはくどいけど必須
    # 第2引数以降に、任意引数を設定していく。

user = User()
user.hello("abc") # helloabc 出力

# 戻り値
class User:
    def hello(self):
        return 'hello!'

user = User()
print(user.hello())
# 因みに、return 省略時はNoneが返却される

# メソッドは複数定義できる
class User:
    def a(self):
        print('a')
    
    def b(self):
        print('b')

user = User()
user.a()
user.b()

# 同一メソッド名は後方優先。
# やらないけど、言語仕様上動く。※スクリプト言語の特性
# 上から順に実行されるから上書きみたいな感じ
class User:
    def a(self):
        print('a')
    
    def a(self):
        print('b')

user = User()
user.a()