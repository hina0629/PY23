# 正規表現（regular expressions）
#  文字列をパターンにて表現するもの
#  そのパターンにマッチしているか否かの判定が行える
# 入力チェックとかに使える
import re

# パターンの記述には、raw string が推奨
# ※正規表現にて「\」が特殊文字のため、pythonと喧嘩しないように
# \n 改行
pattern = 'これは\nraw string'
print(pattern)

# r をつけると特殊文字じゃなくなって改行されなくなる
pattern = r'これは\nraw string'
print(pattern)

pattern = r'a'
str = 'a'

# マッチ時は、matchオブジェクトが返却される
print(re.match(pattern, str))

# ミスマッチ時は、Noneオブジェクトが返却される
str = 'b'
print(re.match(pattern, str))

# パターンにマッチするか否かはifで判定
# ・matchオブジェクト → true判定
# ・Noneオブジェクト → false判定
if re.match(r'a', 'a'):
    print('match')
else:
    print('miss match')

if re.match(r'a', 'b'):
    print('match')
else:
    print('miss match')

# match は先頭がマッチするかを判定する
print(re.match(r'a', 'abc'))
print(re.match(r'b', 'abc')) # miss
print(re.match(r'c', 'abc')) # miss

# search は先頭縛りなし
print(re.search(r'a', 'abc'))
print(re.search(r'b', 'abc'))
print(re.search(r'c', 'abc'))

# 大文字、小文字既定では区別される
print(re.search(r'abc', 'ABC')) # miss
print(re.search(r'abc', 'ABC', re.IGNORECASE)) # これで大文字小文字が区別されなくなる

# メタ文字
#  正規表現で特殊な意味を持つ文字
#  ^ …先頭
#  $ …末尾
#  . …任意の１文字
print('^$.')
print(re.search(r'^abc', 'abc')) # 先頭からabcであること
print(re.search(r'^abc', 'aabc')) # miss
print(re.search(r'^.abc', 'aabc')) # 任意１文字があった後にabcであること
print(re.search(r'^.abc', 'babc'))
print(re.search(r'^.abc', 'babcd')) # 後ろは見ていないからマッチ
print(re.search(r'^.abc', 'abcd')) # miss

print(re.search(r'abc$', 'abc')) # abcで終わっていること
print(re.search(r'abc$', 'xxxabc'))
print(re.search(r'...abc$', 'xxxabc'))
print(re.search(r'...abc$', 'xxxxabc'))
print(re.search(r'...abc$', 'xxabc')) # miss

print(re.search(r'^...abc$', 'xxxxabc')) # miss

# 繰り返し指定のメタ文字
#  「直前の文字が」何回繰り返すかを指定することができる
# + … 1回以上
# * … 0回以上
# ? … 0回か、1回
# {m} … m回
# {m,n} … m回以上、n回以下
# {m,} … m回以上
# {,n} … n回以下
print('+*?{m}{m,n}{m,}{,n}')

print(re.search(r'a+bc', 'abc')) # aが1文字以上のあとにbc
print(re.search(r'a+bc', 'aabc'))
print(re.search(r'a+bc', 'aaabc'))
print(re.search(r'a+bc', 'bc')) # miss

print(re.search(r'a*bc', 'abc')) # aが0文字以上のあとにbc
print(re.search(r'a*bc', 'aabc'))
print(re.search(r'a*bc', 'bc'))
print(re.search(r'a*bc', 'xbc'))

print(re.search(r'a?bc', 'abc')) # aがあるかないかのあとにbc
print(re.search(r'a?bc', 'bc'))
print(re.search(r'a?bc', 'aabc'))
print(re.search(r'^a?bc', 'aabc')) # miss

print(re.search(r'a{3}bc', 'aaabc')) # aを3回のあとにbc
print(re.search(r'a{3}bc', 'aabc')) # miss
print(re.search(r'a{3}bc', 'aaaabc'))
print(re.search(r'^a{3}bc', 'aaaabc')) # miss

print(re.search(r'a{2,3}bc', 'aabc')) # aを2回以上3回以下のあとにbc
print(re.search(r'a{2,3}bc', 'aaabc'))
print(re.search(r'a{2,3}bc', 'abc')) # miss
print(re.search(r'a{2,3}bc', 'aaaabc'))
print(re.search(r'^a{2,3}bc', 'aaaabc')) # miss

print(re.search(r'a{2,}bc', 'aabc')) # aを2回以上のあとにbc
print(re.search(r'a{2,}bc', 'aaabc'))
print(re.search(r'a{2,}bc', 'abc')) # miss
print(re.search(r'^a{2,}bc', 'aaabc'))

print(re.search(r'a{,2}bc', 'bc')) # aを2回以下のあとにbc
print(re.search(r'a{,2}bc', 'abc'))
print(re.search(r'a{,2}bc', 'aabc'))
print(re.search(r'a{,2}bc', 'aaabc'))
print(re.search(r'^a{,2}bc', 'aaabc')) # miss


# -------------------------------------------------------------------------------------------------------- #
#                                                   0508                                                   #
# -------------------------------------------------------------------------------------------------------- #


# 文字集合
# [] … いずれか
print("[]")
print(re.search(r'[abc]bc', 'abc'))
print(re.search(r'[abc]bc', 'bbc'))
print(re.search(r'[abc]bc', 'cbc'))
print(re.search(r'[abc]bc', 'dbc')) # miss

print(re.search(r'[0123456789]', '5')) # 数値であること
print(re.search(r'[0123456789]', 'b')) # miss
print(re.search(r'[0-9]', '5')) # []内の「-」は範囲を示す特殊文字
print(re.search(r'[a-z]', 'x'))
print(re.search(r'[a-z]', '5')) # miss
print(re.search(r'[a-z]', 'X')) # miss
print(re.search(r'[a-zA-Z]', 'x'))
print(re.search(r'[a-zA-Z]', 'X'))
print(re.search(r'[あ-う]', 'あ'))
print(re.search(r'[あ-う]', 'か')) # miss

print(re.search(r'\d', '5')) # 数値（[0-9０-９]と一緒）
print(re.search(r'\d', '５'))
print(re.search(r'\d', 'a')) # miss

print(re.search(r'\D', 'a')) # 数値以外　
print(re.search(r'\D', '5')) # miss
print(re.search(r'\D', '@'))

print(re.search(r'\s', ' ')) # 空白文字
print(re.search(r'\S', 'a')) # 空白文字以外
print(re.search(r'\S', '5'))
print(re.search(r'\S', '　')) # miss

print(re.search(r'\bis\b', 'this is')) # is という単語を探す。「\b」で単語の区切り
print(re.search(r'\bis\b', 'this')) # miss

# 単語選択
# (abc|def) … abcかdef
print("(abc|def)")
print(re.search(r'(color|colour)', 'color'))
print(re.search(r'(color|colour)', 'colour'))

# グループ
# ()で括ってグループ化することにより、.groupや.groupsで取得可能
print("group/groups")
match = re.search(r'(\d{4})/(\d{1,2})/(\d{1,2})', '2025/5/8')
print(match)
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))
print(match.groups())

# 打消しは「\」
print("打消し")
# 特殊文字としての意味を打ち消す
print(re.search(r'\^', '^')) # 「^」が先頭という意味じゃなくなる
print(re.search(r'\$', '$')) 
print(re.search(r'\.', '.'))
print(re.search(r'\+', '+'))
print(re.search(r'\*', '*'))
print(re.search(r'\?', '?'))
print(re.search(r'\{', '{'))
print(re.search(r'\(', '('))

print(re.search(r'[0\-9]', '-')) # 「0」か「-」か「9」
print(re.search(r'[0\-9]', '5')) # miss
print("\\") # 「\」を出力したいときは「\\」
print(re.search(r'\\', '\\'))

# 最短一致
# +? … 手前の文字が1回以上（最短）
# *? … 手前の文字が0回以上（最短）
print("+?*?")
print(re.search(r'.+', 'abc')) # 0~3で最長
print(re.search(r'.+?', 'abc')) # 0~1で最短
print(re.search(r'.*', 'abc')) # 0~3で最長
print(re.search(r'.*?', 'abc')) # 0~0で最短

print(re.search(r'aaa.*ccc', 'aaabbbcccdddccc')) # 0~15で最長
print(re.search(r'aaa.*?ccc', 'aaabbbcccdddccc')) # 0~9で最短

# マッチオブジェクト
print("Match Object")
match = re.search(r'ccc', 'abccc')
print(match.span()) # (2,5) どの区間でマッチしたか
print(match.start()) # 2
print(match.end()) # 5

# searchは複数箇所マッチしない。
match = re.search(r'ccc', 'abcccabccc')
print(match.span())
# →最初に見つかった場所だけ（複数マッチせず）

# 複数マッチ（文字列リスト取得）はfindall
print("findall")
# マッチした文字列のリストになる
match_str_list = re.findall(r'ccc', 'abcccabccc')
print(match_str_list)

# 複数マッチ（Matchオブジェクトイテレータ取得）はfinditer
# ※イテレーター…forで回せる
print("finditer")
match_iter = re.finditer(r'ccc', 'abcccabccc')
for match in match_iter:
    print(match.span())

# かぶりは。。。
print()
match_iter = re.finditer(r'ccc', 'abccccc')
for match in match_iter:
    print(match.span())

print()
match_iter = re.finditer(r'ccc', 'abcccccc')
for match in match_iter:
    print(match.span())
# →かぶりは無し

# マッチした箇所で区切ってリスト化
print("split")
print(re.split(r',', 'aaa,bbb,ccc'))

# マッチした個所を置換
print("sub")
print(re.sub(r',', ':', 'aaa,bbb,ccc'))

# 先読み／後読み
# (?= ) … 先読み
# (?! ) … 否定先読み
# (?<= ) … 後読み
# (?<! ) … 否定後読み
# 先頭を表す^や、末尾を表す$と同じ扱い
# パターンマッチング（検査）はするが、結果のマッチオブジェクトには含まれない

# 先読み（右側をチェック）
print(re.search(r'python(?=flask)', 'pythonflask')) # 0~6(python)でマッチ
print(re.search(r'python(?=flask)', 'python')) # miss
# → 右側に flask がある python だけをマッチ

# 否定先読み（右側をチェック）
# 否定だから先読みの逆
print(re.search(r'python(?!flask)', 'pythonflask')) # miss
print(re.search(r'python(?!flask)', 'python')) # 0~6でマッチ
# → 右側に flask がない python だけをマッチ


# -------------------------------------------------------------------------------------------------------- #
#                                                   0515                                                   #
# -------------------------------------------------------------------------------------------------------- #


# 後読み（左側をチェック）
print()
print(re.search(r'(?<=python)flask', 'pythonflask')) # flask を探す。ただし左に python があること。6~11でマッチ
print(re.search(r'(?<=python)flask', 'flask')) # miss
# → 左側に python がある flask だけをマッチ

# 否定後読み（左側をチェック）
print()
print(re.search(r'(?<!python)flask', 'pythonflask')) # miss
print(re.search(r'(?<!python)flask', 'flask')) # 0~5でマッチ
# → 左側に python がない flask だけをマッチ

# 先読み/後読み + グループ
print()
print(re.search(r'新宿(?=(駅|区))', '新宿区'))
print(re.search(r'新宿(?=(駅|区))', '新宿駅'))
print(re.search(r'新宿(?=(駅|区))', '新宿店')) # miss
print(re.search(r'新宿(?=(駅|区))', '新宿')) # miss
print(re.search(r'新宿(?=(駅|御苑))', '新宿駅')) # 先読みの可変長はOK
print(re.search(r'新宿(?=(駅|御苑))', '新宿御苑')) # 先読みの可変長はOK
print(re.search(r'(?<=(西|東))新宿', '西新宿'))
print(re.search(r'(?<=(西|東))新宿', '東新宿'))
# print(re.search(r'(?<=(西|南東))新宿', '東新宿')) → 後読みの可変長はNG

# 先読み/後読みの活用例　その１
print()
print(re.sub(r'日本(?=語)', '国', '日本では日本語と英語を勉強する。'))

# 先読み/後読みの活用例　その２（タグ取得）
print()
print(re.findall(r'(?<=#)\S+', '#aaa #bbb #ccc')) # 左に # があって空白以外が1文字以上

# 先読みの手前（左）記載
print()
print(re.search(r'(?=pythonflask)python', 'pythonflask'))
print(re.search(r'(?=pythonflask)python', 'flask')) # miss
print(re.search(r'(?=pythonflask)a','pythonflaska')) # miss
# →あらかじめ、先読み指定パターンが存在することをチェックし、
#  存在した場合、右側のパターンを、存在した場所の先頭からチェックする。
# 後読みの場合、存在した場所の"先頭から"、にならない。
# 存在した場所より"右側から"、となる。
print(re.search(r'(?<=pythonflask)a', 'pythonflaska'))

# 先読み/後読みの活用例　その３
# 任意条件（今回は３文字）に加え、英大文字が含まれていること。
print()
print(re.search(r'(?=.*?[A-Z]).{3}', 'Abc')) # 任意の文字が0~あった後に英大文字が最短で出る → 巻き戻って任意の文字が３文字
print(re.search(r'(?=.*?[A-Z]).{3}', 'aBc'))
print(re.search(r'(?=.*?[A-Z]).{3}', 'abC'))
print(re.search(r'(?=.*?[A-Z]).{3}', 'Abcd'))
print(re.search(r'(?=.*?[A-Z]).{3}', 'ABC'))
print(re.search(r'(?=.*?[A-Z]).{3}', 'abc')) # miss
print(re.search(r'(?=.*?[A-Z]).{3}', 'aB')) # miss

# 先読み/後読みの活用例　その４
# 任意条件（今回は３文字）に加え、英大文字および小文字が含まれていること。
print()
pattern = r'(?=.*?[a-z])(?=.*?[A-Z]).{3}'
print(re.search(pattern, 'Abc'))
print(re.search(pattern, 'ABC')) # miss
print(re.search(pattern, '000')) # miss
# Point!
# 先読みが連続した場合、AND条件になる

# 先読み/後読みの活用例　その５
# パスワードは半角英字及び記号（_または.）にて構成され、少なくとも５桁必要。
# また、大文字、小文字、数字、記号（_.）のすべてを含むこと。
print()
pattern = r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[_.])[0-9a-zA-Z_.]{5,}$'
# pattern = r'(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[_.]).{5,}'
# → ^ と $ がなく、 {5,} の前が . だと任意の文字だから大文字、小文字、数字、記号（_.）以外もマッチしてしまう
print(re.search(pattern, 'aA0_a'))
print(re.search(pattern, 'aA0.a'))
print(re.search(pattern, 'aA0.aa'))
print(re.search(pattern, 'aA0.')) # miss 5文字以上じゃない
print(re.search(pattern, 'aa0.a')) # miss 大文字がない
print(re.search(pattern, 'AA0.A')) # miss 小文字がない
print(re.search(pattern, 'aAa.a')) # miss 数字がない
print(re.search(pattern, 'aA0aa')) # miss 記号がない
print(re.search(pattern, 'aA0.a@')) # miss 使えない文字を使っている
