"""
Задание 4. Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется
процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры:
сумма вклада и срок вклада. Каждый из трех банковских продуктов должен
быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и
значения процентной ставки для каждого срока. В функции необходимо
проверять принадлежность суммы вклада к одному из диапазонов и
выполнять расчет по нужной процентной ставке. Функция возвращает
сумму вклада на конец срока.

Примечание: используем функциональный подход (не ООП)
Вы можете сделать расчет без капитализации и с капитализацией

Пример без капитализации: 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11300

Пример с капитализацией (ежемесячной): 10 тыс на 24 мес
deposit(10000, 24)
к концу срока: 11384.29
"""


print('Добро пожаловать в интернет-банк!')
print('У нас фантастические процентные ставки!')
print('На какую сумму желаете сделать вклад?')
money = float(input())
print('На какой срок желаете сделать вклад?')
times = float(input())
# Депозит до 10 000 руб
if (money<9999 and times < 6):
    moneys = (money * 0.05 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')
elif (money<9999 and times < 12):
    moneys = (money * 0.06 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')
elif (money<9999 and times < 24):
    moneys = (money * 0.05 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')

# Депозит до 100 000 руб
elif (money<99999 and times < 6):
    moneys = (money * 0.006 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')
elif (money<99999 and times < 12):
    moneys = (money * 0.007 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')
elif (money<99999 and times < 24):
    moneys = (money * 0.0065 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')


# Депозит до 1 000 000 руб
elif (money<1000000 and times < 6):
    moneys = (money * 0.007 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')
elif (money<1000000 and times < 12):
    moneys = (money * 0.008 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')
elif (money<1000000 and times < 24):
    moneys = (money * 0.0075 * times) + money
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', moneys, '₽.')