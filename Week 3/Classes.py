class Cars:
    def __init__(self):
        self.make = "Honda"
        self.model = "CR-V"
        self.year = 2013

    def getVal(self):
        return self.make, self.model, self.year

    def setVal(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


call = Cars()

# print(call.make)
# print(call.model)
# print(call.year)
