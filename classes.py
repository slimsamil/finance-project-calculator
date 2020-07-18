def passbook():
    years = int(input("Operational time in years:"))
    amount = float(input("Current amount:"))
    monthly_invest = float(input("Monthly deposit:"))
    interest = float(input("Interest as a decimal number(0.0x):"))
    final_amount = 0
    monthly_invest = monthly_invest*12

    for _ in range(0, years):
        if final_amount == 0.0:
            final_amount = amount

        final_amount = (final_amount+monthly_invest)*(1+interest)

    print("\nFinal amount after {} years:".format(years) + str(final_amount))



def loan():
    years = int(input("Operational time in years:"))
    amount = float(input("Loan amount:"))
    interest = float(input("Interest as a decimal number(0.0x):"))
    final_amount = 0

    for _ in range(0, years):
        if final_amount == 0.0:
            final_amount = amount

        final_amount = final_amount * (1+interest)

    rates = final_amount / years/12
   
    print("\nComplete repayment is {} $".format(final_amount))
    print("Monthly payment is {} $".format(rates))



def roi():
    amount = float(input("Loan amount:"))
    income = float(input("Monthly income:"))
    interest = float(input("Interest as a decimal number(0.0x):"))
    final_amount = 0
    final_amount = amount
    income = income*12
    years = 0

    for i in range(0, 100):

        final_amount = final_amount * (1+interest)
        final_amount = final_amount - income
        if(final_amount <= 0):
            years = i
            break
   
    if(years == 0):
        print("\nThe investment is not worth it")
    else:
        print("\nThe investment is repaid after {} years".format(years))




