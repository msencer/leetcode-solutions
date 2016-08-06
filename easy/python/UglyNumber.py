def uglyNumber(n):
    if n<=0:
        return False
    while not n%2:
        n//=2
    while not n%3:
        n//=3
    while not n%5:
        n//=5
    return n==1


assert True == uglyNumber(1)
assert False == uglyNumber(-2125563)
assert True == uglyNumber(1024)
assert False == uglyNumber(19)
