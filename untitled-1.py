with open("26-6.txt") as F:
  s, n = map(int, F.readline().split()) # строку файла превращаем в 2 числа
# s  - свободное место на диске
# n -  кол-во пользователей

  a = [] # массив хранения всех объемов из файла
  for i in range(n):
    obiem = F.readline()  # очередной объем (строка файла)
    a.append(int(obiem)) #  строку превратили в число и добавили в массив

  a.sort() # сортировка по возрастанию  
  summa = 0 # текущая сумма объемов пользователей 
  k = 0 # счетчик пользователей
  Max = 0 # максимальный размер сохраненного файла
  for i in range(n): 
      """ если текущая сумма и следующий объем не превышает
свободное место, то суммируем такой объем, запоминаем макс объем
и считаем кол-во пользователей
"""
      if s >= summa + a[i]: 
        summa += a[i]
        k += 1
        Max = a[i]
      else: # превысили объем, поэтому вычитаем последний учтенный объем (Max)
        summa = summa - Max + a[i]
        if s >= summa: # запоминаем новый максимум    
           Max = a[i]
        
  print(k,Max)
    