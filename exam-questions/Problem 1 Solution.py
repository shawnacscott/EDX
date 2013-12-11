def myLog(x, b):
    testExp = 1
    if x < b:
        return 0
    while b**(testExp+1) <= x:
        testExp += 1
    return testExp
