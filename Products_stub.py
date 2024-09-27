class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def make_purchase(self, quantity):
        if quantity > self.amount:
            raise ValueError(f"Only {self.amount} in stock.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        
        total_price = self.get_price(quantity)
        self.amount -= quantity
        print(f"You bought {quantity} {self.name}(s) for a total of ${total_price:.2f}.")
        print(f"Remaining Items: {self.amount}")