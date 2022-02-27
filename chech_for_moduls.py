from love_aloy import *

t = 1.1036682729472387  # Стьюдент для 6 измерений с доверительным интервалом 0.68
h1 = [11.9 * 1000, 11.9 * 1000, 12.0 * 1000, 12.1 * 1000, 11.9 * 1000, 12.1 * 1000]
h2 = [2.5 * 1000, 2.6 * 1000, 2.5 * 1000, 2.5 * 1000, 2.6 * 1000, 2.6 * 1000]
DELTA_h1 = sigma(h1, t, 100)
DELTA_h2 = sigma(h2, t, 100)
h1_average = sum(h1) / len(h1)
h2_average = sum(h2) / len(h2)
print(DELTA_h1, DELTA_h2)
print(indirect_error('h1 /  (h1 - h2)', 'missing', 'h1 h2', [DELTA_h1, DELTA_h2], [h1_average, h2_average]))
