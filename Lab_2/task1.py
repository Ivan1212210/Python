money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0    # текущий месяц
month_rez = 0.0    # убыток за месяц
while month_rez < money_capital:
    month += 1
    month_rez += spend + spend * increase - salary
    spend += spend * increase
print("Количество месяцев, которое можно протянуть без долгов:", month)

