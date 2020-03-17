from unit_categoy import unit_categories

def lambda_handler(event, context):
    for categoy in unit_categories:
        print(categoy.name)