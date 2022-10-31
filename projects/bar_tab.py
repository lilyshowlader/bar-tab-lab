class Tab:

  menu = {
    'wine': 5,
    'beer': 3,
    'soft_drink': 2,
    'chicken': 10,
    'beef': 15,
    'veggie': 12,
    'dessert': 6
  }

#self.total is the bill. self.item is the list of items in the bill
#in this initialization function, the bill starts off as 0 and there are no items because nothing has been ordered yet.

  def __init__(self):
    self.total = 0
    self.items =[]

#creating an instance method to add everytime a user adds something to their items and increases their total
def add(self, item): 
  self.items.append(item)
  self.total += self.menu[item]

#working out the bill
def print_bill(self, tax, service):
  tax = (tax/100) * self.total
  service = (service/100) * self.total
  total = self.total + tax + service
  
  for item in self.items:
    print(f'{item:20} ${self.menu[item]}')
  print(f'{"Total":20} ${total:.2f}')