from tkinter import *
import biz_logic


class Application(Frame):
    """ GUI App class """

    def __init__(self):

        # Initialising window
        self.root = Tk()
        self.root.title('Расчёт длины припоя')
        self.root.geometry('370x370')

        super(Application, self).__init__()
        self.grid()
        self.create_widgets()

        # Starts main loop
        self.root.mainloop()

    def create_widgets(self):
        """Initialises and creates widgets for GUI"""

        # Header
        Label(self, text='Параметры проволоки припоя:').grid(row=0, sticky=W)

        # Input box for entering wire thickness
        self.lbl_ask_thickness = Label(self, text='Введите толщину проволоки: ').grid(row=1, column=0, sticky=W)
        self.ask_thickness = Entry(self)
        self.ask_thickness.grid(row=1, column=1, sticky=W)

        # Checkbox for swirl
        self.check_swirl = BooleanVar()
        Checkbutton(self, text='Закрутка', variable=self.check_swirl).grid(row=2, column=0, sticky=W)

        # Radiobutton for choosing seam shape
        Label(self, text='Выберите форму спая:').grid(row=3, column=0, columnspan=2, sticky=W)
        self.seam_shape = StringVar()
        self.seam_shape.set(None)
        Radiobutton(self, text='Круглая', variable=self.seam_shape, value='circular', command=self.update_menu
                    ).grid(row=4, column=0, sticky=W)
        Radiobutton(self, text='Прямоугольная', variable=self.seam_shape, value='rectangular', command=self.update_menu
                    ).grid(row=4, column=1, sticky=W)
        self.start_lbl_empty = Label(self, text='\n\n')
        self.start_lbl_empty.grid(row=5, rowspan=3, column=0, sticky=W)

        # Initialises widgets for rectangular seam shape
        self.lbl_circ_ask_diam = Label(self, text='Введите диаметр: ')
        self.ask_circ_diam = Entry(self)
        self.lbl_empty = Label(self, text='\n')

        # Initialises widgets for rectangular seam shape
        self.lbl_rect_ask_length = Label(self, text='Введите длину: ')
        self.ask_rect_length = Entry(self)
        self.lbl_rect_ask_width = Label(self, text='Введите ширину: ')
        self.ask_rect_width = Entry(self)
        self.lbl_rect_ask_curvature_radius = Label(self, text='Введите радиус скругления: ')
        self.ask_rect_curvature_radius = Entry(self)

        # Calculate button
        self.bttn_calcultate = Button(self, text='Рассчитать', command=self.calculate)
        self.bttn_calcultate.grid(row=9, column=0, sticky=W)

        # Results output box
        self.results_text = Text(self, width=50, height=10, wrap=WORD)
        self.results_text.grid(row=10, column=0, columnspan=4)

    def update_menu(self):
        """Updates interface depending on chosen parameters"""
        # Deletes widgets when choosing seam shape
        self.clean_menu()

        # Creates widgets for circular seam shape
        if self.seam_shape.get() == 'circular':
            self.lbl_circ_ask_diam.grid(row=5, column=0, sticky=W)
            self.ask_circ_diam.grid(row=5, column=1, sticky=W)
            self.lbl_empty.grid(row=6, rowspan=2, column=0, sticky=W)

        # Creates widgets for rectangular seam shape
        elif self.seam_shape.get() == 'rectangular':
            self.lbl_rect_ask_length.grid(row=5, column=0, sticky=W)
            self.ask_rect_length.grid(row=5, column=1, sticky=W)
            self.lbl_rect_ask_width.grid(row=6, column=0, sticky=W)
            self.ask_rect_width.grid(row=6, column=1, sticky=W)
            self.lbl_rect_ask_curvature_radius.grid(row=7, column=0, sticky=W)
            self.ask_rect_curvature_radius.grid(row=7, column=1, sticky=W)

    def clean_menu(self):
        """Очистка от виджетов"""
        self.start_lbl_empty.grid_forget()
        self.lbl_circ_ask_diam.grid_forget()
        self.ask_circ_diam.grid_forget()
        self.lbl_empty.grid_forget()
        self.lbl_rect_ask_length.grid_forget()
        self.ask_rect_length.grid_forget()
        self.lbl_rect_ask_width.grid_forget()
        self.ask_rect_width.grid_forget()
        self.lbl_rect_ask_curvature_radius.grid_forget()
        self.ask_rect_curvature_radius.grid_forget()
        self.results_text.delete(0.0, END)

    def print_to_box(self, text):
        """Prints text in results window"""
        self.results_text.delete(0.0, END)
        self.results_text.insert(0.0, text)

    def calculate(self):
        message = biz_logic.calculations(thickness=self.ask_thickness.get(),
                                         if_swirl=self.check_swirl.get(),
                                         seam_shape=self.seam_shape.get(),
                                         diam=self.ask_circ_diam.get(),
                                         rect_length=self.ask_rect_length.get(),
                                         rect_width=self.ask_rect_width.get(),
                                         curvature_radius=self.ask_rect_curvature_radius.get())
        self.print_to_box(message)


app = Application()
