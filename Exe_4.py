#   Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
#   в этой четверти (x и y).

quartal = int(input('Quartal: '))

if quartal == 1:
    print('x > 0, y > 0')
elif quartal == 2:
    print('x < 0, y > 0')
elif quartal == 3:
    print('x < 0, y < 0')
else:
    print('x > 0, y < 0')