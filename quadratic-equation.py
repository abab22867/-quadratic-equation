import cmath
import math

class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def validate_coefficients(a, b, c):
        if not all(isinstance(x, (int, float)) for x in [a, b, c]):
            raise TypeError("Все коэффициенты должны быть числами")
        return True

    def checking_special_cases(self):
        if self.a == 0 and self.b == 0 and self.c == 0:
            print('Бесконечное количество решений')
            return 'infinite'
        elif self.a == 0 and self.b == 0 and self.c != 0:
            print('Не существует решения')
            return 'no_solution'
        elif self.a == 0 and self.b != 0:
            root = -self.c / self.b
            print(f'Линейное уравнение, корень: {root}')
            return 'linear', root
        else:
            print('Крайних случаев нет')
            return 'quadratic'

class QuadraticEquation(Equation):
    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c
    def calculating_roots(self):
        D = self.discriminant()
        if D < 0:
            self.x1 = (-self.b + cmath.sqrt(D)) / (2 * self.a)
            self.x2 = (-self.b - cmath.sqrt(D)) / (2 * self.a)
        else:
            self.x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            self.x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
        return self.x1, self.x2

    def printing_results(self):
        D = self.discriminant()
        if D < 0:
            print("Корней нет на множестве действительных чисел")
            print('Комплексные корни:')
            roots = self.calculating_roots()
            print(f"x1 = {roots[0]}")
            print(f"x2 = {roots[1]}")
        else:
            roots = self.calculating_roots()
            if roots[0] == roots[1]:
                print(f"Один корень: x = {roots[0]}")
            else:
                print(f"x1 = {roots[0]}")
                print(f"x2 = {roots[1]}")

print('Введите коэффициенты квадратного уравнения (a b c):')
try:
    a, b, c = map(float, input().split())
    if Equation.validate_coefficients(a, b, c):
        equation = QuadraticEquation(a, b, c)
        result = equation.checking_special_cases()
        if result == 'quadratic':
            roots = equation.printing_results()
except ValueError as e:
    print(f"Ошибка ввода: {e}")
except TypeError as e:
    print(f"Ошибка типа: {e}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль")
