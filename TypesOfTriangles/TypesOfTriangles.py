# Определение длин сторон треугольника по заданным координатам
# точек (тип Integer).
# Найти также биссектрису, проведённую из наименьшего угла треугольника.
# При вычислении длин сторон под корнем должно быть только целое выражение.
# Никаких операций над действительными числами, никаких преобразований
# типов и т.д.
# Определить является ли треугольник прямоугольным.
#
# Далее ввести координаты одной точки (тоже Integer) и определить,
# находится ли она внутри треугольника или нет.
# Если находится, то найти расстояние от этой точки до ближайшей
# стороны или её продолжения.
#

from math import sqrt

print()
while True:
    print('Введите координаты треугольника A(ax, ay), B(bx, by), C(cx, cy)')

    ax, ay = map(int, input('Координаты ax и ay: ').split())
    bx, by = map(int, input('Координаты bx и by: ').split())
    cx, cy = map(int, input('Координаты cx и cy: ').split())

    # Вычисление длин сторон треугольника

    abx = bx - ax
    aby = by - ay
    AB = sqrt(abx * abx + aby * aby)
    print('\nДлина стороны AB = {:.4f}'.format(AB))

    bcx = cx - bx
    bcy = cy - by
    BC = sqrt(bcx * bcx + bcy * bcy)
    print('Длина стороны BC = {:.4f}'.format(BC))

    cax = ax - cx
    cay = ay - cy
    CA = sqrt(cax * cax + cay * cay)
    print('Длина стороны CA = {:.4f}'.format(CA))

    AB2 = AB * AB
    BC2 = BC * BC
    CA2 = CA * CA

    Eps = 0.001 # Точность для вычислений

    # Определение типа треугольника

    if ((ax == ay) and (bx == by) and (cx == cy)) or \
        ((ay - ax == 1) and (by - bx == 1) and (cy - cx == 1)):
        print('\nТреугольника не существует')
        print('-' * 55, '\n')
        bool = False
    elif (CA >= AB + BC) or (AB >= BC + CA) \
        or (BC >= AB + CA) or (AB * BC * CA == 0):
        print('\nТреугольника не существует')
        print('-' * 55, '\n')
        bool = False
    elif abs((AB2 - (BC2 + CA2))) <= Eps\
        or abs((BC2 - (AB2 + CA2))) <= Eps\
        or abs((CA2 - (AB2 + BC2))) <= Eps:
        print('\nТреугольник прямоугольный')
        bool = True
    elif (AB2 + BC2 < CA2) or (BC2 + CA2 < AB2) or (AB2 + CA2 < BC2):
        print('\nТреугольник тупоугольный')
        bool = True
    else:
        print('\nТреугольник остроугольный')
        bool = True

    if bool == True:

        # Вычисление длины биссектрисы,
        # проведённой из наименьшего угла треугольника

        # Нахождение полупериметра треугольника ABC

        p = (AB + BC + CA) / 2

        # Нахождение площади треугольника ABC

        S = sqrt(p * (p - AB) * (p - BC) * (p - CA))

        minSide = str(min(AB, BC, CA))
        if minSide == AB:
            bis = 2 * sqrt((BC * CA * p) * (p - AB)) / (BC + CA)
            minSide = 'AB'
            nameBis = CD
        elif minSide == 'BC':
            bis = 2 * sqrt((AB * CA * p) * (p - BC)) / (AB + CA)
            minSide = 'BC'
            nameBis = 'AD'
        else:
            bis = 2 * sqrt((AB * BC * p) * (p - CA)) / (AB + BC)
            minSide = 'AC'
            nameBis = 'BD'
        print('{}{}{}'.format('\nНаименьший угол треугольника лежит \
напротив наименьшей стороны (', minSide, ')'))
        print('{}{}{}{:.4f}'.format('Длина биссектрисы ', nameBis,\
' равна\nL = ', bis))

        # Определение принадлежности точки P треугольнику

        print('\nПроверка принадлежности точки P треугольнику ABC:')
        px, py = map(int, input('Введите координаты px и py: ').split())

        # Нахождение сторон треугольников через вершину P(px, py)

        bpx = px - bx
        bpy = py - by
        BP = sqrt((bpx * bpx) + (bpy * bpy))

        pcx = cx - px
        pcy = cy - py
        PC = sqrt((pcx * pcx) + (pcy * pcy))

        pax = ax - px
        pay = ay - py
        PA = sqrt((pax * pax) + (pay * pay))

        # Нахождение полупериметров треугольников ABP, BCP, CAP
            
        p1 = (AB + PA + BP) / 2
        p2 = (BC + BP + PC) / 2
        p3 = (CA + PC + PA) / 2

        # Нахождение площадей треугольников ABP, BCP, CAP

        S1 = sqrt(p1 * (p1 - AB) * (p1 - BP) * (p1 - PA))
        S2 = sqrt(p2 * (p2 - BC) * (p2 - BP) * (p2 - PC))
        S3 = sqrt(p3 * (p3 - CA) * (p3 - PC) * (p3 - PA))

        if  abs((S - (S1 + S2))) <= Eps\
            or abs((S - (S2 + S3))) <= Eps\
            or abs((S - (S1 + S3))) <= Eps:
            print('\nТочка лежит на стороне треугольнике')
            print('-' * 55, '\n')
        elif abs((S - (S1 + S2 + S3))) <= Eps:
            print('\nТочка лежит внутри треугольника\n')

            # Нахождение высот треугольников ABP, BCP, CAP

            h1 = 2 * S1 / AB;
            h2 = 2 * S2 / BC;
            h3 = 2 * S3 / CA;

            # Сравнение высот и поиск минимальной

            minDistance = min(h1, h2, h3)
            if minDistance == h1:
                side = 'AB'
            elif minDistance == h2:
                side = 'BC'
            else:
                side = 'CA'
            print('Расстояние от точки P до ближайшей стороны треугольника ({}\
):\nl = {:0.4f}'.format(side, minDistance))
            print('-' * 55, '\n')
        else:
            print('\nТочка не лежит внутри треугольника')
            print('-' * 55, '\n')
