# benedict musa
# 23/2/2026
# program to classes in python

class Car():
    # attributtes of the car
    def __init__(self,colour,model,make,year):
        self.model = model 
        self.make = make
        self.colour = colour
        self.year = year

    # print car details
    def print_details(self,model,make,colour,year):
     print(f"{model} of colour {colour} was manufactured in the year {year}")



#instantiate a class object

my_car = Car("Atenza","Pagani","navy blue","2023")
dads_car = Car("Atenza","ferrari","green","2016")

my_car.print_details("Atenza","Pagani","navy blue","2023")
