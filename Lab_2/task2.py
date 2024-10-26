salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0.0
month_rez = 0.0    # убыток за месяц
for month in range(1, months + 1):
    if (month > 1):
        month_rez += spend + spend * increase - salary
        spend += spend * increase
    else:
        month_rez += spend - salary
money_capital = round(month_rez)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
