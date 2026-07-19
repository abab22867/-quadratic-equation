import cmath

def data_input():
    while True:
        try:
            n = float(input("Введите число: "))
            return n
        except ValueError:
            print("Необходимо ввести число")

def discriminant(a, b, c):
    D = b ** 2 - 4 * a * c
    return D

def formula(a, b, c):
    x1 = (-b + cmath.sqrt(discriminant(a, b, c))) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminant(a, b, c))) / (2 * a)
    return x1, x2

def main(a, b, c):
    x = 'Не существует решения'
    if a == 0:
        if b == 0:
            if c == 0:
                x = 'Бесконечное количество решений'
            else:
                pass
        else:
            x = - c / b
    elif discriminant(a, b, c) < 0:
        print("Корней нет на множестве действительных чисел")
        print('Комплексные корни:')
        x = formula(a, b, c)
    elif discriminant(a, b, c) == 0:
        x = formula(a, b, c)[0].real
    elif discriminant(a, b, c) > 0:
        x = (formula(a, b, c)[0].real, formula(a, b, c)[1].real)
    return x

print('Коэффициенты квадратного уравнения:')
a = data_input()
b = data_input()
c = data_input()
print('Корни квадратного уравнения:')
print(main(a, b, c))