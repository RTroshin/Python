from math import sqrt, degrees, hypot, acos, pi

# Определение длин сторон треугольника по заданным координатам точек (тип Integer).
# Найти также биссектрису, проведённую из наименьшего угла треугольника.
# При вычислении длин сторон под корнем должно быть только целое выражение.
# Никаких операций над действительными числами, никаких преобразований типов и т.д.
# Определить является ли треугольник прямоугольным.
# Далее ввести координаты одной точки (тоже Integer) и определить, находится ли она внутри треугольника или нет.
# Если находится, то найти расстояние от этой точки до ближайшей стороны или её продолжения.

print('Введите координаты треугольника A(xa, ya), B(xb, yb ), C(xc, yc)')

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
