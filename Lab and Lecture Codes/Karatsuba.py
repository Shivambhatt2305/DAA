def karatsuba(x,y):
    if x<10 or y<10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    if n%2!=0:
        n -= 1
    
    a,b=divmod(x,10**(n//2))
    c,d=divmod(y,10**(n//2))
    
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a+b, c+d)-ac-bd
    return (ac*(10**n))+(abcd)*(10**(n//2))+bd    


x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print(karatsuba(x,y))