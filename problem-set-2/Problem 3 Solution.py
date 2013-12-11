originalBalance=balance
monthlyInterestRate=annualInterestRate/12.0
lowerBound=balance/12.0
upperBound=(balance*(1+monthlyInterestRate)**12)/12.0
while abs(balance)>0.01:
 for month in range(12):
  averagePay=(lowerBound+upperBound)/2.0
  balance=((balance-averagePay)*(1+monthlyInterestRate))
 if balance>0.01:
  lowerBound=averagePay
  balance=originalBalance
 elif balance <-0.01:
  upperBound=averagePay
  balance=originalBalance
 elif (-0.01<=balance and balance<=0.01):
  break
print('Lowest Payment: '+str(round(averagePay,2)))
