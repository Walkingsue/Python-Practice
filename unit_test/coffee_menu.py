
class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }

  def get_price(self, item):
    return self.menu[item]
  
  def add_item(self, item1, item2):
    self.menu[item1] = item2