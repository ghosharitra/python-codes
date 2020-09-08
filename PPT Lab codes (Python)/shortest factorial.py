def factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

def combination(r,n):
    return factorial(n)/(factorial(n-r)*factorial(r))



print(combination(4,6))