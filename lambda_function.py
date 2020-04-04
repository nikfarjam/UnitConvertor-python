import json
from unit_converter import UnitConverter, InvalidInputError

def lambda_handler(event, context):
    print('event', event)
    uc = UnitConverter(event)
        
    try:
        result = uc.calculate()
    except InvalidInputError as error:
        return {
            'statusCode': 400,
            'body': {
                'message': str(error)
            },
            'header': {
                'content-type': 'application/json'
            },
            'input': event
        }
    print('Result is ', result)

    return {
        'statusCode': 200,
        'body': {
            'celsius': str(event['value']),
            'fahrenheit': str(result)
        },
        'header': {
            'content-type': 'application/json'
        },
        'input': event
    }
