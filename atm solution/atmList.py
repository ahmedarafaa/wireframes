class AtmClass(object):


    """docstring for atmClass."""
    def __init__(self, balance, bankName):
        print '*** ' + str(bankName) + ' ***'
        self.balance   = balance
        self.bankName  = bankName
        self.withdrawalsList = []

    def withdraw(self,requested,moneyCategory = [100,50,10,5,2,1]):
        remaining = 0
        if requested > 0 and requested <= self.balance:
            print 'Your balace is: ' + str(self.balance)
            print 'You requested :'  + str(requested)
            print '#########################'
            self.withdrawalsList.append(requested)
            for i in moneyCategory:
                while (requested - i) >= 0:
                    print 'given ' + str(i)
                    requested -= i
                    remaining += i

            self.balance -= remaining
            print 'Your remaining balance is: ' + str(self.balance)
        else:
            print "Please enter valid amount!!"

        return self.balance


    def show_withdrawals(self):
        print '-' * 8 + 'withdrawal' + '-' * 8
        for withdrawal in self.withdrawalsList:
            print 'Your Transaction is: ' + str(withdrawal)


smartBankBalance = 500
barakaBankBalance= 1000

smartBank = AtmClass(smartBankBalance,'Smart Bank')
smartBank.withdraw(277)
smartBank.withdraw(30)
smartBank.show_withdrawals()

barakaBank = AtmClass(barakaBankBalance,'Baraka Bank')
barakaBank.withdraw(500)
barakaBank.withdraw(300)
barakaBank.withdraw(300)
barakaBank.show_withdrawals()
