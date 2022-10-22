class ReportElement:

    def __init__(self,name:str,count:int,price:int):
        self.name = name
        self.count = count
        self.price = price
        self.sum = price*count

    def __str__(self):
        if self.count == 1:
            return self.name+' costs '+str(self.sum)
        return str(self.count)+' of '+self.name+' cost '+str(self.sum)