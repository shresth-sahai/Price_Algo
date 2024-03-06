import unittest
from calculate import calculate_total_order_price
from item import Item

class TestCalculateTotalOrderPrice(unittest.TestCase):
    def test_1(self):
        # Define test data
        item_info_array = [('A',50,(3,130)),('B',30,(2,45)),('C',20, None),('D',15,None)]
        items = "AAABBD"
        
        # Call the function
        total_order_price = calculate_total_order_price(item_info_array, items)
        
        # Assert the result
        self.assertEqual(total_order_price, 190) 
        
    def test_2(self):
        # Define test data
        item_info_array = [('A',50,(3,130)),('B',30,(2,45)),('C',20, None),('D',15,None)]
        items = "AAA"
        
        # Call the function
        total_order_price = calculate_total_order_price(item_info_array, items)
        
        # Assert the result
        self.assertEqual(total_order_price, 130)
    
    def test_3(self):
        # Define test data
        item_info_array = [('A',50,(3,130)),('B',30,(2,45)),('C',20, None),('D',15,None)]
        items = "AB"
        
        # Call the function
        total_order_price = calculate_total_order_price(item_info_array, items)
        
        # Assert the result
        self.assertEqual(total_order_price, 80)
    
    def test_4(self):
        # Define test data
        item_info_array = [('A',50,(3,130)),('B',30,(2,45)),('C',20, None),('D',15,None)]
        items = ""
        
        # Call the function
        total_order_price = calculate_total_order_price(item_info_array, items)
        
        # Assert the result
        self.assertEqual(total_order_price, 0)
    
    def test_5(self):
        # Define test data
        item_info_array = [('A',50,(3,130)),('B',30,(2,45)),('C',20, None),('D',15,None)]
        items = "A"
        
        # Call the function
        total_order_price = calculate_total_order_price(item_info_array, items)
        
        # Assert the result
        self.assertEqual(total_order_price, 50)
    
    # Add more test cases here as needed

if __name__ == '__main__':
    unittest.main()