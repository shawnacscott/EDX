#balance=the outstanding balance on the credit card
#annualInterestRate=annual interest rate as a decimal

originalBalance=balance
minimumMonthlyPayment=10
monthlyInterestRate=(annualInterestRate/12.0)
while balance>=0:
    for month in range(12):
        balance=((balance-minimumMonthlyPayment)*(1+monthlyInterestRate))
    if balance<=0:
        print('Lowest Payment: ')+str(minimumMonthlyPayment)
    elif balance>=0:
        balance=originalBalance
        minimumMonthlyPayment+=10
