import converter_utils
from math_utils import is_float

class InvalidInputError(Exception):
   """Raised when the input value is not valid"""
   pass

class UnitConverter:
    def __init__(self, event):
        super().__init__()
        self.event = event

    def validate_input(self):
        if 'value' not in self.event:
            return 'Value is empty'
        if 'category' not in self.event:
            return 'Unit category is empty'
        if 'units' not in self.event:
            return 'Units is empty'
        if not is_float(self.event['value']):
            return 'Value is not a valid number'
        return ''

    def get_value(self):
        return self.event['value']
    
    def get_operation(self):
        return 'celsius_to_fahrenheit'
    
    def calculate(self):
        validation_message = self.validate_input()
        if validation_message != '':
            raise InvalidInputError(validation_message)

        _value_as_flat = float(self.get_value())
        operation = self.get_operation()
        _function = getattr(converter_utils, operation)
        result = _function(_value_as_flat)
        return result
