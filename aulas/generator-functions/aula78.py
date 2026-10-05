# Yield from

def gen():
    yield 1
    yield 8
    yield 9

def gen2():
    yield from gen()
    yield 4
    yield 5
    yield 6

g = gen2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))