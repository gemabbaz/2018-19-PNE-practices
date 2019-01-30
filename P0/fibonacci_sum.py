n = input('Introduce a number: ')
n =int(n)
counter = 0
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        counter += a
        a,b=b,a+b

print(counter)