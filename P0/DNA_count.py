sequence = input('Introduce a DNA sequence: ')
sequence = sequence.upper()
lenght = len(sequence)
print('The lenght of the DNA sequence is: ', lenght)
print('The number of times A shows up is: ', sequence.count('A'))
print('The number of times G shows up is: ', sequence.count('G'))
print('The number of times T shows up is: ', sequence.count('T'))
print('The number of times C shows up is: ', sequence.count('C'))