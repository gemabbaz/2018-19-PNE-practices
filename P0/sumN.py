num=input('Introduce a number: ')
num=int(num)
def sum(num):
    number = 0
    for i in range(num):
        number = i+1+number


    return number

print('The sum is: ', sum(num))