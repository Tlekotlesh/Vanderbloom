import numpy as np
from matplotlib import pyplot as pp

MODEL_G = 9.81
MODEL_DT = 0.001


class Body:
    def __init__(self, x, y, vx, vy):
        """
        Создать тело.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        vx: float
            горизонтальная скорость
        vy: float
            вертикальная скорость
        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.trajectory_x = []
        self.trajectory_y = []

    def advance(self):
        """
        Выполнить шаг мат. модели применительно к телу, предварительно записав его координаты
        """
        self.trajectory_x.append(self.x)
        self.trajectory_y.append(self.y)


        self.x += self.vx * MODEL_DT
        self.y += self.vy * MODEL_DT
        self.vy -= MODEL_G * MODEL_DT


class Rocket(Body):
    def __init__(self, x, y, mass_r, mass_oil, ux, uy, dm):
        """
        Создать ракету.

        Пареметры:
        ----------
        x: float
            горизонтальная координата
        y: float
            вертикальная координата
        """
        super().__init__(x, y, 10, 100) # Начальная скорость при t = 0
        self.mass_r = mass_r
        self.mass_oil = mass_oil
        self.ux = ux
        self.uy = uy
        self.dm = dm
        self.all_mass = mass_r + mass_oil


    def advance(self):
        super().advance()
        if self.mass_oil > 0:
            self.all_mass += self.dm * MODEL_DT
            self.mass_oil += self.dm * MODEL_DT
            if MODEL_DT * MODEL_G <= -((self.uy * self.dm) / (self.all_mass)) * MODEL_DT:
                self.vx += -((self.ux * self.dm) / (self.all_mass)) * MODEL_DT
                self.vy += -((self.uy * self.dm) / (self.all_mass)) * MODEL_DT
            else:
                self.vy += MODEL_DT * MODEL_G # Не прзволяем ракете падать во время разгона




b = Body(0, 0, 10, 100)
r = Rocket(0, 0, 1, 15, 1, 1, -2.5)  # Rocket(начальные кординаты x, начальные координаты у, масса самой ракеты, масса топлива, относ. скорость по х, относ. скор. по у, расход топлива)

bodies = [b, r]

for t in np.arange(0, 20, MODEL_DT):
    for b in bodies:
        b.advance()

for b in bodies:
    pp.plot(b.trajectory_x, b.trajectory_y)
pp.show()
