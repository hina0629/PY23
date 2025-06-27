ex1 = r'xyz'
ex2 = r'(xyz|XYZ)' # re.IGNORECASE でもOK。ただし、今回は関数化してしまったため、正規表現にて対応。
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
ex13 = r'\d{3}'
ex14 = r'\bpython\b'
ex15 = r'(Red|Green|Blue){3}'
ex16 = r'国(?=(営|民))'
ex17 = r'(?<=(ラー|ソー))メン'
ex18 = r'\.(jpg|png|gif|webp)$'
ex19 = r'^[A-Z]{2}-[0-9]{2}[A-Z]-[0-9]{3}$'
ex20 = r'^[ton][hmi]s[0-9]{5}$'


import re
success_count = 0
failure_count = 0
error_set = set()

def success(pattern, str):
    global success_count, failure_count, error_set
    if pattern == '':
        print('**failure** ' + pattern)
        failure_count += 1
        error_set.add(ex_no)
        return

    if(re.search(pattern, str)):
        print('success')
        success_count += 1
    else:
        print('**failure** ' + pattern)
        failure_count += 1
        error_set.add(ex_no)

def failure(pattern, str):
    global success_count, failure_count, error_set
    if pattern == '':
        print('**failure** ' + pattern)
        failure_count += 1
        error_set.add(ex_no)
        return

    if(re.search(pattern, str)):
        print('**failure** ' + pattern)
        failure_count += 1
        error_set.add(ex_no)
    else:
        print('success')
        success_count += 1

def equals(str1, str2):
    global success_count, failure_count, error_set

    if(str1 == str2):
        print('success')
        success_count += 1
    else:
        print('**equals failure** ' + str1 + ' ' + str2)
        failure_count += 1
        error_set.add(ex_no)

# テストコード
ex_no = 1
print(f'【ex{ex_no}】')
print(' [match]')
success(ex1, 'xyz')
print(' [miss match]')
failure(ex1, '')
failure(ex1, 'abc')

ex_no = 2
print(f'【ex{ex_no}】')
print(' [match]')
success(ex2, 'xyz')
success(ex2, 'XYZ')
print(' [miss match]')
failure(ex2, '')
failure(ex2, 'abc')

ex_no = 3
print(f'【ex{ex_no}】')
print(' [match]')
success(ex3, 'xyz')
success(ex3, 'xyza')
print(' [miss match]')
failure(ex3, '')
failure(ex3, 'xy')
failure(ex3, 'axyz')

ex_no = 4
print(f'【ex{ex_no}】')
print(' [match]')
success(ex4, 'xyz')
success(ex4, 'axyz')
print(' [miss match]')
failure(ex4, '')
failure(ex4, 'xy')
failure(ex4, 'xyza')

ex_no = 5
print(f'【ex{ex_no}】')
print(' [match]')
success(ex5, 'xyz')
print(' [miss match]')
failure(ex5, '')
failure(ex5, 'xy')
failure(ex5, 'axyz')
failure(ex5, 'xyza')

ex_no = 6
print(f'【ex{ex_no}】')
print(' [match]')
success(ex6, 'xyz')
success(ex6, 'xaz')
success(ex6, 'x1z')
print(' [miss match]')
failure(ex6, '')
failure(ex6, 'xy')

ex_no = 7
print(f'【ex{ex_no}】')
print(' [match]')
success(ex7, 'axyza')
print(' [miss match]')
failure(ex7, '')
failure(ex7, 'axyz')
failure(ex7, 'xyza')

ex_no = 8
print(f'【ex{ex_no}】')
print(' [match]')
success(ex8, 'xxxxxyz')
print(' [miss match]')
failure(ex8, '')
failure(ex8, 'xxxxyz')
failure(ex8, 'xxxxxy')

ex_no = 9
print(f'【ex{ex_no}】')
print(' [match]')
success(ex9, 'xxxxxyz')
success(ex9, 'xxxxxxxxyz')
print(' [miss match]')
failure(ex9, '')
failure(ex9, 'xxxxyz')
failure(ex9, 'axxxxxyz')
failure(ex9, 'xxxxxxxxxyz')

ex_no = 10
print(f'【ex{ex_no}】')
print(' [match]')
success(ex10, 'xyx')
success(ex10, 'xyy')
success(ex10, 'xyz')
print(' [miss match]')
failure(ex10, '')
failure(ex10, 'xy')
failure(ex10, 'xya')

ex_no = 11
print(f'【ex{ex_no}】')
print(' [match]')
success(ex11, 'a')
success(ex11, 'm')
success(ex11, 'z')
print(' [miss match]')
failure(ex11, '')
failure(ex11, 'A')
failure(ex11, 'ａ')

ex_no = 12
print(f'【ex{ex_no}】')
print(' [match]')
success(ex12, 'aaa')
success(ex12, 'AAA')
success(ex12, '000')
success(ex12, 'A0z')
success(ex12, '-A0z')
success(ex12, 'A0z-')
print(' [miss match]')
failure(ex12, '')
failure(ex12, 'aa')
failure(ex12, '---')
failure(ex12, 'ａａａ')
failure(ex12, '９９９')
failure(ex12, 'aa')

ex_no = 13
print(f'【ex{ex_no}】')
print(' [match]')
success(ex13, '000')
success(ex13, '０００')
print(' [miss match]')
failure(ex13, '')
failure(ex13, '00')

ex_no = 14
print(f'【ex{ex_no}】')
print(' [match]')
success(ex14, 'python')
success(ex14, ' python')
success(ex14, 'python ')
success(ex14, ' python ')
print(' [miss match]')
failure(ex14, '')
failure(ex14, 'apython')
failure(ex14, 'pythona')
failure(ex14, 'ｐｙｔｈｏｎ')

ex_no = 15
print(f'【ex{ex_no}】')
print(' [match]')
success(ex15, 'RedGreenBlue')
success(ex15, 'GreenBlueRed')
success(ex15, 'BlueRedGreen')
success(ex15, 'RedRedRed')
success(ex15, 'GreenGreenGreen')
success(ex15, 'BlueBlueBlue')
success(ex15, 'RedRedBlue')
print(' [miss match]')
failure(ex15, '')
failure(ex15, 'RGB')
failure(ex15, 'Red')
failure(ex15, 'RedRed')
failure(ex15, 'RedGrean')
failure(ex15, 'ＲｅｄＧｒｅｅｎＢｌｕｅ')

ex_no = 16
print(f'【ex{ex_no}】')
print(' [match]')
success(ex16, '国営')
success(ex16, '国民')
print(' [miss match]')
failure(ex16, '')
failure(ex16, '国')
failure(ex16, '国家')
equals(re.sub(ex16, '市', '国営'), '市営')
equals(re.sub(ex16, '市', '国民'), '市民')
equals(re.sub(ex16, '市', '国'), '国')
equals(re.sub(ex16, '国', '市営'), '市営') # 市営は置換対象ではない。

ex_no = 17
print(f'【ex{ex_no}】')
print(' [match]')
success(ex17, 'ラーメン')
success(ex17, 'ソーメン')
print(' [miss match]')
failure(ex17, '')
failure(ex17, 'メン')
failure(ex17, 'タンメン')
failure(ex17, 'サンマーメン')
equals(re.sub(ex17, '麺', 'ラーメン'), 'ラー麺')
equals(re.sub(ex17, '麺', 'ソーメン'), 'ソー麺')
equals(re.sub(ex17, '麺', 'アーメン'), 'アーメン')
equals(re.sub(ex17, '麺', 'メン'), 'メン')

ex_no = 18
print(f'【ex{ex_no}】')
print(' [match]')
success(ex18, '.jpg')
success(ex18, '.png')
success(ex18, '.gif')
success(ex18, '.webp')
print(' [miss match]')
failure(ex18, '')
failure(ex18, 'jpg')
failure(ex18, '.jpg.')
failure(ex18, '.jpeg')
failure(ex18, '.jpga')
failure(ex18, '_jpg')
failure(ex18, '．jpg')
failure(ex18, '.jpｇ')

ex_no = 19
print(f'【ex{ex_no}】')
print(' [match]')
success(ex19, 'IH-12A-000')
success(ex19, 'AT-11B-999')
print(' [miss match]')
failure(ex19, '')
failure(ex19, 'IH12A000')
failure(ex19, 'IH-12A000')
failure(ex19, 'IH12A-000')
failure(ex19, ' IH-12A-000')
failure(ex19, 'IH-12A-000 ')
failure(ex19, '11-12A-000')
failure(ex19, 'IH-AAA-000')
failure(ex19, 'IH-123-000')
failure(ex19, 'IH-12A-aaa')
failure(ex19, 'ih-12A-000')
failure(ex19, 'IH-12a-000')
failure(ex19, 'ＩH-12A-000')
failure(ex19, 'IＨ-12A-000')
failure(ex19, 'IH-１2A-000')
failure(ex19, 'IH-12Ａ-000')
failure(ex19, 'IH-12A-00０')

ex_no = 20
print(f'【ex{ex_no}】')
print(' [match]')
success(ex20, 'ths00000')
success(ex20, 'tms00000')
success(ex20, 'tis00000')
success(ex20, 'ohs00000')
success(ex20, 'oms00000')
success(ex20, 'ois00000')
success(ex20, 'nhs00000')
success(ex20, 'nms00000')
success(ex20, 'nis00000')
print(' [miss match]')
failure(ex20, '')
failure(ex20, 'hs00000')
failure(ex20, 'ts00000')
failure(ex20, 'th00000')
failure(ex20, 'ths0000')
failure(ex20, 'ths000000')
failure(ex20, 'ahs00000')
failure(ex20, 'tas00000')
failure(ex20, 'tha00000')
failure(ex20, 'thsaaaaa')
failure(ex20, 'aths00000')
failure(ex20, 'Ths00000')
failure(ex20, 'ｔhs00000')
failure(ex20, 'tHs00000')
failure(ex20, 'tｈs00000')
failure(ex20, 'tHS00000')
failure(ex20, 'tHｓ00000')
failure(ex20, 'ths0000０')

print('【Summary】')
print(f'Total tests run: {success_count + failure_count}')
print(f'Tests passed: {success_count}')
print(f'Tests failed: {failure_count}')
print(f'Success rate: {round(success_count / (success_count + failure_count) * 100, 2)}%')
print(f'Failure rate: {round(failure_count / (success_count + failure_count) * 100, 2)}%')

if error_set:
	print('Failure ex number', sorted(error_set))

print(f'Overall status: {"FAIL" if error_set else "PASS"}')
