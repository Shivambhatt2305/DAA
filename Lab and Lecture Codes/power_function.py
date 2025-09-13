# # t(n)=o(n)
# def power(x,n):
#     if n==0:
#         return 1
#     elif n%2==0:
#         return power(x,n//2) * power(x,n//2)
#     else:
#         return x * power(x,n//2) * power(x,n//2)
    
# print(power(2,3))


#t(n)=o(log n)
# Using recursion with optimized approach
# def power(x,n):
#     temp=power(x,n//2)
#     if n==0:
#         return 1
#     elif n%2==0:
#         return temp * temp
#     else:
#         return x * temp * temp
    
# print(power(2,3))

#native approch
def power_iterative(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

print(power_iterative(2, 3)) 
