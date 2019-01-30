n = input('Introduce a number: ')
n =int(n)

def fibonacci(n):
    counter = 0
    a,b=0,1
    for i in range(n-1):
        a, b = b, a + b
        counter += a
    print(counter)
fibonacci(n)