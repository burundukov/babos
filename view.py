from tkinter import *

root = Tk()
#root.geometry('600x400+200+100')
root.title("Babos")

l = Label(root, bg='black', fg='white', width=100, text="Сколько человек было?")
e = Entry(root, width=100, justify = CENTER)
b = Button(root, text="Посчитать", bg='yellow')


b.bind('<Button-1>')

l.pack()
e.pack()
b.pack()

root.mainloop()