# this script is to get an idea on self variable


class Restaurant(object):
    bankrupt = False
    def open_branch():
        if self.bankrupt:
            print(self.bankrupt)
            print("Branch opened")
        open_branch()


x = Restaurant()
print(x.bankrupt)


y = Restaurant()
y.bankrupt = True
print(y.bankrupt)

print(x.bankrupt)
