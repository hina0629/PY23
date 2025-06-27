# アクセッサ
#   private(外部非公開)アトリビュートに
#   アクセスする専用のメソッド
#   取得するメソッドをゲッター(getter)
#   設定するメソッドをセッター(setter)という

class User:
    def __init__(self):
        self.__id = 40000
        self.__name = 'a'

    # idのゲッター
    def get_id(self):
        return self.__id
    
    # idのセッター
    def set_id(self, value):
        self.__id = value

    # nameのゲッター
    def get_name(self):
        return self.__name
    
    # nameのセッター
    def set_name(self, value):
        self.__name = value

user = User()
print(user.get_id())
user.set_id(49999)
print(user.get_id())

print(user.get_name())
user.set_name('b')
print(user.get_name())

# ゲッターのみ作成することにより、
# 読み取り専用とすることが可能。
# ※セッターのみの作成は無い。

# おまけ
# アクセッサの必要性
# オブジェクト指向のお作法として、
# アトリビュートはprivateにする。
# アクセスするにはアクセッサを用意する。

# アクセッサ、つまりメソッド化することにより、
# 以下の効能が生まれる。
# ①設定値のバリデーション(検証)を組み込むことができる。
#   例) idは負の値を設定できないようにする。
#   def set_id(self, value):
#       if value < 0:
#           self.__id = value
# ②読み取り専用を実現することができる。
# ③内部的にアトリビュート名が後に変更されたとしても、
# 　公開されているのはアクセッサのメソッドのため、
# 　アクセッサ(メソッド)名の変更が掛からなければ、
#   利用サイドのプログラムに影響を及ぼさない。
#   例) __id → __no
#   def get_id(self):
#       return self.__no
# ④user.nama = の罠エラーに引っかからなくなる。

# プロパティ
#  アクセッサをメソッドの形式で呼び出すのではなく、
#  アトリビュートの形式で呼び出せる様にする仕組み。
#  デコレーターを使って、アクセッサを定義することで、
#  簡単にアクセスできる様になる。
#　print(user.id) 
#  user.id = 40000
#  print(user.id)
#  ができるようになる

class User:
    def __init__(self):
        self.__id = 40000
        self.__name = 'a'

    # idのゲッター
    @property
    def id(self):
        return self.__id
    
    # idのセッター
    @id.setter
    def id(self, value):
        self.__id = value

    # nameのゲッター
    @property
    def name(self):
        return self.__name
    
    # nameのセッター
    @name.setter
    def name(self, value):
        self.__name = value

user = User()
print(user.id)
print(user.name)
user.id = 99999
user.name = 'c'
print(user.id)
print(user.name)