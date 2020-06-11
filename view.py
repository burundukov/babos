from tkinter import *

root = Tk()
root.geometry('500x400+200+100')
root.title('Babos')

person0 = []
check = []

person_out = []     #Список для отображения введенных данных

name = StringVar()
cash = StringVar()


name_label = Label(text="Введите имя:")
cash_label = Label(text="Введите сумму:")
name_label.grid(row=1, column=0, sticky="w")
cash_label.grid(row=2, column=0, sticky="w")

name_entry = Entry(root, width=50, justify=CENTER, textvariable=name)
cash_entry = Entry(root, width=50, justify=CENTER, textvariable=cash)
name_entry.grid(row=1, column=1, padx=5, pady=5)
cash_entry.grid(row=2, column=1, padx=5, pady=5)


def finished():

    consol = ""

    check.append(float(cash.get()))
    person0.append(name.get())
    person_out.append(name.get() + " заплатил " + cash.get())
    print(person0)
    print(check)

    for i in person_out:
        consol += (i + '\n')

    name_entry.delete(0, END)
    cash_entry.delete(0, END)
    out_label.config(text = consol)

button1=Button(root, text = 'Подсчитать', bg = 'pink')
button1.grid(row=0, column=1)

#button1.bind('<Button-1>', added)



button2 = Button(root, text='внести данные', bg = 'yellow', command = finished)
button2.grid(row=3, column=1)

out_label = Label(wraplength=250)
out_label.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()