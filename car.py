class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def greet(self):
       print(f"the car name is {self.name}and its model is {self.model}")

car1=Car("toyota","corolla")
car1.greet()

