
tax_rate = 7.25
usr_cost = float(input("Enter the total value of all item: "))

tax = usr_cost * 7.25 / 100
total = usr_cost + tax


print("------------------------------")
print("Value of items before tax:", usr_cost)
print("Tax: $ {0:.2f}".format(tax))
print("Total after tax: $ {0:.2f}".format(total))

