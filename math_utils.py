def is_float(value):
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False