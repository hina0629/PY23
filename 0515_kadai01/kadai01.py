import re

# Ex1)
# xyz

# Ex2)
# xyz
# XYZ
# ※re.IGNORECASE　ではなく、正規表現にて対応してください。

# Ex3)
# xyz　※先頭がxyz(以後"先頭"と記載(末尾も同様))

# Ex4)
# xyz　※末尾

# Ex5)
# xyz　※先頭かつ末尾

# Ex6)
# xyz  ※yは、任意1文字（y以外でもOK）とする。

# Ex7)
# xyz の前後に任意1文字が存在すること。

# Ex8)
# xxxxxyz　※繰り返し表現を用いること。

# Ex9)
# xxxxxyz		※先頭
# xxxxxxyz	※先頭
# xxxxxxxyz	※先頭
# xxxxxxxxyz	※先頭
# ※以下２つはmiss match
# xxxxyz
# xxxxxxxxxyz

# Ex10)
# xyx
# xyy
# xyz

# Ex11)
# x　※xは、任意の英字、かつ小文字とする。

# Ex12)
# XXX　※Xは、任意の英数字。なお、大文字小文字は両方許容とする。

# Ex13)
# 123     ※任意の数値3桁
# １２３  ※全角も許容

# Ex14)
# python　※pythonという"単語"が含まれていること。（apythonはミスマッチ）

# Ex15)
# RedGreenBlue
# GreenBlueRed
# BlueRedGreen
# RedRedRed
# GreenGreenGreen
# BlueBlueBlue
# RedRedGreen　　※等々、RGBの組み合わせ

# Ex16)
# 国営
# 国民
# ※"国"単体はミスマッチ
# また、"国"を"市"に置換することを想定。

# Ex17)
# ラーメン
# ソーメン
# ※"メン"単体はミスマッチ
# また、Ex16同様、"メン"を"麺"に置換することを想定。

# Ex18)拡張子
# ファイル名をチェックする。というシナリオで、以下４種の拡張子のみマッチする。
# .jpg
# .png
# .gif
# .webp

# Ex19)クラス記号 IH-12B-111
# 固定10桁。※10桁以外はミスマッチ
# 先頭２桁は任意英字　※大文字限定
# 次の１桁は固定ハイフン
# 次の２桁は数値２桁
# 次の１桁は任意英字　※大文字限定
# 次の１桁は固定ハイフン
# 次の３桁は任意数値

# Ex20)種別＋学籍番号 ※ths00000
# 固定8桁。※8桁以外はミスマッチ
# 種別は、3桁で、以下のルール
# 1桁目…地域種別(t/o/n)　※t…東京,o…大阪,n…名古屋
# 2桁目…校種(h/m/i)　※h…HAL,m…MODE,i…医校
# 3桁目…固定s　※s…student

ex1 = r'[x-z]'
ex2 = r'[x-zX-Z]'
ex3 = r'^xyz'
ex4 = r'xyz$'
ex5 = r'^xyz$'
ex6 = r'x.z'
ex7 = r'.xyz.'
ex8 = r'x{5}yz'
ex9 = r'^x{5,8}yz'
ex10 = r'xy[xyz]'
ex11 = r'[a-z]'
ex12 = r'[a-zA-Z0-9]{3}'
ex13 = r'[0-9０-９]{3}'
ex14 = r'\bpython\b'
ex15 = r'(Red|Green|Blue){3}'
ex16 = r'国(?=(営|民))'
ex17 = r'(?<=(ラー|ソー))メン'
ex18 = r'^\.(jpg|png|gif|webp)$'
ex19 = r'^[A-Z]{2}-[0-9]{2}[A-Z]-[0-9]{3}$'
ex20 = r'^[ton][hmi]s[0-9]{5}$'

print(re.search(ex17, 'たんたんメン'))
print(re.sub(ex17, '麺', 'ラーメン'))