import robot

robot1 = robot.Robot(1, "ドラえもん", "ネコ")
print(robot1.no)
print(robot1.name)
print(robot1.kata)

robot1.hello()

robot1.give_dorayaki(0)
robot1.give_dorayaki(1)
robot1.give_dorayaki(5)
robot1.give_dorayaki(10)

print(robot1.help())

robots = []

for i in range(3):
    robots.append(robot.Robot(i + 1, f"ドラえもん{i + 1}", "ネコ"))

for r in robots:
    r.hello()