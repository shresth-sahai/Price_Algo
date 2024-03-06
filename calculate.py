from item import Item
from collections import Counter
import collections

def calculate_total_order_price(item_info_array, items):
    item_info_map=collections.defaultdict(tuple)
    for item in item_info_array:
        item_info_map[item[0]] = ((item[1],item[2]))

    total_order_price = 0
    item_count = Counter(items)
    for item in item_count.keys():
        item_obj = Item(item,item_info_map[item][0], item_info_map[item][1], item_count[item])
        total_item_cost = item_obj.calculate_total_price()
        total_order_price += total_item_cost

    return total_order_price

#print(calculate_total_order_price([('A',50,(3,130)),('B',30,(2,45)),('C',20, None),('D',15,None)],"AAABBD"))