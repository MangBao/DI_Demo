class Car:
    def __init__(self, name: str, speed: int, wheel: int) -> None:
        self.name = name
        self.speed = speed
        self.wheel = wheel

class Mercedes:
    def __init__(self, car: Car, color: str) -> None:
        self.car = car
        self.color = color

car = Car("Mercedes", 180, 4)
mercedes = Mercedes(car, "white")

print(f"""
            Car name: {mercedes.car.name}
            Max speed: {mercedes.car.speed} km/h
            Wheel: {mercedes.car.wheel}
            Color: {mercedes.color}
    """)
