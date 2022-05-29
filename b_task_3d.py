from abc import ABC, abstractmethod
import numpy as np
from numpy import array as vec
import numpy.linalg
import matplotlib.pyplot as plt
import itertools
import turtle

MODEL_G = 0.5  # гравитационная постоянная
COLLISION_DISTANCE = 5.0
COLLISION_COEFFICIENT = 50.0
MODEL_DELTA_T = 0.01
TIME_TO_MODEL = 100

# Тут все интересные значения.
N = 3  # Количество тел

x = 0  # Смещение по координатам
y = 0

cords = [[0., 0.], [100., 0.], [0., 100.]]  # Начальные координаты
vir = [[0., 0.], [0., -10.], [15., 0.]]  # Скорость
all_mass = [50000., 10., 10.]  # Массы слева направо

k = 2  # Увеличение изображение
speed = 15  # Скорость отображения орбит

about = 0  # Относительно какого тела строиьтся график.
# Если 0 - то относительно вселеннского эфира. -1 - относ.


# центра масс. 1...n относ. тел.


# ABC это не алфавит, а AbstractBaseClass. Не даст создать экземпляр,
# пока не переопределишь все методы-заглушки
class Universe(ABC):
    """Невнятная вселенная, основа всех миров"""

    def __init__(self):
        self.bodies = []

    @abstractmethod
    def gravity_flow_dencity_per_1_1(self, dist):
        """
        Плотность потока гравитационного поля между двумя
        единичными массами на заданном расстоянии
        """
        ...

    def model_step(self):
        """Итерация решения задачи Коши. Конечно не присуща вселенной, но тут на своём месте"""
        for b1, b2 in itertools.product(self.bodies, self.bodies):
            if b1 != b2:
                b1.apply_force(b1.force_induced_by_other(b2))
        for b in self.bodies:
            b.advance()

    def add_body(self, body):
        self.bodies.append(body)


class MaterialPoint:
    """Материальная точка, движущаяся по двумерной плоскости"""

    def __init__(self, universe, mass, position, velocity):
        self.universe = universe
        self.mass = mass
        self.position = position
        self.velocity = velocity
        universe.add_body(self)

        self.ptrace = [self.position.copy()]
        self.vtrace = [self.velocity.copy()]

    def force_induced_by_other(self, other):
        """Сила, с которой другое тело действует на данное"""
        delta_p = other.position - self.position
        distance = numpy.linalg.norm(delta_p)  # Евклидова норма (по теореме Пифагора)
        force_direction = delta_p / distance
        force = force_direction * self.mass * other.mass * \
                self.universe.gravity_flow_dencity_per_1_1(distance)
        return force

    def advance(self):
        """Перемещаем тело, исходя из его скорости"""
        self.position += self.velocity * MODEL_DELTA_T
        self.ptrace.append(self.position.copy())
        self.vtrace.append(self.velocity.copy())

    def apply_force(self, force):
        """Изменяем скорость, исходя из силы, действующей на тело"""
        self.velocity += force * MODEL_DELTA_T / self.mass


class Universe3D(Universe):
    def __init__(self,
                 G,  # гравитационная постоянная
                 k,  # коэффициент при упругом соударении
                 collision_distance  # всё-таки это не точки
                 ):
        super().__init__()
        self.G = G
        self.k = k
        self.collision_distance = collision_distance

    def gravity_flow_dencity_per_1_1(self, dist):
        # будем считать, что отскакивают точки друг от друга резко,
        # но стараться не допускать этого

        if dist > self.collision_distance:
            # Ситуация с обычным потоком поля — просто притяжение
            return self.G / dist ** 2
        else:
            # Отталкивание при соударении (притяжение убираем).
            # К гравитации не относится, т.к. имеет скорее электростатическую
            # природу, так что это sort of hack.
            # Никаких конкретных законов не реализует, просто нечто отрицательное =)
            return -self.k / dist ** (1 / 2)


u = Universe3D(MODEL_G, COLLISION_COEFFICIENT, COLLISION_DISTANCE)

bodies = []
for d in range(N):
    bodies.append(MaterialPoint(u, all_mass[d], vec(cords[d]), vec(vir[d])))

steps = int(TIME_TO_MODEL / MODEL_DELTA_T)
for stepn in range(steps):
    u.model_step()


def plt_kepler(same_fig=False):
    for zo in bodies:
        delta_s = []
        f = zo.ptrace
        g = zo.vtrace
        for c in range(len(f)):
            ds = abs(np.cross(f[c], g[c])) / 2
            delta_s.append(ds)
        too = range(len(delta_s))
        plt.plot(too, delta_s)

        if not same_fig:  # По картинке на тело
            plt.show()
    if same_fig:  # Одна картинка на всех
        plt.show()


plt_kepler()
plt_kepler(True)

win = turtle.Screen()

m = sum(all_mass[:N + 1])
M_P = []
for i in range(N):
    m_point = turtle.Turtle()
    m_point.shape('circle')
    color = hex(2)[2:]
    m_point.pencolor('#' + '0' * (4 - len(color)) + color + 'ff')
    m_point.turtlesize(k * (all_mass[i] / 10000000) ** (1 / 6))
    m_point.up()
    if about != 0 and about != -1:
        m_point.goto(k * (cords[i][0] - cords[about - 1][0] - x), k * (cords[i][1] - cords[about - 1][1] - y))
    elif about == - 1:
        rcx = 0
        rcy = 0
        for io in range(N):
            rcx += all_mass[io] * cords[io][0]
            rcy += all_mass[io] * cords[io][1]
        rcx = rcx / m
        rcy = rcy / m
        m_point.goto(k * (cords[i][0] - rcx - x), k * (cords[i][1] - rcy - y))
    else:
        m_point.goto(k * (cords[i][0] - x), k * (cords[i][1] - y))
    m_point.down()
    t = bodies[i].ptrace
    xs = [p[0] for p in t]
    ys = [p[1] for p in t]
    M_P.append([m_point, xs, ys])

win.tracer(speed, 0)

a = 0
b = 0
for i in range(len(M_P[0][1])):

    for s in range(N):
        if about == 0:
            pass
        elif about == -1:
            rcx = 0
            rcy = 0

            for io in range(N):
                rcx += all_mass[io] * M_P[io][1][i]
                rcy += all_mass[io] * M_P[io][2][i]
            rcx = rcx / m
            rcy = rcy / m
            a = rcx
            b = rcy
        else:
            a = M_P[about - 1][1][i]
            b = M_P[about - 1][2][i]
        M_P[s][0].goto(k * (M_P[s][1][i] - a - x), k * (M_P[s][2][i] - b - y))

win.mainloop()
