# 0717_inheritance
# インヘリタンス（継承）
# オブジェクト指向３大要素の２つめ（１つめはカプセル化）
# あるクラスの性質を別のクラスに
# 引き継げる仕組み。
# 一言でいうと、コピペはやめて、
# 差分だけ作ろうよ！

# [継承書式]
# class クラス名(継承元クラス名):
class A:
    def a(self):
        print('a')

# Aの性質（メンバ）を継承したBの定義
class B(A):
    pass

b = B()
b.a()

# Aクラスの性質をBクラスに
# 引き継いで（継承して）いるので、
# Bクラスの持ち物に a メソッドがある

print()

# アトリビュートも引き継がれる。
class A:
    def __init__(self):
        self.id = 0

class B(A):
    pass

b = B()
print(b.id)

print()

# [用語]
# 継承元（A）を特に
# ・スパークラス
# ・上位クラス
# ・親クラス
# 継承先（B）を特に
# ・サブクラス
# ・下位クラス
# ・子クラス
# と言う。

# 基本、親は１つで子は複数の関係
class A:
    def a(self):
        print('a')

class B(A):
    def b(self):
        print('b')

class C(A):
    def c(self):
        print('c')

b = B()
b.a()
b.b()

c = C()
c.a()
c.c()

print()

# オーバーライド
# 　上書き。スーパークラスのメソッドを
# 　サブクラスで上書きすることができる。
# 　※正しくは「奪い」
class A:
    def a(self):
        print('a')

class B(A):
    pass

b = B()
b.a()

class B(A):
    # 同一メソッドを別途定義すれば、
    # オーバーライドとなる。
    def a(self):
        print('b')

b = B()
b.a()

print()

# サブクラスから、
# スーパークラスのメソッドを
# 呼び出せる。
# [書式]
# super().メソッド名()
class B(A):
    def b(self):
        super().a()

        # self.でもいける
        self.a()

b = B()
b.b()

# super 実用例１）
class B(A):
    def a(self):
        super().a()
        print('b')

b = B()
b.a()

# super 実用例２）
class A:
    def __init__(self, id):
        self.id = id

class B(A):
    def __init__(self, name):
        self.name = name

b = B('aaa')
print(b.name)
# print(b.id) コンストラクタがオーバーライドされたのでidがない。

class B(A):
    def __init__(self, id, name):
        self.id = id # 親の処理のコピー → 悪手
        self.name = name

b = B(0, 'bbb')
print(b.id)
print(b.name)

# ↑ で、要件は満たされるけど、
# self.id = id は冗長。コピーは嫌。
# また、たくさんアトリビュートが
# あった場合に面倒
# → super を使う
class B(A):
    def __init__(self, id, name):
        # 親のコンストラクタ呼び出し
        super().__init__(id)
        self.name = name

b = B(0, 'bbb')
print(b.id)
print(b.name)

print()

# 継承は代々引き継げる
class A:
    def a(self):
        print(1)

class B(A):
    def b(self):
        print(2)

class C(B):
    def c(self):
        print(3)

c = C()
c.a()
c.b()
c.c()

print()

# 多重継承が可能
# 　→ 複数の親OK
class A:
    def a(self):
        print(1)

class B:
    def b(self):
        print(2)

# 継承元として、
# カンマで複数指定が可能
class C(A, B):
    def c(self):
        print(3)

c = C()
c.a()
c.b()
c.c()