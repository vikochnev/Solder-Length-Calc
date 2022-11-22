SWIRL = 11

def solder_var(sol_length):
    """Задаёт допуска по ЕСКД в зависимости от длины проволоки"""
    if sol_length >= 400:
        return -1.55
    elif sol_length >= 315:
        return -1.4
    elif sol_length >= 250:
        return -1.3
    elif sol_length >= 180:
        return -1.15
    elif sol_length >= 120:
        return -1
    elif sol_length >= 80:
        return -0.87
    elif sol_length >= 50:
        return -0.74
    elif sol_length >= 30:
        return -0.62
    elif sol_length >= 18:
        return -0.52
    elif sol_length >= 10:
        return -0.43
    elif sol_length >= 6:
        return -0.36
    elif sol_length >= 3:
        return -0.3
    else:
        return -0.25