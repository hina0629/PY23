import slime
import time

main_slime = slime.Slime("＝", "〇", 1)

while main_slime.position < 11:
    main_slime.run()

SLIME_DATA = (
    ("＝", "〇", 1),
    ("～", "☆", 2),
    ("ー", "★", 3),
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

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("Go!")
time.sleep(1)

judge = False
winner = ""


None
winner_number = []

while True:
    print("ーーーー５ーーーー10")
    print()
    for slime in slimes:
        slime.run()
        time.sleep(0.1)
        
        if winner is not None and slime.position >= 11:
            winner += slime.mark
            winner_number.append(slime.number)

        elif slime.position >= 11:
            judge = True
            winner = slime.mark
            winner_number.append(slime.number)

    if judge:
        print("ーーーー５ーーーー10")
        break

print()
print("winner!")
print(winner)

print(f"You bet on {slimes[int(bet) - 1].mark}")

if len(winner_number) > 1:
    for i in winner_number:
        if i == int(bet):
            print("You win!")
            break
elif int(bet) == winner_number[0]:
    print("You win!")
else:
    print("You lose!")
