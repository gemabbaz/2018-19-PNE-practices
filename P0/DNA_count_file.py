sequence = input('Please introduce the filename: ')

def countdna(sequence):
    with open(sequence, 'r') as f:
        filename= f.read()
        length = len(filename)-1
    print('The number of times A shows up is: ', filename.count('A'))
    print('The number of times G shows up is: ', filename.count('G'))
    print('The number of times T shows up is: ', filename.count('T'))
    print('The number of times C shows up is: ', filename.count('C'))
    print('The total lenght of the DNA sequence is: ', length)

countdna(sequence)