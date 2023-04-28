#Задание 1
#перебрать числа от 1 до 100
#если число делится на 3 - вывести вместо него Fizz
#если на 5 - вывести вместо него Buzz
#если и на 3 и на 5 - вывести вместо него FizzBuzz

#for i in range(1, 101):
#    if i % 3 == 0 and i % 5 == 0:
#        print("FizzBuzz")
#    elif i % 3 == 0:
#        print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(i)


#Задание 2
#Отсортировать 1й список по элементам 2го. Должно получиться [1, 6, 4]

#spisok1= [1, 4, 6]
#spisok2 = [11, 33, 22]
#a_sorted = sorted(spisok1, key=lambda x: spisok2[spisok1.index(x)])
#print(a_sorted)


#Задание 3
#Дан список строк.
#Нужно вывести все буквы, которые встречаются в каждой из строк списка, включая дубли

#spisok = ["cool","lock","cook"]
#x = set(spisok[0])
#for i in spisok[1:]:
#    x = x.intersection(set(i))
#    result = list(x)
#    result.sort()
#print(result)


#Задание 4
#Римские цифры представлены семью различными символами: I, V, X, L, C, D и M.
#Дана римская цифра, преобразовать ее в целое число

znachenie = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
rim_n = input('Введите римскую цифру: ')
result = 0
x = None

for symbol in rim_n:
    if x and znachenie[symbol] > znachenie[x]:
        result += znachenie[symbol] - 2 * znachenie[x]
    else:
        result += znachenie[symbol]
        x = symbol
print(result)