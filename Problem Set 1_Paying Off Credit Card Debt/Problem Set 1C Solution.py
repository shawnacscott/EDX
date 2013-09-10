balance = float(raw_input('Enter the outstanding balance on your credit card: '))
interest = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

minpay = balance/12
print minpay
maxpay = (balance*(1+(interest/12.0))*12.0)/12.0
print maxpay
while balance>0
    

    
##while x > 0:
##    x = x * (1 + (y/12.0)) - mmp
##    mmp = mmp + 10
##    
##print 'RESULT'
##print 'Monthly payment to pay off debt in one year: ' + str(mmp)
##print 'Balance: ' + str(x)
