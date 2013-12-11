#x = float(raw_input('Enter the outstanding balance on your credit card: '))
#y = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
#z = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))
for a in range(1, 13):
 print 'Month: ' + str(a)
 mmp = round((x * z), 2)
 print 'Minimum monthly payment: ' + str(mmp)
 pp = round((mmp - (x * (y/12.0))), 2)
 print 'Principle paid: ' + str(pp)
 rb = round((x - pp), 2)
 print 'Remaining balance: ' + str(rb)
 x = rb
 if a == 1:
  tp = mmp
 elif a > 1:
  tp = tp + mmp
print 'RESULT'
print 'Total amount paid: ' + str(tp)
print 'Remaining balance: ' + str(x - tp)
