import random
check1 = 0
check2 = 0
data = 0
for i in range(0, 10000):
    a = [1, 2, 3]
    b = [1, 2, 3]
    for i in range(0, 100):
        door = random.choice(a)
        door1 = random.choice(a)
        car = random.choice(b)
    if door == door1 == car or door != door1 == car: # всего вариантов
        data += 1
    if door != door1 == car:
        print('поменяли и выиграли', door, door1, car) # ситуации, где поменяли дверь и выиграли
        check1 += 1
    elif door == door1 == car:
        print('оставили и выиграли', door, door1, car) # ситуации, где оставили дверь и выиграли
        check2 += 1
print(data, "вариантов,", check1, "поменяли и выиграли -", check1 // (data // 100), "%,", check2, "оставили и выиграли -", check2 // (data // 100), "%")
