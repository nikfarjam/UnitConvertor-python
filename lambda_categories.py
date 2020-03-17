from unit_category import unit_categories

def lambda_handler(event, context):
    result = {}
    for categoy in unit_categories:
        result[categoy.name] = list(categoy.items)
    return {
            'statusCode': 400,
            'body': result,
            'header': {
              'content-type': 'application/json'
            },
            'input': event
        } 