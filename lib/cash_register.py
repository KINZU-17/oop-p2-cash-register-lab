#!/usr/bin/env python3

"""
Script Name: cash_register.py
Description: Implements an object-oriented transaction tracking engine utilizing
             arithmetic modifiers, comparisons, and discrete control flow logic.
Author: Junior Software Engineer
Date: June 2026
"""

class CashRegister:
    def __init__(self, tax_rate=0.08):
        """
        Initializes the stateful tracking metrics for a new transaction ledger.
        """
        # Assign the tax multiplier baseline (e.g., 0.08 maps to an 8% flat rate)
        self.tax_rate = float(tax_rate)
        
        # State tracking attributes initiated at clean zero points
        self.subtotal = 0.00
        self.total_items = 0
        self.discount_applied = 0.00

    def add_item(self, price, quantity=1):
        """
        Applies item entry increments onto running transaction subtotals.
        Uses compound arithmetic assignment operators.
        """
        try:
            item_price = float(price)
            item_quantity = int(quantity)
            
            if item_price < 0 or item_quantity < 0:
                print("[Warning] Item records cannot process negative numbers.")
                return
                
            # Perform calculations using operators: subtotal = subtotal + (price * quantity)
            self.subtotal += (item_price * item_quantity)
            
            # Increment total number of items handled using compound addition: total = total + quantity
            self.total_items += item_quantity
            
        except ValueError:
            print("[Error] Failed to calculate transaction input types.")

    def apply_discount(self, discount_code):
        """
        Evaluates string inputs through an if-elif conditional sequence 
        to alter the active discount deduction value.
        """
        # Standardize the input string to prevent unexpected failures
        code = str(discount_code).strip().upper()
        
        if code == "SAVE10":
            # Deducts a direct flat rate value of $10.00
            self.discount_applied = 10.00
            print("🚀 Code accepted: $10.00 flat deduction applied.")
        elif code == "FRESH20":
            # Calculates a variable 20% savings against the active subtotal
            self.discount_applied = self.subtotal * 0.20
            print("🚀 Code accepted: 20% subtotal savings applied.")
        else:
            print(f"❌ Code '{discount_code}' unrecognized. No deductions applied.")
            self.discount_applied = 0.00

    def calculate_total(self):
        """
        Executes final calculations, accounts for deductions, 
        and applies the sales tax percentage.
        """
        # Ensure the discount amount doesn't drop the subtotal below zero
        adjusted_subtotal = self.subtotal - self.discount_applied
        if adjusted_subtotal < 0:
            adjusted_subtotal = 0.00
            
        # Calculate the sales tax amount using multiplication operators
        tax_amount = adjusted_subtotal * self.tax_rate
        
        # Calculate final total
        final_total = adjusted_subtotal + tax_amount
        return round(final_total, 2)

    def print_receipt(self):
        """
        Generates a clean string-formatted breakdown of the transaction metrics.
        """
        print("\n=====================================")
        print("         TRANSACTION RECEIPT         ")
        print("=====================================")
        print(f" Total Scanned Items: {self.total_items}")
        print(f" Gross Subtotal     : ${self.subtotal:.2f}")
        print(f" Coupon Deductions  : -${self.discount_applied:.2f}")
        print(f" Sales Tax Rate     : {self.tax_rate * 100:.1f}%")
        print("-------------------------------------")
        print(f" FINAL BALANCE DUE  : ${self.calculate_total():.2f}")
        print("=====================================\n")

# -------------------------------------------------------------------------
# LOCAL SCRATCHPAD VERIFICATION
# -------------------------------------------------------------------------
if __name__ == "__main__":
    # Create an instance of our class to test the logic
    register = CashRegister(tax_rate=0.08)
    
    # Simulate a user scanning standard items
    register.add_item(price=15.50, quantity=2)  # Subtotal becomes $31.00
    register.add_item(price=4.50, quantity=1)   # Subtotal becomes $35.50
    
    # Simulate applying a discount code
    register.apply_discount("FRESH20")          # Deducts 20% ($7.10)
    
    # Print the receipt to verify the calculations
    register.print_receipt()