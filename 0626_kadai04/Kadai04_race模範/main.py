from slime import Slime

PRINT_INFO = ({'foot_prints':'＝', 'mark':'〇'},
              {'foot_prints':'～', 'mark':'☆'})

# 出走スライムのインスタンス化
slimes = []
for print_info in PRINT_INFO:
    slimes.append(Slime(print_info['foot_prints'], print_info['mark']))

# 出走スライムの出力
print('[List of runners]')
i = 1
for slime in slimes:
    print(f'No.{i}:{slime.mark}')
    i += 1

# Bet処理
while True:
    print('[Bet]')
    try:
        bet_no = int(input('No:'))
    except ValueError:
        # 英字の場合はValueErrorが発生
        continue

    if bet_no <= 0 or len(slimes) < bet_no:
       continue

    break

# レース開始前演出
print('[On your mark]')
import time
time.sleep(1)
for i in range(3, 0, -1):
    print(i, end=' ', flush=True)
    time.sleep(1)

print('Go!')

# レース処理
print('ーーーー５ーーーー10')
is_race_complete = False
winners = []
while(not is_race_complete):
    for slime in slimes:
        slime.run()
        if(10 < slime.pos):
            winners.append(slime.mark)
            is_race_complete = True
    print('ーーーー５ーーーー10')

# レース結果処理
print('Winner!')
for mark in winners:
    print(mark)

print(f'you bet on {slimes[bet_no-1].mark}')
print(f'you {"win!" if slimes[bet_no-1].mark in winners else "lose.."}')
