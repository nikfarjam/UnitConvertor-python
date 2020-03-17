class UnitCategory:
    def __init__(self,name,items):
        self.name = name
        self.items = items

temperature = UnitCategory('temperature', ('celsius_to_fahrenheit', 'fahrenheit_to_celsius'))
length = UnitCategory('length', ('metre_to_foot', 'metre_to_foot'))
unit_categories = (temperature, length)