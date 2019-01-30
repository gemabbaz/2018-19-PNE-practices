n = input('Introduce a number: ')
n =int(n)
def fibonacci(n):
    a,b=1,1
    for i in range(n-2):
        a,b=b,a+b
    return a
print(fibonacci(n))