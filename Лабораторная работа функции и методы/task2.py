# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    participants_ = list(set(first_group.split("|")).intersection(second_group.split("|")))
    participants_.sort()
    return list(participants_)


# def find_common_participants(str1, str2, separator=','):
#     participants_first_group = str1.split("|").replace(" ", "")
#     participants_second_group = str2.split("|").replace(" ", "")
#
#     common_participants = list(set(participants_first_group) & set(participants_second_group))
#     common_participants.sort()
#
#     return common_participants
#
# str1 = "Иванов|Петров|Сидоров"
# str2 = "Петров|Сидоров|Смирнов"
#
# print(find_common_participants(str1, str2))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"



print(find_common_participants(participants_first_group, participants_second_group))
# TODO Провеьте работу функции с разделителем отличным от запятой









# def find_common_items(last_week_purchases, current_week_purchases):
#     items_ = list(set(last_week_purchases).intersection(current_week_purchases))
#     items_.sort()
#     return items_