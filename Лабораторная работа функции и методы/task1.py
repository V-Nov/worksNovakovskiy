# TODO Напишите функцию для поиска индекса товара
def item_search(items_lt, item_):
    if item_ in items_lt:
        return items_lt.index(item_)



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']



for find_item in ['банан', 'груша', 'персик']:
    index_item = item_search(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
