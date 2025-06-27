# import されると、モジュールのプログラム全てが実行される
import my_module
import my_module # ただし、最初の１回のみ

# インポートされたモジュールすべてのメンバ（変数／関数／クラス）が使える
print(my_module.a)
my_module.my_func()

from my_module import my_func
# my_module. をつけなくても使えるようになる
my_func()

# from を使っても同じようにすべてが実行される
from my_module2 import my_func
my_func()

# 変数も読み込める
from my_module2 import a
print(a)