from math import pi, sin

# z1 = x^3 - 6,5x^2 - 31,3x + 2,32
# z2 = x^3 - sin(Pix)
# z3 = z1^2 - z2^2
#
# x = 0 (0,05) 1
#
# Оператор "while"
# Определить минимальное значение z1 и максимальное z2
#

print()
while True:
    while True:
        x = float(input('Введите значение аргумента x в диапазоне (0..1): '))
        if (x < 0) or (x > 1):
            print('\nНеверное значение! Попробуйте ещё раз!')
        else:
            break

    min_z1 = 0
    max_z2 = 0

    z1 = x**3 - 6.5 * x**2 - 31.3 * x + 2.32
    z2 = x**3 - sin(pi * x)
    z3 = z1**2 - z2**2

    step = 0.05
    number = 1

    print('{}'.format('----------------------------------------------------------', sep='-'))
    print('{:^5s}| {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format('№', 'Аргумент', 'Ф1', 'Ф2', 'Ф3'))
    print('                                            |            | ')
    while x < 1:
        z1 = x**3 - 6.5 * x**2 - 31.3 * x + 2.32
        z2 = x**3 - sin(pi * x)
        z3 = z1**2 - z2**2

        if min_z1 > z1:
            min_z1 = z1
        if max_z2 < z2:
            max_z2 = z2

        if number % 2 != 0:
            elem = '|'
        else:
            elem = ' '
        print('{1:^5d}{0} {2: 10.4f} {0} {3: 10.4f} {0} {4: 10.4f} | {5: 10.4f} |'.format(elem, number, x, z1, z2, z3))
        #if (number % 2 != 0):
        #    print('{:^3d}| {: 10.3f} | {: 10.3f} | {: 10.3f} | {: 10.3f} |'.format(number, x, z1, z2, z3))
        #else:
        #    print('{:^3d}  {: 10.3f}   {: 10.3f}   {: 10.3f}   {: 10.3f} |'.format(number, x, z1, z2, z3))
        #if (number % 2 != 0):
        #    print(' %-2d | %7f | %7f | %7f | %7f |' % (number, x, z1, z2, z3))
        #else:
        #    print(' %-2d   %7f   %7f   %7f   %7f |' % (number, x, z1, z2, z3))
        x += step
        number += 1
    print('{}'.format('----------------------------------------------------------\n', sep='-', end = '\n'))
    print('Минимальное значение функции z1: {: .4f}\nМаксимальное значение функции z2: {: .4f}\n'.format(min_z1, max_z2))
