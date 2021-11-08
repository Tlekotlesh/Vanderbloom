A = open('4 миллиона числа пи.txt')
a = list(A.read().split())
S = ''

for i in a:
    S += i

B = open("Final_pi.txt", 'w')
B.write(S)
B.close()