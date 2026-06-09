#!/usr/bin/env python3
"""
Module: cash_register.py
Provides a stateful class tracking customer point-of-sale transactions.
"""

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes transactional states, accommodating an optional baseline discount rate.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        
        # Tracks historical structural changes for transaction voiding
        self._last_transaction_history = []

    def add_item(self, title, price, quantity=1):
        """
        Calculates item insertions, accumulates values, and lists scanned keys.
        """
        transaction_cost = price * quantity
        self.total += transaction_cost
        
        # Append titles to build the transaction sequence
        for _ in range(quantity):
            self.items.append(title)
            
        # Record the transaction metadata for precise reversal operations
        self._last_transaction_history.append({
            "title": title,
            "cost": transaction_cost,
            "quantity": quantity
        })

    def apply_discount(self):
        """
        Executes a percentage discount deduction while logging matching system output lines.
        """
        if self.discount > 0:
            savings_multiplier = 1 - (self.discount / 100)
            self.total = self.total * savings_multiplier
            print(f"After the discount, the total comes to ${self.total:g}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last transaction entry block entirely from tracking.
        """
        if not self._last_transaction_history:
            return
            
        # Pop the latest transaction log snapshot
        last_action = self._last_transaction_history.pop()
        
        # Deduct the recorded cost value from our total metric balance
        self.total -= last_action["cost"]
        
        # Slice away the exact quantity of items from the tail end of the list
        qty_to_remove = last_action["quantity"]
        if qty_to_remove > 0:
            self.items = self.items[:-qty_to_remove]