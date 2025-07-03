import slime
import time

# main_slime = slime.Slime("＝", "〇", 1)

# while main_slime.position < 11:
#     main_slime.run()

SLIME_DATA = (
    ("＝", "〇", 1),
    ("～", "☆", 2),
    # ("ー", "★", 3),
)

slimes = []

for i in range(len(SLIME_DATA)):
    slimes.append(slime.Slime(SLIME_DATA[i][0], SLIME_DATA[i][1], SLIME_DATA[i][2]))

print("[List of runners]")
for i in range(len(slimes)):
    print(f"No.{i + 1}：{slimes[i].mark}")

while True:
    print("[Bet]")
    bet = input("No:")
    if (bet.isdigit()) and (1 <= int(bet) <= len(slimes)):
        break

print("[On your mark]")
time.sleep(1)

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("Go!")
time.sleep(1)

judge = False
winner = ""


None
winner_numbers = []

while True:
    print("ーーーー５ーーーー10")
    print()
    for slime in slimes:
        slime.run()
        time.sleep(0.1)
        
        if slime.position > 10:
            winner += ( slime.mark + " " )
            winner_numbers.append(slime.number)
            judge = True

    if judge:
        print("ーーーー５ーーーー10")
        break

print()
print("winner!")
print(winner)

print(f"You bet on {slimes[int(bet) - 1].mark}")

judge = False

for i in winner_numbers:
    if i == int(bet):
        print("You win!")
        judge = True

if not judge:
    print("You lose...")