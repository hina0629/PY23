# デコレーター
#   関数(メソッド)の前後に
#   任意処理を追加すること
#   ができる

# [定義例]※覚えなくてOK
def my_decorator(funk):
    def wrapper(*args, **kwargs):
        # 前処理
        print(0)

        # 実関数呼び出し
        result = funk(*args, **kwargs)

        # 後処理
        print(2)
        return result
    return wrapper

# [利用書式]
# @デコレーター名
# def 関数名():

@my_decorator
def a():
    print(1)

a()
