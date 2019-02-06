def count_bases(seq):
    """Counting the number of As in the string"""
    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0
    for b in seq:
        if b == 'A':
            result_a += 1
        elif b == 'C':
            result_c += 1
        elif b == 'T':
            result_t += 1
        elif b == 'G':
            result_g += 1

    return dict(A=result_a, C=result_c, G=result_g, T=result_t)


s1 = input("Introduce the first DNA sequence: ")
s1 = s1.upper()
s2 = input("Introduce the second DNA sequence: ")
s2 = s2.upper()
sequences=[s1, s2]
na1 = count_bases(sequences[0])
na2 = count_bases(sequences[1])


print("There are {} in the first sequence".format(na1))
print("There are {} in the second sequence".format(na2))

# Calculate the total length

t1 = len(s1)
t2 = len(s2)

if len(s1) or len(s2) != 0:
    print("The first sequence is {} bases in length".format(t1))
    print("The percentages of As in the first sequence is {}%".format(round(100.0 * count_bases(sequences[0])["A"] / t1, 1)))
    print("The percentages of Cs in the first sequence is {}%".format(round(100.0 * count_bases(sequences[0])["C"] / t1, 1)))
    print("The percentages of Gs in the first sequence is {}%".format(round(100.0 * count_bases(sequences[0])["G"] / t1, 1)))
    print("The percentages of Ts in the first sequence is {}%".format(round(100.0 * count_bases(sequences[0])["T"] / t1, 1)))
    print("The second sequence is {} bases in length".format(t2))
    print("The percentages of As in the second sequence is {}%".format(round(100.0 * count_bases(sequences[1])["A"] / t2, 1)))
    print("The percentages of Cs in the second sequence is {}%".format(round(100.0 * count_bases(sequences[1])["C"] / t2, 1)))
    print("The percentages of Gs in the second sequence is {}%".format(round(100.0 * count_bases(sequences[1])["G"] / t2, 1)))
    print("The percentages of Ts in the second sequence is {}%".format(round(100.0 * count_bases(sequences[1])["T"] / t2, 1)))

else:
    print("There are 0 As in the sequence")
    print("This sequence is 0 bases in length")
    print("The percentages of As is 0%")