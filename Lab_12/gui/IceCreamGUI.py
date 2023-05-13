from tkinter import Tk, Listbox, mainloop, END, Frame, Label


class IceCreamGUI:
    def __init__(self, ice_cream_stand):
        self.ice_cream_stand = ice_cream_stand

        self.window = Tk()

        self.window.title(ice_cream_stand.restaurant_name)

        frm = Frame(self.window)
        frm.grid()

        Label(frm, text=ice_cream_stand.restaurant_name).grid(column=0, row=0)
        Label(frm, text=ice_cream_stand.location).grid(column=0, row=1)
        Label(frm, text=ice_cream_stand.work_time).grid(column=0, row=2)
        self.listbox = Listbox(frm)
        self.listbox.grid(column=0, row=3)
        self.update_flavors()
        mainloop()

    def update_flavors(self):
        flavors = self.ice_cream_stand.get_flavors()
        self.listbox.delete(0, END)
        for flavor in flavors:
            self.listbox.insert(END, flavor)
