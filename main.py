from tkinter import *

PI = 3.1415926535897932384626433832795
SWIRL = 11


class Application(Frame):
    """ GUI приложение для расчёта длины припоя. """

    def __init__(self):

        # Инициализировать окно
        self.root = Tk()
        self.root.title('Расчёт длины припоя')
        self.root.geometry('370x370')

        super(Application, self).__init__()
        self.grid()
        self.create_widgets()

        # Создание main loop
        self.root.mainloop()

    def create_widgets(self):
        """Создание кнопок интерфейса"""

        # Часть интерфейса, отвечающая за параметры проволоки припоя
        Label(self, text='Параметры проволоки припоя:').grid(row=0, sticky=W)

        # Виджет для ввода толщины проволоки
        self.lbl_ask_thickness = Label(self, text='Введите толщину проволоки: ').grid(row=1, column=0, sticky=W)
        self.ask_thickness = Entry(self)
        self.ask_thickness.grid(row=1, column=1, sticky=W)

        # Чекбокс для закрутки
        self.check_swirl = BooleanVar()
        Checkbutton(self, text='Закрутка', variable=self.check_swirl).grid(row=2, column=0, sticky=W)

        # Часть интерфейса, отвечающая за выбор между круглой и прямоугольной формами спая
        Label(self, text='Выберите форму спая:').grid(row=3, column=0, columnspan=2, sticky=W)
        self.seam_shape = StringVar()
        self.seam_shape.set(None)
        Radiobutton(self, text='Круглая', variable=self.seam_shape, value='circular', command=self.update_menu
                    ).grid(row=4, column=0, sticky=W)
        Radiobutton(self, text='Прямоугольная', variable=self.seam_shape, value='rectangular', command=self.update_menu
                    ).grid(row=4, column=1, sticky=W)

        # Инициализация виджетов для круглой формы спая
        self.lbl_circ_ask_diam = Label(self, text='Введите диаметр: ')
        self.ask_circ_diam = Entry(self)
        self.lbl_empty = Label(self, text=" \n ")

        # Инициализация виджетов для прямоугольной формы спая
        self.lbl_rect_ask_length = Label(self, text='Введите длину: ')
        self.ask_rect_length = Entry(self)
        self.lbl_rect_ask_width = Label(self, text='Введите ширину: ')
        self.ask_rect_width = Entry(self)
        self.lbl_rect_ask_r_radius = Label(self, text='Введите радиус скругления: ')
        self.ask_rect_r_radius = Entry(self)

        # Кнопка для расчёта результатов
        self.bttn_calcultate = Button(self, text='Рассчитать', command=self.prepare_to_calc)
        self.bttn_calcultate.grid(row=9, column=0, sticky=W)

        # Окно с результатами
        self.results_text = Text(self, width=50, height=10, wrap=WORD)
        self.results_text.grid(row=10, column=0, columnspan=4)

    def update_menu(self):
        """Обновление интерфейса в зависимости от выбранной формы спая"""
        # Удаление виджетов
        self.clean_menu()

        # Создание виджетов для круглого спая
        if self.seam_shape.get() == 'circular':
            self.lbl_circ_ask_diam.grid(row=5, column=0, sticky=W)
            self.ask_circ_diam.grid(row=5, column=1, sticky=W)
            self.lbl_empty.grid(row=6, rowspan=2, column=0, sticky=W)
        # Создание виджетов для прямоугольного спая
        elif self.seam_shape.get() == 'rectangular':
            self.lbl_rect_ask_length.grid(row=5, column=0, sticky=W)
            self.ask_rect_length.grid(row=5, column=1, sticky=W)
            self.lbl_rect_ask_width.grid(row=6, column=0, sticky=W)
            self.ask_rect_width.grid(row=6, column=1, sticky=W)
            self.lbl_rect_ask_r_radius.grid(row=7, column=0, sticky=W)
            self.ask_rect_r_radius.grid(row=7, column=1, sticky=W)

    def clean_menu(self):
        """Очистка от виджетов"""
        self.lbl_circ_ask_diam.grid_forget()
        self.ask_circ_diam.grid_forget()
        self.lbl_empty.grid_forget()
        self.lbl_rect_ask_length.grid_forget()
        self.ask_rect_length.grid_forget()
        self.lbl_rect_ask_width.grid_forget()
        self.ask_rect_width.grid_forget()
        self.lbl_rect_ask_r_radius.grid_forget()
        self.ask_rect_r_radius.grid_forget()

    def print_to_box(self, text):
        """Выводит текст в окне результатов"""
        self.results_text.delete(0.0, END)
        self.results_text.insert(0.0, text)

    def solder_var(self, sol_length):
        """Задаёт допуска по ЕСКД в зависимости от длины проволоки"""
        if sol_length >= 400: return -1.55
        elif sol_length >= 315: return -1.4
        elif sol_length >= 250: return -1.3
        elif sol_length >= 180: return -1.15
        elif sol_length >= 120: return -1
        elif sol_length >= 80: return -0.87
        elif sol_length >= 50: return -0.74
        elif sol_length >= 30: return -0.62
        elif sol_length >= 18: return -0.52
        elif sol_length >= 10: return -0.43
        elif sol_length >= 6: return -0.36
        elif sol_length >= 3: return -0.3
        else: return -0.25

    def results_message(self, sol_length, if_warning = False):
        """"Обрабатывает рассчитанный результат и выводит его в окне результатов"""
        if if_warning == False:
            message = 'Длина проволоки: ' + str(sol_length) + '\nДопуск длины: ' + str(self.solder_var(sol_length))
        else:
            message = 'Предупреждение: Радиус скругления меньше толщины проволоки!\n' \
                      'Длина проволоки: ' + str(sol_length) + "\nДопуск длины: " + str(self.solder_var(sol_length))
        self.print_to_box(message)

    def prepare_to_calc(self):
        """Обработка введенных пользователем значений, запуск функции расчёта длины"""

        # Обработка ошибки выбора формы спая
        if self.seam_shape.get() not in ('circular', 'rectangular'):
            self.print_to_box('Ошибка: Выберите форму спая')
        else:
            # Конвертация значений в числа, обработка ошибки корректного ввода
            try:
                # Обнуление значений для корректной обработки ошибок ввода
                self.diam = ''
                self.rect_length = ''
                self.rect_width = ''
                self.r_rad = ''
                self.thickness = ''

                # Получение параметров для круглого спая
                if self.seam_shape.get() == 'circular':
                    self.diam = float(self.ask_circ_diam.get())
                # Получение параметров для прямоугольного спая
                elif self.seam_shape.get() == 'rectangular':
                    self.rect_length = float(self.ask_rect_length.get())
                    self.rect_width = float(self.ask_rect_width.get())
                    self.r_rad = float(self.ask_rect_r_radius.get())
                # Получение толщины проволоки припоя
                self.thickness = float(self.ask_thickness.get())

                # Проверка на закрутку
                if self.check_swirl.get() == True:
                    self.swirl = SWIRL
                else:
                    self.swirl = 0

                # Запуск расчёта в случае отсутствия ошибок
                self.calculate()

            except:
                self.print_to_box('Ошибка: Введите все значения как числа')

    def calculate(self):
        """Функция расчёта и вывода на экран длины припоя"""
        if self.seam_shape.get() == 'circular':
            # Проверка, что все параметры положительны
            if self.diam <= 0:
                self.print_to_box('Ошибка: Значения всех параметров должны быть больше нуля')
            else:
                # Формула: pi*(diam+wire_thickness)
                self.print_results = round(PI * (self.diam + self.thickness) + self.swirl, 1)
                self.results_message(self.print_results)
        elif self.seam_shape.get() == 'rectangular':
            # Проверка, что все параметры положительны
            if min(self.rect_length, self.rect_width, self.r_rad) <= 0:
                self.print_to_box('Ошибка: Значения всех параметров должны быть больше нуля')
            # Проверка на случай, если радиус скругления больше половины любой из сторон
            elif min(self.rect_length, self.rect_width) < 2 * self.r_rad:
                self.print_to_box('Ошибка: Радиус скругления не может быть больше половины любой из сторон')
            else:
                # Формула: 2(a-2*r_rad) + 2(b-2*r_rad) + 2*pi*(r_rad + wire_thickness/2)
                self.print_results = round(
                    2 * (self.rect_length - 2 * self.r_rad) \
                    + 2 * (self.rect_width - 2 * self.r_rad) + \
                    2 * PI * (self.r_rad + 0.5 * self.thickness) + \
                    self.swirl,
                    1)
                # Проверяет, если радиус скругления меньше толщины проволоки,
                # чтобы выдать предупреждение о плохой конструкции места спая
                if self.r_rad < self.thickness:
                    self.results_message(self.print_results, if_warning=True)
                else:
                    self.results_message(self.print_results)


app = Application()
