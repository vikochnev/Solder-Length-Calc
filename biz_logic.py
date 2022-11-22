import math
import constants


def calculations(thickness, if_swirl, seam_shape, diam, rect_length, rect_width, curvature_radius):
    """Takes parameters, organizes calculation logic"""

    # Checks for swirl
    if if_swirl:
        swirl = constants.SWIRL
    else:
        swirl = 0

    # Checks if seam shape is picked
    if seam_shape not in ('circular', 'rectangular'):
        return 'Ошибка: Выберите форму спая'

    # Checks if all parameters in input boxes are numbers, calls calculation functions depending on seam shape
    try:
        if seam_shape == 'circular':
            message = calculate_circular(thickness=float(thickness),
                               swirl=float(swirl),
                               diam=float(diam))
            return message

        elif seam_shape == 'rectangular':
            message = calculate_rectangular(thickness=float(thickness),
                                  swirl=float(swirl),
                                  rect_length=float(rect_length),
                                  rect_width=float(rect_width),
                                  curvature_radius=float(curvature_radius))
            return message

        else:
            return 'Ошибка: неожиданная ошибка'
    except:
        return 'Ошибка: Введите все значения как числа'


def calculate_circular(thickness, swirl, diam):
    """Calculates wire length for circular seam shape"""

    # Checks if all parameters are positive
    if min(thickness, diam) <= 0:
        return 'Ошибка: Значения всех параметров должны быть больше нуля'

    # returns calculation results
    else:
        # Формула: pi*(diam+wire_thickness)
        results = round(math.pi * (diam + thickness) + swirl, 1)
        return results_message(results)


def calculate_rectangular(thickness, swirl, rect_length, rect_width, curvature_radius):
    """Calculates wire length for rectangular seam shape"""

    # Checks if all parameters are positive
    if min(thickness, rect_length, rect_width, curvature_radius) <= 0:
        return 'Ошибка: Значения всех параметров должны быть больше нуля'

    # Checks if curvature radius is greater than any of rectangle sides
    elif min(rect_length, rect_width) < 2 * curvature_radius:
        return 'Ошибка: Радиус скругления не может быть больше половины любой из сторон'

    # Calculates wire length
    else:
        # Формула: 2(a-2*curvative_radius) + 2(b-2*curvative_radius) + 2*pi*(r_rad + wire_thickness/2)
        results = round(2 * (rect_length - 2 * curvature_radius) +
                        2 * (rect_width - 2 * curvature_radius) +
                        2 * math.pi * (curvature_radius + 0.5 * thickness) +
                        swirl)

        # Checks if curvature_radius is less than wire thickness, adds warning to results
        if curvature_radius < thickness:
            return results_message(results, if_warning=True)

        # returns calculation results
        else:
            return results_message(results)


def results_message(sol_length, if_warning=False):
    """"Обрабатывает рассчитанный результат и выводит его в окне результатов"""
    if if_warning == False:
        message = f'Длина проволоки: {str(sol_length)}\nДопуск длины: {str(constants.solder_var(sol_length))}'
    else:
        message = f'Предупреждение: Радиус скругления меньше толщины проволоки! \
        \nДлина проволоки: {str(sol_length)} \
        \nДопуск длины: {str(constants.solder_var(sol_length))}'
    return message

