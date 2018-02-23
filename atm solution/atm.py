moneyCategory = [100,50,10,5,2,1]

def atm(requested):
    money = 500
    remaining = 0
    if requested > 0 and requested < (money + 1):
        print 'Your balace is: ' + str(money)
        print 'You requested :' + str(requested)
        for i in moneyCategory:
            while (requested - i) >= 0:
                print 'given ' + str(i)
                requested -= i
                remaining += i
        print 'Your remaining balance is: ' + str(money - remaining)
    else:
        print "You don't have enough balance"


atm(227)
