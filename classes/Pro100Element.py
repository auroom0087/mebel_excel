class Pro100Element:

    def __init__(self, name:str, count:int):
        self.name = name
        self.count = count

    def __str__(self):
        return 'There is '+str(self.count)+' of '+self.name+' in PRO100 project'