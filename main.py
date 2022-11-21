from tkinter import *
import biz_logic




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
        self.bttn_calcultate = Button(self, text='Рассчитать', command=self.calculate())
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
        pass
        self.results_text.delete(0.0, END)
        self.results_text.insert(0.0, text)


    def calculate(self):
        if self.seam_shape.get() not in ('circular', 'rectangular'):
            self.print_to_box('Ошибка: Выберите форму спая')
        elif self.seam_shape.get() == 'circular':
            output = biz_logic.prepare_to_calc(thickness=self.ask_thickness.get(), if_swirl=self.check_swirl,
                                      seam_shape='circular', diam=self.ask_circ_diam.get())
            # self.print_to_box(str(output))
        elif self.seam_shape.get() == 'rectangular':
            output = biz_logic.prepare_to_calc(thickness=self.ask_thickness.get(), seam_shape='rectangular',
                                      rect_length=self.ask_rect_length.get(), rect_width=self.ask_rect_width.get())
            # self.print_to_box(str(output))
        else:
            pass
            # self.print_to_box('Ошибка: неожиданная ошибка')








app = Application()
