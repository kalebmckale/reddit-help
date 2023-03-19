def calculate_tax(income):
    tax_owed 
    if income < 18200.00:
        return tax
    if income < 45000.00:
        return (income - 18200.00) * 0.19
    if income < 120000.00:
        return (income - 45000.00) * 0.325)+5092)

    if 


# input() returns a str object; so don't need to cast it, but if an int
# is needed then we can cast that.
# However, if a tax file number is supposed to begin with a 0, then this
# would fail. So, perhaps keeping it as a str and comparing to a string
# later is what you really want.
⁠if (tax_id := input("Enter your tax file number: ")) == "0":
    print("Unknown user")
    # If a function was used to get the tax file number, then instead of
    # using sys.exit(), one could just return.
    sys.exit(0)

# The while loop will repeat until break is reached, which will only happen
# if user enters a number that can be cast as a float type, i.e. a number, 
# and a non-negative value. Otherwise, it will print an error and repeat the
# request for taxable income.
while True:
    try:
        income  = float(user_input := input("Enter your taxable income: "))
    except ValueError:
        print(f"Taxable income must be a number: '{user_input}' entered.")
    else:
        if income < 0.0:
            print(f"Taxable income cannot be negative: '{user_input}' entered.")
            continue
        break

# Since we know that income is non-negative, now we can check only the upper
# bound for each tax bracket.
brackets = {
    range(18200): 0.0,
    range(18200, 45000): 0.19,
    range(45000, 120000): 0.325,
    range(120000, 180000): 0.37,
    range(180000, ): 0.45
}

tax_owed = 0.0
for min_income, tax_rate in brackets:
    if income < min_income:
        return tax_owed
    tax_owed += min_income * tax_rate



if income < 18200.00:
⁠if  Tax>=0 and Tax<18200:
    print(TFN, "You pay Nil tax")
elif Tax>=18201 and Tax<45000:
    ⁠print("TFN", TFN, "owes $",(
elif Tax>=120001 and Tax<180000:
    print("TFN", TFN, "owes $", ((Tax-120000)*0.37)+29467)
elif Tax>=180001:
    print("TFN", TFN, "owes $", ((Tax-180000)*0.45)+51667)
