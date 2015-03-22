from inheritance_car_class import OurCar
from inheritance_car_class import ExampleCar
##x = car()
make = 'Ford'
model = 'Fusion'
year = '2011'
x = OurCar(make, model, year)
print 'make', x.make
print 'model', x.model
print 'year', x.year

x.set_color('maroon')

print 'color', x.color

##############
new_car = ExampleCar(make = 'Ford', model = 'Focus', year = '2011')
print new_car.make
print new_car.model
print new_car.year
print new_car.color
print new_car.plate