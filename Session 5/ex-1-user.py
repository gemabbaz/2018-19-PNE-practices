def count_a(seq):
    """Counting the number of As in the string"""
    result = 0
    for b in seq:
        if b == 'A':
            result += 1

    return result

# Main program

s = input("Introduce a DNA sequence: ")
s = s.upper()
na = count_a(s)
print("There are {} As in the sequence".format(na))

# Calculate the total length

t1 = len(s)

if len(s) != 0:
    print("This sequence is {} bases in length".format(t1))
    print("The percentages of As is {}%".format(round(100.0 * na/t1, 1)))
else:
    print("There are 0 As in the sequence")
    print("This sequence is 0 bases in length")
    print("The percentages of As is 0%")