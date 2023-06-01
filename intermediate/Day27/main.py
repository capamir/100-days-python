import tkinter

class Calcute:
    def __init__(self):
        self.window = tkinter.Tk()
        self._screen_setup()
        
        self.create_enrty()
        self.create_label()
        self.create_button()

        self.window.mainloop()

    def _screen_setup(self):
        self.window.title("mile to km")
        self.window.config(padx=20, pady=20)


    def create_label(self):
        self.miles_label = tkinter.Label(text="Miles")
        self.miles_label.grid(column=2, row=0)

        self.is_equal_to_label = tkinter.Label(text="is equal to")
        self.is_equal_to_label.grid(column=0, row=1)

        self.km_result_label = tkinter.Label(text="0")
        self.km_result_label.grid(column=1, row=1)

        self.km_label = tkinter.Label(text="km")
        self.km_label.grid(column=2, row=1)

    def button_clicked(self):
        mile = float(self.input.get())
        km = round(mile * 1.609)
        self.km_result_label.config(text=f"{km}")

    def create_button(self):
        self.button = tkinter.Button(text="Calcute", command=self.button_clicked)
        self.button.grid(column=1, row=2)


    def create_enrty(self):
        self.input = tkinter.Entry(width=7)
        self.input.grid(column=1, row=0)


Calcute()