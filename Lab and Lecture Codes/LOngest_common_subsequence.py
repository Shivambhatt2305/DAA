def LCS(str1,str2):
    m=len(str1)
    n=len(str2)
    L=[[0 for i in range(n+1)]for j in range( m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str1[i-1]==str2[j-1]:
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i][j-1],L[i-1][j])
    return L[m][n]
    
str1=str(input("Enter first string: "))
str2=str(input("Enter second string: "))
print("The longest common subsequence is: ",LCS(str1,str2))