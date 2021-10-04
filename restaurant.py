class RestaurantTable : 

    menus = {
        'pizza' : 5000,
        'chicken curry' : 1500,
        'potato fried' : 1000,
        'tom yam soup' : 3000,
        'hotpot' : 8000,
        'cola' : 800
    }

    def __init__(self) -> None:
        self.total = 0
        self.orderList = []

    def addOrder(self,order):
        self.orderList.append(order)
        self.total += self.menus[order]

    def printBill(self):
        for order in self.orderList:
            print (f'{order} : {self.menus[order]} MMK')
        
        print(f'Total price : {self.total} MMK')

def startProgram():
    table = RestaurantTable()

    while True: 
        order = input('order : ')
        table.addOrder(order)

        another = input ('order again? "y/n"')
        if another == "y" :
            continue 
        elif another == "n" :
            table.printBill()
            break
        else : 
            print ('Please enter yes or no (y/n).')

startProgram()
        
