import math # импортируем математику
import matplotlib.pyplot as plt # импортируем пакет построения графиков
import numpy

def plot_stuff(x): # Делаем функцию по построению графика
    plt.plot(x, [(math.sin(a / c) ** n) * (math.sin(a / b) ** m) for a in x]) # Сам график - все оттенки кардиограммы студента перед сессией по матанализу.


A = [1] + [10*i for i in range(1, 6)] # Создаем разнообразие
S = [i for i in range(0, 5)] # Тут тоже
x = numpy.arange(-100, 100, 0.1) # Массив значений

plt.ion() # Разбдочиваем неизменность графика
fig , axes = plt.subplots(1) # Создаем фигуру
plt.show() # Показываем холст

for c in A:  # Непосредственно перебор
        for b in A: # Тут тоже
            for n in S: # Тут тоже
                for m in S: # Тут тоже
                    plt.plot(x, [(math.sin(a / c) ** n) * (math.sin(a / b) ** m) for a in x])  # Сам график - все оттенки кардиограммы студента перед сессией по матанализу.
                    plt.pause(0.1) # Выжидаем некоторое время
                    fig.clear() # Очищаем холст от старого графика


