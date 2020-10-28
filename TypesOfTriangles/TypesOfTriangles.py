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
 
    ax, ay = map(int, input('Координаты ax и ay: ').split())
    bx, by = map(int, input('Координаты bx и by: ').split())
    cx, cy = map(int, input('Координаты cx и cy: ').split())

    abx = bx - ax
    aby = by - ay
    AB = sqrt(abx * abx + aby * aby)
    print('{}{:.4f}'.format('\nДлина стороны AB = ', AB))

    bcx = cx - bx
    bcy = cy - by
    BC = sqrt(bcx * bcx + bcy * bcy)
    print('{}{:.4f}'.format('Длина стороны BC = ', BC))

    cax = ax - cx
    cay = ay - cy
    CA = sqrt(cax * cax + cay * cay)
    print('{}{:.4f}'.format('Длина стороны CA = ', CA))

    AB2 = AB * AB
    BC2 = BC * BC
    CA2 = CA * CA

    Eps = 0.001 # Точность для вычислений

    # Определение типа треугольника

    if ((ax == ay) and (bx == by) and (cx == cy)) or \
        ((ay - ax == 1) and (by - bx == 1) and (cy - cx == 1)):
        print('\nТреугольника не существует')
        print('_______________________________________________________\n')
        bool = False
    elif (CA >= AB + BC) or (AB >= BC + CA) \
        or (BC >= AB + CA) or (AB * BC * CA == 0):
        print('\nТреугольника не существует')
        print('_______________________________________________________\n')
        bool = False
    elif ((AB2 + BC2 <= CA2 + Eps) and (AB2 + BC2 >= CA2 - Eps)) or \
         ((BC2 + CA2 <= AB2 + Eps) and (BC2 + CA2 >= AB2 - Eps)) or \
         ((AB2 + CA2 <= BC2 + Eps) and (AB2 + CA2 >= BC2 - Eps)):
        print('\nТреугольник прямоугольный')
        bool = True
    elif (AB2 + BC2 < CA2) or (BC2 + CA2 < AB2) or (AB2 + CA2 < BC2):
        print('\nТреугольник тупоугольный')
        bool = True
    else:
        print('\nТреугольник остроугольный')
        bool = True

    if bool == True:
        print('\nПроверка принадлежности точки P треугольнику ABC:')
        px, py = map(int, input('Введите координаты px и py: ').split())

        v1 = (ax - px) * (by - ay) - (bx - ax) * (ay - py)
        v2 = (bx - px) * (cy - by) - (cx - bx) * (by - py)
        v3 = (cx - px) * (ay - cy) - (ax - cx) * (cy - py)

        # print('{}{}{}{}{}{}'.format('v1 = ', v1, '\nv2 = ', v2, '\nv3 = ', v3))

    #    print('{}{:.4}'. format('\nКосинус угла между векторами AB и BC = ', cosABBC))
    #    print('{}{:.4}'. format('Косинус угла между векторами BC и CA = ', cosBCCA))
    #    print('{}{:.4}'. format('Косинус угла между векторами AB и CA = ', cosABCA))

    #    if (cosABBC == 90) or (cosBCCA == 90) or (cosABCA == 90):
    #        print('\nТреугольник прямоугольный')
    #    elif (cosABBC < 90) and (cosBCCA < 90) and (cosABCA < 90):
    #        print('\nТреугольник остроугольный')
    #    else:
    #        print('\nТреугольник тупоугольный')

        # Нахождение биссектрисы

        Hypotenuse = max(AC, AB, BC)
        Cathetus = min(AC, AB, BC)

        L = Cathetus * sqrt((2 * Hypotenuse) / Cathetus + Hypotenuse)

        print('{}{:0.4}'.format('Биссектриса треугольника: ', L))

        print('\nВведите координаты точки:')
        xp, yp = map(int, input('Введите xp и yp: ').split)
