#!/usr/bin/env python3

amount = float(input("输入数额:"))
inrate = float(input("输入利率:"))
period = int(input("输入年限:"))

value = 0
year = 1
while year <= period:
    value = amount + (amount * inrate)
    print("Year {} Rs. {:.2f}".format(year,value))
    amount = value
    year += 1
