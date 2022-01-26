class Car:
    # dunder init method, set a max_speed attribute
    # implement the following methods:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.speed = 0
        self.limit = 0

    # accelerate
    # brake

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        # if self.speed + speed_increase > self.max_speed:
        #     self.speed = self.max_speed
        # else:
        #     self.speed += speed_increase
        self.speed = min(self.max_speed, self.speed + speed_increase)

    def brake(self, speed_decrease):
        # if self.speed - speed_decrease < 0
        #     self.speed = 0
        # else:
        #     self.speed -= speed_decrease

        self.speed = min(0, self.speed - speed_decrease)




    # what happens if you aceelerate beyond the max speed?
    # what happens if you brake past 0 mph?



car = Car(100)
print(car.speed)
car.accelerate(50)
print(car.speed)
car.accelerate(300000)
print(car.speed)
