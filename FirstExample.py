from abc import ABC, abstractmethod
from cmath import sin
import numpy as np


# Скорость движения;V;C
# Высота;H;C
# Плотность;Ro;C
# Давление на составную часть 1;P1;F
# Давление на составную часть 2;P2;F
# Давление на составную часть 4;P4;F
class Functions(ABC):
    type_of_funcs = 0

    @abstractmethod
    def createStr(self):
        pass

    @abstractmethod
    def createStrSecond(self):
        pass


class FirstExample(Functions):

    def func1(self, x1: float, x2: float, x3: float) -> float:  # функция типа "синусоида", без периода
        return sin(x1 * x2 * x3) / (x1 ** 2 + x2 ** 2 + x3 ** 2 + 1)

    def func2(self, x1: float, x2: float, x3: float) -> float:
        return (x1 + x2 + x3) ** 5 * (1 - (x1 + x2 + x3)) ** 10  # функция типа "ступенька"

    def func3(self, x1: float, x2: float, x3: float) -> float:  # функция типа "выброс"
        return 1 / (2 * (np.pi * 2) ** (1 / 2)) * np.e ** (-(x1 + x2 + x3) ** 2 / 8)

    def __init__(self):
        self.type_of_funcs = 1

    def createStr(self, x1, x2, x3):
        s = ';'
        seq = (str(x1), str(x2), str(x3),
               str(self.func1(x1, x2, x3)),
               str(self.func2(x1, x2, x3)),
               str(self.func3(x1, x2, x3)))
        return (s.join(seq) + '\n')

    def createStrSecond(self, var_lst):
        s = ';'
        seq = (str(var_lst[0]), str(var_lst[1]), str(var_lst[2]),
               str(self.func1(var_lst[0], var_lst[1], var_lst[2])), str(abs(var_lst[3] - self.func1(var_lst[0], var_lst[1], var_lst[2]))),
               str(self.func2(var_lst[0], var_lst[1], var_lst[2])), str(abs(var_lst[4] - self.func2(var_lst[0], var_lst[1], var_lst[2]))),
               str(self.func3(var_lst[0], var_lst[1], var_lst[2])), str(abs(var_lst[5] - self.func3(var_lst[0], var_lst[1], var_lst[2]))))
        return (s.join(seq) + '\n')
