

def calculate(check):
  summ = 0
  for i in check:
    summ += i

  first = summ/n
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

  for i in result:
    print(i)

print('Введите количество человек')
n = int(input())

check =[]
person0 =[]

# Ввод данных:

for i in range(n):
  print("Введите имя")
  a = str(input())
  person0.append(a)
  print('Сколько ' + a + ' потратил?')
  b = float(input())
  check.append(b)


calculate(check)
