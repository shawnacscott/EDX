def iterPower(base, exp):
    result=base
    iter=0
    while iter <= int(exp):
        if exp == 0:
            result=1
            break
        elif exp == 1:
            break
        elif iter ==0:
            iter=2
        elif exp >= 2:
            result *= base
            iter += 1
    return result
