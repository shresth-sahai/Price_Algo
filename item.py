class Item:
    def __init__(self,item_name, item_price, item_offer, item_count) -> None:
        self.name = item_name
        self.price = item_price
        self.offer = item_offer
        self.count = item_count

    def calculate_total_price(self):
        if self.offer == None:
            return self.count * self.price
        else:
            item_group_size = self.offer[0]
            item_group_price = self.offer[1]

            total_cost = 0

            total_groups = self.count // item_group_size
            group_cost = total_groups * item_group_price

            individual_items = self.count % item_group_size
            individual_cost = individual_items * self.price

            total_cost = individual_cost + group_cost

            return total_cost