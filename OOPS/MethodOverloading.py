# method over-loading in python using default argument

class A:
    def first(self, f=None):
        if f is not None:
            print('Method', f)
        else:
            print('Method without argument')


a = A()
a.first()
print
a.first('with argument')
