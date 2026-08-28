"""
File: cafe_bill.py
Course: C S 313E
Description: Solution for Week 1 Lecture 1 Activity - Cafe Bill
"""

# Instructions: You run a small cafe and need to generate a basic bill
# for 3 customers. For each customer, you are given:
# Customer name (string), Number of items bought (int), Price per item (float)

# Set one tax rate of 0.18 for all 3 bills
tax_rate = 0.18

# Use advanced assignment to set name, item count, and unit price per customer
c1_name, num_items1, price1 = input("Customer 1 Name: "), int(input("Number of \
items: ")), float(input("Price per item: "))

print()

c2_name, num_items2, price2 = input("Customer 2 Name: "), int(input("Number of \
items: ")), float(input("Price per item: "))

print()

c3_name, num_items3, price3 = input("Customer 3 Name: "), int(input("Number of \
items: ")), float(input("Price per item: "))

# Calculate each customers' total bill with tax
total_bill1 = (1 + tax_rate) * price1 * num_items1
total_bill2 = (1 + tax_rate) * price2 * num_items2
total_bill3 = (1 + tax_rate) * price3 * num_items3

# Match the required output format exactly:
'''
Customer bill summary
----------------------------------------
Name: Alice
Items: 3
Price per item: $50.00
Total (with tax): $177.00
'''

# To ensure all prices are rounded to 2 decimal places,
# we'll have to convert them to f-strings outside the print statements
price1 = f"{price1:.2f}"
price2 = f"{price2:.2f}"
price3 = f"{price3:.2f}"

total_bill1 = f"{total_bill1:.2f}"
total_bill2 = f"{total_bill2:.2f}"
total_bill3 = f"{total_bill3:.2f}"

# Print with only + and , plus \n and \t
print("\nCustomer bill summary\n----------------------------------------\n\
Name: " + c1_name + "\nItems:", num_items1, "\nPrice per item: $" + price1 + \
      "\nTotal (with tax): $" + total_bill1)

print("\nCustomer bill summary\n----------------------------------------\n\
Name: " + c2_name + "\nItems:", num_items2, "\nPrice per item: $" + price2 + \
      "\nTotal (with tax): $" + total_bill2)

print("\nCustomer bill summary\n----------------------------------------\n\
Name: " + c3_name + "\nItems:", num_items3, "\nPrice per item: $" + price3 + \
      "\nTotal (with tax): $" + total_bill3)
