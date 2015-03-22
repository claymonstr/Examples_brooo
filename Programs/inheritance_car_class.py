class car:

    def __init__(self):
        self.make = ''
        self.model = ''
        self.year = ''

    def set_color(self, color):
        self.color = color

class OurCar(car):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def set_plate(self, plate):
        self.plate = plate

class ExampleCar(object):
    __slots__ = (
        'make',
        'model',
        'year',
        'color',
        'plate'
    )

    def __init__(self, **kwargs):
        self.make = kwargs.get('make', '')
        self.model = kwargs.get('model', '')
        self.year = kwargs.get('year', '')
        self.color = kwargs.get('color', 'Red')
        self.plate = kwargs.get('plate', 'flash')
##        self.tire = kwargs.get('tire', 'goodyear')