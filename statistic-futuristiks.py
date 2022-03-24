import pandas
import random
import matplotlib
import numpy
import matplotlib.pyplot as plt
from scipy import stats


counter = 50
experiments = [4.50,
4.13,
4.59,
4.66,
3.51,
3.87,
3.72,
4.15,
3.81,
4.04,
4.09,
3.90,
4.08,
4.06,
3.84,
4.02,
3.88,
3.92,
3.88,
3.70,
4.00,
3.84,
3.82,
3.88,
3.88,
3.87,
3.78,
3.78,
3.79,
3.96,
4.13,
4.14,
3.93,
4.34,
4.14,
3.88,
4.11,
3.88,
3.74,
3.66,
3.82,
3.62,
3.61,
3.69,
3.88,
3.90,
3.86,
4.09,
3.78,
3.84]
plt.plot(list(range(counter)), experiments)
plt.title('Experimental data')
plt.show()

df = pandas.DataFrame(data={
    'experiments': experiments
})

df.to_csv("experiments.csv")


df1 = pandas.read_csv("experiments.csv")


df1['experiments'].plot(kind='bar')


print(df1.experiments.describe())


df12 = pandas.DataFrame(data={
    'df1': df1['experiments'],
})

df12.plot.kde()

d1 = df12['df1']

print(stats.kstest('norm', 'norm', N=500))
print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=len(d1)))
#statistic = 0,168 - маленькое значение; pvalue=0.1 - тоже мало, но тем не менее распределение нормальное.