from Bases import count_bases


s = input("Introduce a DNA sequence: ")
s = s.upper()
count_bases(s)
na = count_bases(s)

print("There are {} in the sequence".format(na))

# Calculate the total length

t1 = len(s)

if len(s) != 0:
    print("This sequence is {} bases in length".format(t1))
    print("The percentages of As is {}%".format(round(100.0 * count_bases(s)["A"] / t1, 1)))
    print("The percentages of Cs is {}%".format(round(100.0 * count_bases(s)["C"] / t1, 1)))
    print("The percentages of Gs is {}%".format(round(100.0 * count_bases(s)["G"] / t1, 1)))
    print("The percentages of Ts is {}%".format(round(100.0 * count_bases(s)["T"] / t1, 1)))
else:
    print("There are 0 As in the sequence")
    print("This sequence is 0 bases in length")
    print("The percentages of As is 0%")