class Vehicle:
    def __init__(self):
        self.speed = 0
       # self.color = "white"

    def move(self):
        print(f"Машина двигается со скоростью {self.speed}")

    def info(self):
        print(f"Цвет машины {self.color}")


class Car(Vehicle):
    def __init__(self):
        self.speed = 100

car = Car()
car.move()
#car.info()