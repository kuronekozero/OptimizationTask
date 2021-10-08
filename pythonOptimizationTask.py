from math import floor

max = 0 # Максимальная прибыль
min1 = 1000 # Минимальная прибыль
truex = 0 # Количество упоковок "Черное дерево"
truey = 0 # Количество упоковок "Букет вкусов"

for x in range(1, 2000):
    y1 = floor((1365 - 0.7 * x) / 0.3)
    y2 = floor((1245 - 0.6 * x) / 0.3)
    y3 = floor((650 - 0.1 * x) / 0.2)

    if y1 < 0 or y2 < 0 or y3 < 0:
        break

    if y1 < y2 and y1 < y3:
        y = y1

    elif y2 < y1 and y2 < y3:
        y = y2

    else:
        y = y3

    if 90 * x + 100 * y > max:
        max = 90 * x + 100 * y
        truex = x
        truey = y

    if (1365 - 0.7 * x - 0.3 * y) + (1245 - 0.6 * x - 0.7 * y) + (650 - 0.1 * x - 0.2 * y) < min1:
        min = (1365 - 0.7 * x - 0.3 * y) + (1245 - 0.6 * x - 0.3 * y) + (650 - 0.1 * x - 0.2 * y)
        minx = x
        miny = y

print("Максимальна прибыль = ", max)
print("Минимальное число кофе, что может остаться", min1)
print("Черное дерево = ", truex)
print("Букет вкусов = ", truey)


