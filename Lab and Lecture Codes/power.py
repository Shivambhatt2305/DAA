# def power(base, exponent):
#     a=base
#     for i in range(exponent-1):
#         base=base*a
#     return base

# print(power(2, 3))  

#2nd approch using recursion
def power(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base,exponent-1)

print(power(2, 3))
