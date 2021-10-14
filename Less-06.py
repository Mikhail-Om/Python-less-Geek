# Практическое задание к шестой лекции
#
#
#Задание 1
#
# Создать класс TrafficLight (светофор). 
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния 
# (красный) составляет 7 секунд, 
# второго (жёлтый) — 2 секунды, 
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
 
# Задачу можно усложнить, реализовав проверку порядка режимов. 
# При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time
class TrafficLight:
    __color = 1
    Color_dict = {'Красный': 7,'Желтый': 2,'Зеленый': 14}
    __color = 1
    __color_index = 0
    change_color = 6
    
    def running(self):
        
        return color


#
#Задание 2
#
# Реализовать класс Road (дорога).
 
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра 
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
 
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    weight_1m = 25
    
    
    def __init__(self, L, W):
        self._L = L
        self._W = W
    def road_mass(self, depth):
        return depth * self.weight_1m * self._W * self._L
road_rez = Road(5000, 20)
print("Дорога длиной ", road_rez._L, "м и шириной ", road_rez._W, " весит ",road_rez.road_mass(5) ,"КГ")
        


#
#Задание 3
#
# Реализовать базовый класс Worker (работник).
 
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: 
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

        
class Position(Worker):

    def __init__(self,  name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'ФИО: {self.surname} {self.name}'

    def get_total_income(self):
        return sum(self._income.values())    
    
worker_temp = Position("Test_Name","Test_surname","Test_poz",100000,50000)
print(worker_temp.get_full_name(), f'Total income: {worker_temp.get_total_income()}', worker_temp._income )

#
#Задание 4
#
# Реализуйте базовый класс Car.
 
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
# Вызовите методы и покажите результат.

class Car:
    __speed = 0
    __direction = None
    
    def __init__(self, speed, color, name, is_polis):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True
        
    def go(self):
        self.speed = self.__speed
        
    def stop(self):
        self.speed = 0
        
    def turn(self, direction):
        pass
        
    def show_speed(self):
        print(f'Скорость автомобиля {self.name} : {self.speed} км/ч')

class TownCar(Car):
    max_speed = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

        
class WorkCar(Car):
    max_speed = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.max_speed:
            print(f'Превышение скорости автомобилем {self.name}!')
        print(f'Текущая скорость автомобилья {self.name}: {self.speed}км/ч')     

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

pol_car = PoliceCar(120, 'blue', 'polli_car')
w_car = WorkCar(20, 'blue', 'job_job')
sprt_c = SportCar(200, 'rad', 'Nic')
town_c = TownCar(90, 'gray', 'TTT')

pol_car.show_speed()
pol_car.go()
pol_car.show_speed()
pol_car.stop()
print(pol_car.color)
print(pol_car.name)

w_car.show_speed()
w_car.go()
w_car.show_speed()
w_car.stop()
print(w_car.color)
print(w_car.name)

    
#
#Задание 5
#
# Реализовать класс Stationery (канцелярская принадлежность). 
# определить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self):
        super().__init__('ручка')

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Pencil(Stationery):

    def __init__(self):
        super().__init__('карандаш')

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Handle(Stationery):

    def __init__(self):
        super().__init__('маркер')

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')
    p= Pen()
    n = Pencil()
    h = Handle()
    s = Stationery('канцелярская принадлежность')

    p.draw()
    n.draw()
    h.draw()       


