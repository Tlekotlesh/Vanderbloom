from numbers import Number


class RingDomainError(ValueError):
    pass


class RingZeroDivisionError(ValueError):
    pass


class RingTypeError(TypeError):
    pass


class Ring:

    def __init__(self, arg=(0, 0)):
        if isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], Number) and isinstance(arg[1], Number):
            self.couple = list(arg)
        elif isinstance(arg, list) and len(arg) == 2 and isinstance(arg[0], Number) and isinstance(arg[1], Number):
            self.couple = arg
        else:
            raise RingTypeError("You are trying to create couple from " + repr(arg))

    def __str__(self):
        return '(ﾉ◕ヮ◕)ﾉ ' + str(self.couple[0]) + ' :･ﾟ✧ ✧ﾟ･: '+ str(self.couple[1]) + ' ヽ(◕ヮ◕ヽ)'

    def __eq__(self, other):
        if isinstance(other, Ring):
            pass
        else:
            other = Ring(other)

        if isinstance(other, Ring):
            return self.couple[0] == other.couple[0] and self.couple[1] == other.couple[1]
        else:
            raise RingDomainError("Can't say if couples is equal to " + str(type(other)))

    def is_reverse(self):
        if abs(self.couple[0]) != abs(self.couple[1]):
            return "This couple has a inverse elements. Here it is:" + str(Ring([1, 0]).__floordiv__(self))

    def __add__(self, other):
        if isinstance(other, Ring):
            pass
        else:
            other = Ring(other)

        sc = self.couple.copy()
        oc = other.couple.copy()

        return Ring([sc[0] + oc[0], sc[1] + oc[1]])

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return Ring([-c for c in self.couple])

    def __sub__(self, other):
        if isinstance(other, Ring):
            pass
        else:
            other = Ring(other)

        return self.__add__(other.__neg__())

    def __rsub__(self, other):
        return self.__neg__().__add__(other)

    def __mul__(self, other):
        if isinstance(other, Ring):
            pass
        else:
            other = Ring(other)

        sc = self.couple.copy()
        oc = other.couple.copy()

        return Ring([sc[0] * oc[0] + sc[1] * oc[1], sc[0] * oc[1] + sc[1] * oc[0]])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        if isinstance(other, Ring):
            pass
        else:
            other = Ring(other)

        oc = other.couple.copy()
        if abs(oc[0]) != abs(oc[1]):
            return self.__mul__(Ring([oc[0] / (oc[0] ** 2 - oc[1] ** 2), oc[1] / (oc[1] ** 2 - oc[0] ** 2)]))
        else:
            raise RingZeroDivisionError("You are trying to divide by an irreversible element " + repr(other))


C = Ring([0, 1])
C1 = Ring((0, 1))
A = C * C1
print(A) # Почти поле, но нет обратного к парам вида (х, -х) и (х, х)
