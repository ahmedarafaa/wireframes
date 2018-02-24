class atmClass(object):

    moneyCategory = [100,50,10,5,2,1]
    """docstring for atmClass."""
    def __init__(self, balance, bankName):
        print '*** ' + str(bankName) + ' ***'
        self.balance   = balance
        self.bankName  = bankName

    def withdraw(self,requested):
        remaining = 0
        if requested > 0 and requested <= self.balance:
            print 'Your balace is: ' + str(self.balance)
            print 'You requested :' + str(requested)
            print '#########################'
            for i in atmClass.moneyCategory:
                while (requested - i) >= 0:
                    print 'given ' + str(i)
                    requested -= i
                    remaining += i
            self.balance -= remaining
            print 'Your remaining balance is: ' + str(self.balance)
        else:
            print "Please enter valid amount!!"

        return self.balance

smartBankBalance = 500
barakaBankBalance= 1000

smartBank = atmClass(smartBankBalance,'Smart Bank')
smartBank.withdraw(277)
smartBank.withdraw(800)

barakaBank = atmClass(barakaBankBalance,'Baraka Bank')
barakaBank.withdraw(500)
barakaBank.withdraw(300)
barakaBank.withdraw(300)
