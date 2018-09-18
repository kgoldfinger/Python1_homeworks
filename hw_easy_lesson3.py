__author__ = 'Екатерина Гольдфингер'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    """

    :param number: десятичное число
    :param ndigits: количество знаков после запятой
    :return: число, округленное до заданного количества знаков после запятой
    """
    list1 = str(number).split('.')
    first =  list1[0]
    second = list1[1]
    second_cut = int('1'+second[:ndigits])
    first_number_in_second = int(str(second_cut)[1])
    if int(second[ndigits+1]) >= 5:
       second_cut += 1
       second_cut = str(second_cut)[1:ndigits+1]
       if int(str(second_cut)[0]) == 0:
           if first_number_in_second == 9:
               first = int(first) + 1


    result = str(first) + "." + str(second_cut)
    return result





print(my_round(2.1234567, 5))
print(my_round(2.0999999, 5))
print(my_round(2.9999967, 5))



# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    '''

    :param ticket_number: шестизначное число
    :return: значение: Счастливый/несчастливый
    '''
    result = 0
    s = str(ticket_number)
    list1=[]
    for i in s:
        list1.append(int(i))
    if sum(list1[:3]) == sum(list1[:-3]):
        result = "Счастливый билет"
    else:
        result = "Нечастливый билет"
    return result

print(lucky_ticket(123006))
print(lucky_ticket(123321))
print(lucky_ticket(436751))





