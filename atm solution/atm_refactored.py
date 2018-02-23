moneyCategory = [100,50,10,5,2,1]
balance = 500

def withdraw(requested):
    global balance
    remaining = 0
    if requested > 0 and requested < (balance + 1):
        print 'Your balace is: ' + str(balance)
        print 'You requested :' + str(requested)
        for i in moneyCategory:
            while (requested - i) >= 0:
                print 'given ' + str(i)
                requested -= i
                remaining += i
        balance -= remaining
        #print 'Your remaining balance is: ' + str(balance - remaining)

        print 'Your remaining balance is: ' + str(balance)
    else:
        print "You don't have enough balance"

withdraw(277)
withdraw(30)
withdraw(5)
withdraw(500)
