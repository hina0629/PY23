from robot import Robot

robot = Robot()

print(robot.id)
print(robot.name)
print(robot.type)

robot.hello()

robot.give_dorayaki(0)
robot.give_dorayaki(1)
robot.give_dorayaki(4)
robot.give_dorayaki(5)
robot.give_dorayaki(9)
robot.give_dorayaki(10)

print(robot.help())

ROBOTS_DATA = (
    (1, 'ドラえもん', 'ネコ'),
    (2, 'ドラミ', 'ネコ'),
    (3, 'ミニドラ', '小型ネコ'),
)
robots = []
for i in range(len(ROBOTS_DATA)):
    robots.append(Robot(
        ROBOTS_DATA[i][0],
        ROBOTS_DATA[i][1],
        ROBOTS_DATA[i][2]))

for robot in robots:
    robot.hello()