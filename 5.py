def normalize(name):
    s = name[0].upper()
    for x in name[1:]:
        s += x.lower()
    return s

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
#########################
def isodd():
    n = 1
    while 1:
        n += 2
        yield n

def iss(n):
    return lambda x: x % n > 0 

def prime():
    yield 2
    it = isodd()
    while 1:
        n = next(it)
        yield n
        it = filter(lambda x: x % n > 0,it)
        #it = filter(iss(n),it)

for n in prime():
    if n < 1000:
        print(n)
    else:
        break


#########################
def nat():
    n = 1
    while 1:
        n += 1
        yield n
        
def iis(x):
    a = str(x)
    flag = 1
    l = 0;r = len(a)-1
    while l < r:
        if a[l] != a[r]:
            flag = 0
            break
        l+=1;r-=1
    return flag
    

def pa():
    yield 1
    it = nat()
    while 1:
        n = next(it)
        yield n
        it = filter(iis,it)

for n in pa():
    if n < 1000:
        print(n)
    else:
        break
##########################
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return -t[1]
L2 = sorted(L, key=by_score)
print(L2)

L = list(filter(lambda x:x%2==1, range(1, 20)))
print(L)
