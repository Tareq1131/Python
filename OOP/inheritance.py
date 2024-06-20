class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def full_name(self):
          return f"{self.brand} {self.model}"
    
class Ele(Car):
     def __init__(self, brand, model, battery_size):
          super().__init__(brand, model)
          self.battery_size = battery_size
        

r = Car("Toyota", "d45")
ele = Ele("Toyota", "d45", '12v')
# print(r.model)
# print(r.brand)

# print(r.full_name())

print(ele.model)