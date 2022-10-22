class PriceElement:
    
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price

    def __str__(self):
        output = 'Price of '+self.name+' is '+self.price
        return output