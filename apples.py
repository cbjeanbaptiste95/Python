
import math
class apple:
    color = ""
    size = 0
    basket_weight = 0
    def __init__(self,c,s):
        self.color = c
        self.size = s
        print "the apple is " ,self.color, " and is ", self.size, "ounces"

    def print_price(self):
        price = float(self.size * 0.50)
        return price
    
    def basket(self, n):
        self.basket_weight = float(self.size * n)
        print "there are ", n, "apples in the basket, with a total weight of ", format(self.basket_weight,'.2f'), "ounces"
        return self.basket_weight
def main():
    
    apple1 = apple("blue", 12)
    cost = (apple1.print_price())
    print "the price of this apple is $", format(cost, '.2f')
    applebasket = float(apple1.basket(5))

    basket_cost = applebasket * cost
    basket_cost = format(basket_cost, '.2f')
    print "$" + basket_cost
    
if __name__ == "__main__":
    main()
