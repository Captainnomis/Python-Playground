class Car:
    def drive(self):
        print(f"This {self.model} is driving")
    def stop(self):
        print(f"This {self.model} is stopped")
        
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year    
        self.color = color
        
car_1 = Car("Chevy", "Corvette", 2021, "blue")

print(car_1.make)
car_1.drive()
car_1.stop()