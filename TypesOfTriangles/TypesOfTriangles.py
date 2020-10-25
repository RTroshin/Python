from math import sqrt

# Определение длин сторон треугольника по заданным координатам точек (тип Integer).
# Найти также биссектрису, проведённую из наименьшего угла треугольника.
# При вычислении длин сторон под корнем должно быть только целое выражение.
# Никаких операций над действительными числами, никаких преобразований типов и т.д.
# Определить является ли треугольник прямоугольным.
# Далее ввести координаты одной точки (тоже Integer) и определить, находится ли она внутри треугольника или нет.
# Если находится, то найти расстояние от этой точки до ближайшей стороны или её продолжения.
#

print()
while True:
    print('Введите координаты треугольника A(ax, ay), B(bx, by), C(cx, cy)')

    xa, ya = map(int, input('Введите xa и ya: ').split())
    xb, yb = map(int, input('Введите xb и yb: ').split())
    xc, yc = map(int, input('Введите xc и yc: ').split())

    xab = xb - xa
    yab = yb - ya
    AB = sqrt(xab * xab + yab * yab)
    print('{}{:.4}'. format('\nДлина стороны AB = ', AB))

    xbc = xc - xb
    ybc = yc - yb
    BC = sqrt(xbc * xbc + ybc * ybc)
    print('{}{:.4}'. format('Длина стороны BC = ', BC))

    xca = xa - xc
    yca = ya - yc
    CA = sqrt(xca * xca + yca * yca)
    print('{}{:.4}'. format('Длина стороны CA = ', CA))

    if (AC >= AB + BC) or (AB >= BC + AC) or (BC >= AB + AC) or (AC + AB + AC == 0):
        print('\nТреугольника не существует\n')
    elif (AC * AC == AB * AB + BC * BC) or (AB * AB == BC * BC + AC * AC) or (BC * BC == AB * AB + AC * AC):
        print('\nТреугольник прямоугольный\n')
    elif (AC * AC < AB * AB + BC * BC) or (AB * AB < BC * BC + AC * AC) or (BC * BC < AB * AB + AC * AC):
        print('\nТреугольник остроугольный\n')
    elif (AC * AC > AB * AB + BC * BC) or (AB * AB > BC * BC + AC * AC) or (BC * BC > AB * AB + AC * AC):
        print('\nТреугольник тупоугольный\n')

    # Вычисление скалярного произведения

    scalarABBC = xab * xbc + yab * ybc
    scalarBCCA = xbc * xca + ybc * yca
    scalarABCA = xab * xca + yab * yca

    print('{}{}{}{}{}{}'.format('\nAB * BC = ', scalarABBC, '\nBC * CA = ', scalarBCCA, '\nAB * CA = ', scalarABCA))

    if (AB >= BC + CA) or (BC >= AB + CA) or (CA >= AB + BC) or (AB * BC * CA == 0.0):
        print('\nТреугольника не существует')
    else:
        cosABBC = degrees(acos(scalarABBC / (AB * BC)))
        cosBCCA = degrees(acos(scalarBCCA / (BC * CA)))
        cosABCA = degrees(acos(scalarABCA / (AB * CA)))
        print('{}{}{}{}{}{}'.format('\ncosAB^BC = ', cosABBC, '\ncosBC^CA = ', cosBCCA, '\ncosAB^CA = ', cosABCA))

        print('{}{:.4}'. format('\nКосинус угла между векторами AB и BC = ', cosABBC))
        print('{}{:.4}'. format('Косинус угла между векторами BC и CA = ', cosBCCA))
        print('{}{:.4}'. format('Косинус угла между векторами AB и CA = ', cosABCA))

        if (cosABBC == 90) or (cosBCCA == 90) or (cosABCA == 90):
            print('\nТреугольник прямоугольный')
        elif (cosABBC < 90) and (cosBCCA < 90) and (cosABCA < 90):
            print('\nТреугольник остроугольный')
        else:
            print('\nТреугольник тупоугольный')

        # Нахождение биссектрисы

        Hypotenuse = max(AC, AB, BC)
        Cathetus = min(AC, AB, BC)

        L = Cathetus * sqrt((2 * Hypotenuse) / Cathetus + Hypotenuse)

        print('{}{:0.4}'.format('Биссектриса треугольника: ', L))

        print('\nВведите координаты точки:')
        xp, yp = map(int, input('Введите xp и yp: ').split)
