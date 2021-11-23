def repeat(n):
    def logging_decorator(genuine_function):
        def fake_function(y):
            ans = y
            for i in range(n):
                ans = genuine_function(ans)

            return ans

        return fake_function

    return logging_decorator


@repeat(2)
def plus_1(x):
    return x + 1


@repeat(0)
def mul_2(x):
    return x * 2


print(plus_1(3))
print(mul_2(4))
