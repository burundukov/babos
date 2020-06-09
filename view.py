from tkinter import *

root=Tk()
root.geometry('500x400+200+100')
root.title('Babos')

person0 = []
check = []

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
    check.append(float(cash.get()))
    person0.append(name.get())
    print(person0)
    print(check)
    name_entry.delete(0, END)
    cash_entry.delete(0, END)

button1=Button(root, text='Добавить участника', bg = 'pink')
button1.grid(row=0, column=1)

#button1.bind('<Button-1>', added)



button2 = Button(root, text='внести данные', bg = 'yellow', command = finished)
button2.grid(row=3, column=1)


#consol = Label(root, bg='#b8b894', fg='white', text=person0)

out_label = Label(textvariable = name, wraplength=250, bg = 'pink')
out_label.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()