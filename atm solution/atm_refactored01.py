moneyCategory = [100,50,10,5,2,1]
balance = 500

def withdraw(balance , requested):
    #global balance
    remaining = 0
    if requested > 0 and requested <= balance:
        print 'Your balace is: ' + str(balance)
        print 'You requested :' + str(requested)
        for i in moneyCategory:
            while (requested - i) >= 0:
                print 'given ' + str(i)
                requested -= i
                remaining += i
        balance -= remaining
        print 'Your remaining balance is: ' + str(balance)
        return balance
    else:
        print "You don't have enough balance"

#balance = 500
balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
#print balance
#balance = withdraw(balance , 30)
