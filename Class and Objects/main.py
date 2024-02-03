import csv 

class Item:

    all =[]
    pay_rate = 0.8
    
    #Constructor
    def __init__(self,name:str,price:float,quantity=0):
        # Run validations to the received agrument
        assert price >=0 ,f"Price {price} is not greater than or equal to zero"
        assert quantity >=0 ,f"Quantity {quantity} is not greater than or equal to zero"

        #Assign to Self Objects
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
    # apply discount 
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_price(self):
        return self.price * self.quantity
    
    def __repr__(self) -> str:
        return f"Item('{self.name}' , {self.price} , {self.quantity})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('myfile.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )




item1 = Item('Phone',100,2)

item2 = Item('Cable',50,10)

# item1.apply_discount()
# print(item1.price)
# print(item1.calculate_price())

# item2.pay_rate = 0.7
# print(item2.price)

# item2.apply_discount()
# print(item2.price)

# print(Item.__dict__)
# print(item1.__dict__)





'''
item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 3

print(item1)

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 5

print(item2)
'''