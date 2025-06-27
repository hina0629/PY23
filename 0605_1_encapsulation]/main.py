# カプセル化
#  オブジェクト指向３大要素の内の１つ。
#  次の２つの意味合いがある。
# １．属性と振る舞いを、一つの
# 　まとまりとして管理することができる。
# ２．メンバ(アトリビュート&メソッド)を隠蔽する。

# [隠蔽書式]
# 各々の定義名称の開始を、
# アンダーバー２つとする
class User:
    def __init__(self):
        self.id = 40000
        self.name = 'aaa'
        self.__privateAttribute = 111
        self.__bbb = 222
    
    def a(self):
        # 隠蔽されていても、
        # 自身(self)であれば、
        # アクセスできる
        print(self.__privateAttribute)
        print(self.__bbb)
        self.__b()

    def __b(self):
        print('private method b')

user = User()
print(user.id)
print(user.name)
# print(user.__privateAttribute) 見えない(隠蔽されてる)
# print(user.__bbb) 見えない(隠蔽されてる)

user.a()
# user.__b() 見えない

# おまけ。
# 一般的な言語には情報の公開範囲を制御するアクセス修飾子なるものが存在する。
# 例）public…外部公開 private…外部非公開
# ※pythonには無い。

# おまけ
# Double underscoreを略してDunder(ダンダー)という。

# ポイント
# 　極力隠蔽し、不必要な情報を外部に公開しないこと。
# 　　→保守性向上