class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed