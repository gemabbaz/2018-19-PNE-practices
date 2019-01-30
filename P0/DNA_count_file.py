sequence = input('Please introduce the filename: ')
filename = open(sequence, 'r')
counta = 0
countc = 0
countg = 0
countt = 0
for line in sequence:
    line.replace(' ', '').upper()
    counta += line.count('A')
    countg += line.count('G')
    countt += line.count('T')
    countc += line.count('C')

print('The number of times A shows up is: ', counta)
print('The number of times G shows up is: ', countg)
print('The number of times T shows up is: ', countt)
print('The number of times C shows up is: ', countc)
