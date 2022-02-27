from sympy import Symbol, diff, sympify
from numba import prange


def never_ever_call_me():
    print('How you dare!')
    a = input("Do not press 5 and then enter! Whatever you want but not 5...")
    if a == '5':
        print("I told you so...")
        print("https://www.youtube.com/watch?v=a7Dh5QoXv2c")
    else:
        print('Good...')


# сигма среднего. Вводные данные: массив случайной величины и приборная погрешность
def sigma(array, t, device, show_sigma = False, show_sudden = False):
    s = 0
    n = len(array)
    avr = sum(array) / n
    for i in range(n):
        s += (array[i] - avr)**2
    sigma_suddenly = (s / (n*(n - 1)))**(1/2)
    if show_sigma:
        print(sigma_suddenly)
    delta_suddenly = sigma_suddenly * t
    if show_sudden:
        print(delta_suddenly)
    return (delta_suddenly**2 + device**2)**(1/2)


# Погрешность косвенныных измерений. На вход функция, константы
# (по которым не интегрируют, строка из символов через пробел),
# переменные (строка из символов через пробел),
# абсолютные погрешности (массив), их значения (сначала переменных затем констант массив).
def indirect_error(function, const, variable, abs_error, args):
    row = list(map(Symbol, variable.split(" ")))
    if const != 'missing':
        consts = list(map(Symbol, const.split(" ")))
    else:
        consts = []
    sympy_function = sympify(function)
    s = sympify('0')
    for i in prange(len(row)):
        s += (diff(sympy_function, row[i])**2)*(abs_error[i])**2
    s = s ** (1/2)
    params = {}
    time_array = row + consts
    for j in prange(len(time_array)):
        params[time_array[j]] = args[j]
    ans = (sympy_function.evalf(20, subs=params), s.evalf(20, subs=params))
    return ans
