import time

class TrafficLight:

    def running(self):
        self.__color = 'red'
        print(f'\r\033[41m{self.__color}\033[0m', end='')
        time.sleep(7)
        self.__color = 'yelow'
        print(f"\r\033[43m{self.__color}\033[0m", end='')
        time.sleep(2)
        self.__color = 'green'
        print(f"\r\033[42m{self.__color}\033[0m", end='')
        time.sleep(7)
        print(f"\r\033[0m ", end='')


TrafficLight1 = TrafficLight()
TrafficLight1.running()