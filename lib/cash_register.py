#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction_amount = 0
  def add_item(self, title, price, quantity=1):
    amount = price * quantity
    self.total += amount
    self.last_transaction_amount = amount
    for _ in range(quantity):
      self.items.append(title) 
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
        discount_amount = self.total * (self.discount / 100)     
        self.total -= discount_amount
        if self.total.is_integer():
            self.total = int(self.total)
        print(f"After the discount, the total comes to ${self.total}.")
  def void_last_transaction(self):
    self.total -= self.last_transaction_amount
    self.last_transaction_amount = 0
  pass
