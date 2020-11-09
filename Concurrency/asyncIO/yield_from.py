def test_yield_inner():
    inner_result = yield 2
    print("inner result", inner_result)
    return 3

def test_yield_outer():
    yield 1
    val = yield from test_yield_inner()
    print("val of test_yield_outer", val)
    yield 4

gen = test_yield_outer()
print(next(gen))
print(next(gen))
print(gen.send("abc"))
