#balance=the outstanding balance on the credit card
#annualInterestRate=annual interest rate as a decimal
#monthlyPaymentRate=minimum monthly payment rate as a decimal

#balance=4842
#annualInterestRate=0.2
#monthlyPaymentRate=0.04
totalPaid = 0
for x in range(1, 13):
    print 'Month: ' + str(x)
    minimumMonthlyPayment = (balance * monthlyPaymentRate)
    totalPaid = (totalPaid + minimumMonthlyPayment)
    print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment, 2))
    interestPaid = ((annualInterestRate/12) * balance)
    principlePaid = minimumMonthlyPayment-interestPaid
    balance = (balance-minimumMonthlyPayment)
    balance = (1 + (annualInterestRate/12)) * balance
    print 'Remaining balance: ' + str(round(balance, 2))   
print 'Total paid: ' + str(round(totalPaid, 2))
print 'Remaining balance: ' + str(round(balance, 2))

