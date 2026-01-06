def doanhnd():
    print("doanhnd10")
    yield 10
    print("doanhnd20")
    yield 20
    
d = doanhnd()
print(next(d))
print(next(d))