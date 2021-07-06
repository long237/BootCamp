income= float(input("Enter your income here:$"))
TAX_LIM_10= 9875
TAX_LIM_12= 40125
TAX_LIM_22= 85525
TAX_LIM_24= 163300
TAX_LIM_32= 207350
TAX_LIM_35= 518400
TAX_LIM_37= 518400

TAX_12= 987.50
TAX_22= 4617.50
TAX_24= 14605.50
TAX_32= 33271.50
TAX_35= 47367.50
TAX_37= 156235

if income>=0 and income<= TAX_LIM_10: #10 percent tax
    tax= income*10/100
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_10+1) and income <= TAX_LIM_12: #12 percent tax
    income_12= income - TAX_LIM_10
    tax= income_12 * 12/100 + TAX_12
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_12+1) and income<= TAX_LIM_22:#22 percent tax
    income_22= income - TAX_LIM_12
    tax= income_22 * 22/100 + TAX_22
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_22+ 1) and income <= TAX_LIM_24: #24% tax
    income_24= income - TAX_LIM_22
    tax= income_24 * 24/100 + TAX_24
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_24 + 1) and income <= TAX_LIM_32: #32% tax
    income_32= income - TAX_LIM_24
    tax= income_32 * 32/100 + TAX_32
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_32 + 1) and income <= TAX_LIM_35: #35% tax
    income_35= income - TAX_LIM_32
    tax= income_35 * 35/100 + TAX_35
    print("tax liability: $ {0:.2f}".format(tax))
elif income >=(TAX_LIM_35 + 1) and income<= 9.5e6: #37% tax
    income_37= income - TAX_LIM_35
    tax= income_37 * 37/100 + TAX_37
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= 10000000: # more than 10 million tax
    income_10e6= income - 10e6
    tax= TAX_37 + (9.5e6 * 37/100) + (income_10e6 *70/100)
    print("tax liability: $ {0:.2f}".format(tax))
tax_rate= (tax / income)*100
print("this is your tax rate: {0:.1f}".format(tax_rate))

#Research
#1) The average salary is: 88,849
#2) 0.89%
#3) 1 person in the class might be able to but it is hard to say.
    
    
    
    
