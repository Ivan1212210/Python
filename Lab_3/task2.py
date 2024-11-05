# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, c=","):
    rez_list = []
    a = a.split(c)
    b = b.split(c)
    for i in a:
        for j in b:
            if (i == j):
                rez_list.append(j)
    rez_list.sort()
    return rez_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, ";")) # TODO Провеьте работу функции с разделителем отличным от запятой