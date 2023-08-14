x = 'global x'
def test():
    y = 'local y'
    print(y)
    print(x)
test()
print(x)


def test():
    x = 'local x'
    print(x)
test()
print(x)

def test():
    global x
    x = 'local x'
    print(x)
test()
print(x)


def test(z):
    x = 'local x'
    print(z)
test('local z')


m = min([5, 1, 4, 2, 3])
print(m)


def outer():
    x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()



def outer():
    x = 'outer x'
    
    def inner():
        #x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()


x = 'global x'

def outer():
    x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()
print(x)



x = 'global x'

def outer():
    #x = 'outer x'
    
    def inner():
        #x = 'inner x'
        print(x)
    
    inner()
    print(x)
outer()
print(x)