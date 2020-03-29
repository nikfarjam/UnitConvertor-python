def celsius_to_fahrenheit(celsius, fraction = 2):
    if celsius:
        return round((celsius * 9 / 5 ) + 32, fraction)
    return float('nan')
