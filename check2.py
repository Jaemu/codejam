ageTable = []
fibNumbers = []

def initFibNumbers():
    global fibNumbers
    fibNumbers.append(0)
    fibNumbers.append(1)
    fib1 = 0
    fib2 = 1
    for i in range(2, 5000):
        fibNumbers.append(fib1 + fib2)
        temp = fib1
        fib1 = fib2
        fib2 = temp + fib1

def initAgeTable():
    global ageTable
    global fibNumbers
    ageTable.append(10000)
    ageTable.append(9999)
    currentOpacity = 9999
    for i in range(2, 5001):
        if(i in fibNumbers):
            currentOpacity = currentOpacity - i
        else:
            currentOpacity = currentOpacity + 1
        ageTable.append(currentOpacity)

def checkio(opacity):
    initFibNumbers()
    initAgeTable()
    print('fib table: ' + str(fibNumbers))
    return 0
