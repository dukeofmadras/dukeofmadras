import time
#declaration states
FIVE = "SLIM BAR"
TEN = "FAR BAR"
TWENTY = "MAR BAR"
FIFTY = "TWIN BAR"
#timer for performance
start = time.process_time()
class vendingMachine():
    def __init__(self, state, money, change):
        self.money = 0
        super().__init__()
        self.state = state
        self.change = 0
    # checks exact product name
    def operation(self, state, money,change):
        # program terminates if not exact products
        if state in ["SLIM BAR" , "slim bar", "slimbar", "SLIMBAR" , "slim", "SLIM", "SLIM bar", "slim BAR"]:
            print("Slim Bar Selected")
            if money >= 5:
                print("Here's your Slim bar")
                change = money - 5
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change
        elif state in ["FAR BAR", "far bar", "farbar", "FARBAR", "far", "FAR", "FAR bar", "far BAR"]:
            print("Far Bar Selected")
            if money >= 10:
                print("Here's your far bar")
                change = money - 10
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change
        elif state in ["MAR BAR", "mar bar", "marbar", "MARBAR", "mar", "MAR", "MAR bar", "mar BAR"]:
            print("Mar Bar selected")
            if money >= 20:
                print("Here's your Slim bar")
                change = money - 20
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change
        elif state in ["TWIN BAR", "twin bar", "twinbar", "TWINBAR", "twin", "TWIN", "TWIN bar", "twin BAR"]:
            print("Twin Bar selected")
            if money == 50:
                print("Here's your Slim bar")
                change = money - 50
                print("Take your change", change)
            else:
                print("Insufficient cash")
            return change
        else: print("Invalid response")

    # more and product functions are if customer wants to buy more items with remaining change

    def more(self, change):
        while change >= 5:
            z = input("Want to buy more items ? (y/n)")  # if no, program terminates
            if z in ["y", "yes", "Y", "YES"]:
                change = vendingMachine.moreproduct(0, change)
            else:
                print("thank you for shopping")
                break
        else:
            print("Thank you for shopping")

    def moreproduct(self, change):
        a = input("Enter product name")
        checking1 = checking.operation(a, change, 0)
        return checking1


print('Welcome to the vending machine!')
print("We accept only coins of 5, 10, 20 and 50 and the exact products, Thank you")
print("Slim bar - 5p, Far bar - 10p, Mar bar- 20p and Twin bar - 50p")
coins = int(input("Please, Insert Coin"))
statex = str(input("Please, Enter product you needed"))
changex = 0
if coins in [5,10,20,50]:
    checking = vendingMachine(statex, coins, changex)
    change = int(checking.operation(statex,coins, changex))
    vendingMachine.more(0,change)
else:
    print("Enter exact coins")  # program ends if not exact poins

print(time.process_time() - start)  #prints the calculated time
