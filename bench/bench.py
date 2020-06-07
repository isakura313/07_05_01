from simple_benchmark import benchmark
from cikl import *
from factorial import *
import matplotlib.pyplot as plt


func = [fact_rec, cikl] # список с нашими функциями нашими
arguments = {} #у нас аргументы передаются в словаре
for i in range(2, 5):
    arguments[str(i)] = i
print(arguments)

arguments_name = 'натуральные числа'
aliases = {fact_rec: "Простая рекурсия", cikl:"Использование цикла"}
b = benchmark(func, arguments, arguments_name, aliases)
print(benchmark.__doc__)
b.plot()

plt.show(b)



