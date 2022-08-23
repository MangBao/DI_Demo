class Car:
    def __init__(self, name: str, speed: int, wheel: int) -> None:
        self.name = name
        self.speed = speed
        self.wheel = wheel

class Glass:
    def getGlassFunc(self):
        return "This glass !"

class Mercedes:
    def __init__(self, car: Car, color: str):
        self.car = car
        self.color = color

    def getGlass(self):
        glass = Glass.getGlassFunc(self)
        return glass

car = Car("Mercedes", 180, 4)
mercedes = Mercedes(car, "white")

print(f"""
            Car name: {mercedes.car.name}
            Max speed: {mercedes.car.speed} km/h
            Wheel: {mercedes.car.wheel}
            Color: {mercedes.color}
            Has glass: {mercedes.getGlass()}
    """)
