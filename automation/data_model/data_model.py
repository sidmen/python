# some behaviour that I want to implement -> write some __function__
# top-level function or top-level syntax -> corresponding __function__
# x + y --> __add__
# init x --> __init__
# repr(x) --> __repr__


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)


p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)

print(p1)
print(p2)
print(p1 + p2)
print(len(p1))
