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


def buildingsaving():
    amount = float(input("amount for saving:"))
    income = float(input("Monthly payment:"))
    interest = float(input("interest as a decimal number(0.0x):"))
    final_amount = 0
    years = 0

    for i in range(0, 100):
        final_amount = (income*12)*(1+interest)

        if(final_amount >= amount/2):
            years = i
            break

    print("Sie haben die Hälfte ihrer Bausparsumme angespart")
    print("Sie haben drei Optionen:")
    nextstep = int(input("1: Bis zum Ende der Bausparsumme weitersparen\n2: Die Hälfte der Summe entgegennehmen\n3: Die Hälfte der Summe entgegennehmen und die zweite Hälfte als Darlehen aufnehmen\n"))

    if nextstep == 1:
        print(f"Sie erhalten nach {years*2} Jahren {amount} Euro")

    elif nextstep == 2:
        print(f"Sie erhalten {years} Jahren {final_amount} Euro")

    elif nextstep == 3:
        leftover = final_amount/2
        interest = float(input("Zinsen des Darlehens als Dezimalzahl:"))
        for i in range(0, 100):
            leftover = leftover - income*12
            leftover = leftover * (1+interest)

            if(leftover <= 0):
                years = i
                break
            if(years == 0):
                print("Scale Error")
            else:
                print("Nach {} Jahren ist das Darlehen abgezahlt".format(years))



