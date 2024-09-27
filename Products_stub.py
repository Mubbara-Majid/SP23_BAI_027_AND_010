class Product:
    
   
    def __init__(self, Pname, Pprice, Regprice):
        self.Pname = Pname  # Product name
        self.Pprice = Pprice  # Price per item
        self.Regprice = Regprice  # Regular price per item

   
    def getPrice(self, Pname, Pprice, Regprice, quantity, amount):
       
        if quantity > amount:
            print(f"Error: Not enough stock for {Pname}. Available stock: {amount}")
            return

       
        totalCost = quantity * Pprice ##wuithout discount

        
        regPrice = quantity * Regprice ##regularprice

       
        if quantity < 10:
            discount = 0
        elif 10 <= quantity <= 99:
            discount = 10 / 100  
        else:  
            discount = 20 / 100  

       
        discounted_total = totalCost * (1 - discount)

        
        remaining_stock = amount - quantity ##stockAfterpurchase

        
        print("Quantity Purchased: " + str(quantity))
        print("Total Cost (with Discount): $" + str(round(discounted_total, 2)))
        print("Total Regular Price (without discount): $" + str(round(regPrice, 2)))
        print("Discount applied: " + str(discount * 100) + "%")
        print("Remaining Stock: " + str(remaining_stock) + "\n")

        return discounted_total



laptop1 = Product(Pname="Dell", Pprice=1200.99, Regprice=1500.00)
laptop2 = Product(Pname="Apple", Pprice=2399.50, Regprice=2599.00)
laptop3 = Product(Pname="HP", Pprice=1549.00, Regprice=1699.00)


laptop1.getPrice(Pname="Dell", Pprice=1200.99, Regprice=1500.00, quantity=5, amount=20)
laptop2.getPrice(Pname="Apple", Pprice=2399.50, Regprice=2599.00, quantity=8, amount=15)
laptop3.getPrice(Pname="HP", Pprice=1549.00, Regprice=1699.00, quantity=2, amount=10)

      