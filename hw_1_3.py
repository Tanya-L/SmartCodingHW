# -*- coding: utf-8 -*-
# Question 3
# An ICA supermarket attendant works every day selling to customers.
# They have a business where each item you buy, mjolk, Pannkakor, Bröd, Paj,
# and everything there costs a positive number of Kroner (integers).
# If bröd costs 22 kroner. There is no item in ICA that costs a decimal
# value like 10.13 kr (VAT tax is included in the amount already).
# Kroner change can be provide in 1 kr, 2kr, 5kr and 10kr.
# Write a function in Python that takes in two arguments will return
# the correct change to the customer with the smallest possible number
# of coins (or bills if paper money is used).
#            def getChange(costOfItem, amountPaid):
#                # replace with your code


def changeAmount(amount, coinvalues):
    change = {}
    while amount > 0:
        n = amount // coinvalues[0]
        if n > 0:
            change["%dkr" % coinvalues[0]] = n
            amount -= n * coinvalues[0]
        del coinvalues[0]
    return change


# change efter buying
def getChange(costOfItem, amountPaid):
    return changeAmount(amountPaid - costOfItem, [10, 5, 2, 1])


print(getChange(73, 100))
print(getChange(44, 100))
print(getChange(15, 100))
print(getChange(31, 90))
