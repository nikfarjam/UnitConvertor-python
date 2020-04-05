import converter_utils
from math_utils import is_float

class InvalidInputError(Exception):
   """Raised when the input value is not valid"""
   pass

class UnitConverter:
    def __init__(self, input):
        super().__init__()
        self.input = input

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input):
        self.validate_input(input)
        self._input = input

    def validate_input(self, input):
        if 'value' not in input:
            raise InvalidInputError('Value is empty')
        if 'category' not in input:
            raise InvalidInputError('Unit category is empty')
        if 'units' not in input:
            raise InvalidInputError('Units is empty')
        if not is_float(input['value']):
            raise InvalidInputError('Value is not a valid number')

    def get_value(self):
        return self.input['value']
    
    def get_operation(self):
        return 'celsius_to_fahrenheit'
    
    def calculate(self):
        value_as_flat = float(self.get_value())
        operation = self.get_operation()
        function = getattr(converter_utils, operation)
        result = function(value_as_flat)
        return result
