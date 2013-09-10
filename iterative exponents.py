def iterPower(base, exp):
    result=base
    iter=0
    while iter <= int(exp):
##        print('I made it to the for loop')
        if exp == 0:
            result=1
##            print('I made it to the exp == 0 if statement')
            break
        elif exp == 1:
##            print('I made it to the exp == 1 if statement')
            break
        elif iter ==0:
            iter=2
        elif exp >= 2:
            result *= base
            iter += 1
##            print('I made it to the actual calculation part')
    return result
