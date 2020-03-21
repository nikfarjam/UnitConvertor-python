class UnitCategory:
    def __init__(self,name,items):
        self.name = name
        self.items = items

temperature = UnitCategory('temperature', ('celsius', 'fahrenheit'))
length = UnitCategory('length', ('metre', 'foot'))
unit_categories = (temperature, length)