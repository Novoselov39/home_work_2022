class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weight=25, thickness=5):
        print(f'Масса дороги равна: {self._length * self._width * weight * thickness/1000}')



Road1 = Road(5000,20)
Road1.mass()