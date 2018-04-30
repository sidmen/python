from library import Base

assert hasattr(Base, 'foo'), "you broke it, you fool!"
# code fails when foo() method does not exist


class Derived(Base):
    def bar(self):
        return self.foo()


bar()
