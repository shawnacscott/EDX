ob = float(raw_input('Enter the outstanding balance on the credit card: '))
ir = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
mp = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))
for x in range(1, 13):
    print 'Month: ' + str(x)
    mmp = ob * mp
    if x == 1:
        tp = mmp
    elif x > 1:
        tp = round(tp + mmp, 2)
    print 'Minimum monthly payment: ' + str(round(mmp, 2))
    ip = (ir/12) * ob
    pp = mmp-ip
    print 'Principle paid: ' + str(round(pp, 2))
    ob = ob-pp
    print 'Remaining balance: ' + str(round(ob, 2))   
print 'Total paid: ' + str(round(tp, 2))
print 'Remaining balance: ' + str(round(ob, 2))

