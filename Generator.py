import random

from FirstExample import FirstExample


class Generator:
    num_of_points = 0
    type_of_example = 0
    lst_of_examples = [['Скорость движения;V;C',
                        'Высота;H;C',
                        'Плотность;Ro;C',
                        'Давление на составную часть 1;P1;F',
                        'Давление на составную часть 2;P2;F',
                        'Давление на составную часть 4;P4;F']]

    def __init__(self):
        pass

    def readMeta(self) -> int:
        meta = open("meta.csv", 'r', encoding='utf-8')
        # print("Соответствующая метаинформация: ")
        lines = meta.read().splitlines()  # читаем строку из файла без последнего \n, получили список строк
        pos = self.lst_of_examples.index(lines) + 1
        if (pos == 1):
            print('Необходимо использовать FirstExample')
            self.type_of_example = 1
            meta.close()
            return 1
        lines = [str.split(";") for str in lines]  # получили 5 списков по 3 значения

    def readAtoAData(self) -> list:
        atoMData = open("AtoMData.csv", 'r', encoding='utf-8')
        print("Необходимы повторные замеры в точках: ")
        lines = atoMData.read().splitlines()  # читаем строку из файла без последнего \n, получили список строк
        lines = [st.split(";") for st in lines]  # получили 2 списка по 2 значения
        print(lines)
        atoMData.close()
        return lines

    def firstGenerate(self, num_of_points: int):
        mtoAData = open("MtoAData.csv", 'w', encoding='utf=8')
        if (self.type_of_example == 1):
            x1_lst = [] # TODO: как то вынести этот блок
            x2_lst = []
            x3_lst = []
            f_ex = FirstExample()
            for i in range(num_of_points):
                x1_lst.append(random.randint(0, 100))  # здесь можно задание своих координат, временно
                x2_lst.append(random.randint(0, 50))  # здесь можно задание своих координат, временно
                x3_lst.append(random.randint(0, 50))
                # print(createStr(v_lst[i], h_lst[i]))
                mtoAData.write(f_ex.createStr(x1_lst[i], x2_lst[i], x3_lst[i]))
        mtoAData.close()

    def secondGenerate(self):
        outPutData = open("OutPutData.csv", 'w', encoding='utf=8')
        if (self.type_of_example == 1):
            lst_of_coords = Generator.readAtoAData(self)
            f_ex = FirstExample()
            for lst in lst_of_coords:
                outPutData.write(f_ex.createStrSecond([int(elem) for elem in lst]))
        outPutData.close()


generator = Generator()
generator.readMeta()  # читали мета информацию и определили какими дальше функциями нужно пользоваться
generator.firstGenerate(10)  # ввели только количество точек
generator.secondGenerate()
