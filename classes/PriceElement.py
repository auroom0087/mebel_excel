class PriceElement:
    
    def __init__(self, name:str, amount:int, type_:str, price:int):
        self.name = name
        self.amount = amount
        self.type = type_
        self.price = price

    def __str__(self):
        output = 'Price of '+self.name+' is '+self.price
        return output