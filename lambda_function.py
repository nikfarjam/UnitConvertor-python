import json
import logging
import converter_utils
from math_utils import isFloat

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_input(event):
    if 'value' not in event:
        return 'Value is empty'
    if 'category' not in event:
        return 'Unit category is empty'
    if 'units' not in event:
        return 'Units is empty'
    if not isFloat(event['value']):
        return 'Value is not a valid number'
    return ''


def lambda_handler(event, context):
    print('event', event)
    validation_message = validate_input(event)
    if validation_message != '':
        message = str(validation_message)
        return {
            'statusCode': 400,
            'body': {
                'message': message
            },
            'header': {
                'content-type': 'application/json'
            },
            'input': event
        }

    celsius = float(event['value'])
    fahrenheit = getattr(converter_utils, 'celsius_to_fahrenheit')(celsius)
    print('Result is ', fahrenheit)

    return {
        'statusCode': 200,
        'body': {
            'celsius': str(celsius),
            'fahrenheit': str(fahrenheit)
        },
        'header': {
            'content-type': 'application/json'
        },
        'input': event
    }
