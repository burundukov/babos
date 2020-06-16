from tkinter import *

root = Tk()
root.geometry('420x400+200+100')
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

    name_entry.focus_set()

def calculate():
  summ = 0
  for i in check:
    summ += i

  first = summ/len(check)
  print('Средний чек ' + str(first) + ' рублей')

  person1 = []
  person2 = []
  for i in check:
    if i - first >= 0:
      person1.append(i - first)
      person2.append(0)
    else:
      person1.append(0)
      person2.append(first - i)

  # person1 - те, кто тртил деньги (имеет чек)
  # person2 - те, кто не имеет чека
  # person0 - Имена участников

  #Процесс вычисления:

  result = []

  for i in range(len(person1)):
    if person1[i] != 0:
      for j in range(len(person2)):
        if person2[j] == 0:
          continue
        else:
          delta = person1[i] - person2[j]
          if delta < 0:
            result.append('Человек ' + str(person0[j]) + ' платит человеку ' + str(person0[i]) + ' ' + str(person1[i]) + ' рублей')
            person2[j] = - delta
            person1[i] = 0
            break
          else:
            result.append('Человек ' + str(person0[j]) + ' платит человеку ' + str(person0[i]) + ' ' + str(person2[j]) + ' рублей')
            person2[j] = 0
            person1[i] = delta
    else:
      continue

  consol_2 = f"Средний чек {first} рублей" + '\n' + '\n' + '\n'
  for i in result:
    consol_2 += (i + '\n')
  out_label.config(text=consol_2)

def clear():
    person0.clear()
    check.clear()
    consol = ""

button1 = Button(root, text = 'Подсчитать', bg = 'pink', command = calculate)
button1.grid(row=0, column=1)

button2 = Button(root, text='внести данные', bg = 'yellow', command = finished)
root.bind('<Return>', lambda event: finished())
button2.grid(row=3, column=1)

button_3 = Button(root, text = "Сброс", bg = 'pink', command = clear)
button_3.grid(row = 0, column = 0)

out_label = Label(wraplength=250)
out_label.grid(row=4, column=1, padx=5, pady=5)


root.mainloop()
