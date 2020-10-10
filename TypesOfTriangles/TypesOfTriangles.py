from math import sqrt

# Вариант 3

# Определение длин сторон треугольника по заданным координатам точек (тип Integer).
# Найти также биссектрису, проведённую из наименьшего угла треугольника.
# При вычислении длин сторон под корнем должно быть только целое выражение.
# Никаких операций над действительными числами, никаких преобразований типов и т.д.
# Определить является ли треугольник прямоугольным.
# Далее ввести координаты одной точки (тоже Integer) и определить, находится ли она внутри треугольника или нет.
# Если находится, то найти расстояние от этой точки до ближайшей стороны или её продолжения.

def isqrt(n): # Метод Ньютона для вычисления целочисленного корня
	x = n
	y = (x + 1) // 2
	while y < x:
		x = y
		y = (x + n // x) // 2
	return x

print('Введите координаты треугольника A(xa, ya), B(xb, yb ), C(xc, yc)')

xa, ya = map(int, input('Введите xa и ya: ').split())
xb, yb = map(int, input('Введите xb и yb: ').split())
xc, yc = map(int, input('Введите xc и yc: ').split())

xab = xb - xa
yab = yb - ya
AB = abs(isqrt(xab * xab + yab * yab))
print('{}{}'. format('\nДлина стороны AB = ', AB))

xbc = xc - xb
ybc = yc - yb
BC = abs(isqrt(xbc * xbc + ybc * ybc))
print('{}{}'. format('Длина стороны BC = ', BC))

xac = xc - xa
yac = yc - ya
AC = abs(isqrt(xac * xac + yac * yac))
print('{}{}'. format('Длина стороны AC = ', AC))

if (AC >= AB + BC) or (AB >= BC + AC) or (BC >= AB + AC) or (AC + AB + AC == 0):
    print('\nТреугольника не существует\n')
elif (AC * AC == AB * AB + BC * BC) or (AB * AB == BC * BC + AC * AC) or (BC * BC == AB * AB + AC * AC):
    print('\nТреугольник прямоугольный\n')
elif (AC * AC < AB * AB + BC * BC) or (AB * AB < BC * BC + AC * AC) or (BC * BC < AB * AB + AC * AC):
    print('\nТреугольник остроугольный\n')
elif (AC * AC > AB * AB + BC * BC) or (AB * AB > BC * BC + AC * AC) or (BC * BC > AB * AB + AC * AC):
    print('\nТреугольник тупоугольный\n')
