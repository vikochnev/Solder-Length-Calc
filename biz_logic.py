import math

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


def prepare_to_calc(thickness, if_swirl, seam_shape, diam, rect_length, rect_width, r_rad):
    """Обработка введенных пользователем значений, запуск функции расчёта длины"""

    # Конвертация значений в числа, обработка ошибки корректного ввода
    try:
        # # Обнуление значений для корректной обработки ошибок ввода
        #     diam = ''
        #         rect_length = ''
        #         rect_width = ''
        #         r_rad = ''
        #         thickness = ''

        # Проверка на закрутку
        if if_swirl == True:
            swirl = SWIRL
        else:
            swirl = 0

        # Получение параметров для круглого спая
        if seam_shape == 'circular':
            calculate(thickness=float(thickness), swirl=swirl, seam_shape=seam_shape, diam=float(diam))
        # Получение параметров для прямоугольного спая
        elif seam_shape.get() == 'rectangular':
            calculate(thickness=float(thickness), swirl=swirl, seam_shape=seam_shape, rect_length=float(rect_length),
                      rect_width=float(rect_width), r_rad=float(r_rad))

    except:
        return 'Ошибка: Введите все значения как числа'


def calculate(thickness, swirl, seam_shape, diam, rect_length, rect_width, r_rad):
    """Функция расчёта и вывода на экран длины припоя"""
    if seam_shape.get() == 'circular':
        # Проверка, что все параметры положительны
        if diam <= 0:
            return 'Ошибка: Значения всех параметров должны быть больше нуля'
        else:
            # Формула: pi*(diam+wire_thickness)
            print_results = round(math.pi * (diam + thickness) + swirl, 1)
            results_message(print_results)
    elif seam_shape.get() == 'rectangular':
        # Проверка, что все параметры положительны
        if min(rect_length, rect_width, r_rad) <= 0:
            return 'Ошибка: Значения всех параметров должны быть больше нуля'
        # Проверка на случай, если радиус скругления больше половины любой из сторон
        elif min(rect_length, rect_width) < 2 * r_rad:
            return 'Ошибка: Радиус скругления не может быть больше половины любой из сторон'
        else:
            # Формула: 2(a-2*r_rad) + 2(b-2*r_rad) + 2*pi*(r_rad + wire_thickness/2)
            print_results = round(
                2 * (rect_length - 2 * r_rad) \
                + 2 * (rect_width - 2 * r_rad) + \
                2 * math.pi * (r_rad + 0.5 * thickness) + \
                swirl,
                1)
            # Проверяет, если радиус скругления меньше толщины проволоки,
            # чтобы выдать предупреждение о плохой конструкции места спая
            if r_rad < thickness:
                results_message(print_results, if_warning=True)
            else:
                results_message(print_results)


def results_message(sol_length, if_warning=False):
    """"Обрабатывает рассчитанный результат и выводит его в окне результатов"""
    if if_warning == False:
        message = f'Длина проволоки: {str(sol_length)}\nДопуск длины: {str(solder_var(sol_length))}'
    else:
        message = f'Предупреждение: Радиус скругления меньше толщины проволоки! \
        \nДлина проволоки: {str(sol_length)} \
        \nДопуск длины: {str(solder_var(sol_length))}'
    return (message)
