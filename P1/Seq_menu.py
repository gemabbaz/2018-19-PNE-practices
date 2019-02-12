from Seq import Seq



s_1 = Seq("AAAGCTCTCGATCTGA")
s_2 = Seq("AGCGCTAGCTAA")
s_3 = s_1.complement()
s_4 = s_2.reverse()


print("The length of the first sequence", s_1.strbases, "is: ", s_1.len())
print("The number of times base A shows up is: ", s_1.count("A"))
print("The number of times base G shows up is: ", s_1.count("G"))
print("The number of times base C shows up is: ", s_1.count("C"))
print("The number of times base T shows up is: ", s_1.count("T"))
print("The percentage of A is: ", s_1.perc("A"))
print("The percentage of G is: ", s_1.perc("G"))
print("The percentage of C is: ", s_1.perc("C"))
print("The percentage of T is: ", s_1.perc("T"))

print("The length of the second sequence", s_2.strbases, "is: ", s_2.len())
print("The number of times base A shows up is: ", s_2.count("A"))
print("The number of times base G shows up is: ", s_2.count("G"))
print("The number of times base C shows up is: ", s_2.count("C"))
print("The number of times base T shows up is: ", s_2.count("T"))
print("The percentage of A is: ", s_2.perc("A"))
print("The percentage of G is: ", s_2.perc("G"))
print("The percentage of C is: ", s_2.perc("C"))
print("The percentage of T is: ", s_2.perc("T"))

print("The length of the third sequence", s_3.strbases, "is: ", s_3.len())
print("The number of times base A shows up is: ", s_3.count("A"))
print("The number of times base G shows up is: ", s_3.count("G"))
print("The number of times base C shows up is: ", s_3.count("C"))
print("The number of times base T shows up is: ", s_3.count("T"))
print("The percentage of A is: ", s_3.perc("A"))
print("The percentage of G is: ", s_3.perc("G"))
print("The percentage of C is: ", s_3.perc("C"))
print("The percentage of T is: ", s_3.perc("T"))

print("The length of the fourth sequence", s_4.strbases, "is: ", s_4.len())
print("The number of times base A shows up is: ", s_4.count("A"))
print("The number of times base G shows up is: ", s_4.count("G"))
print("The number of times base C shows up is: ", s_4.count("C"))
print("The number of times base T shows up is: ", s_4.count("T"))
print("The percentage of A is: ", s_4.perc("A"))
print("The percentage of G is: ", s_4.perc("G"))
print("The percentage of C is: ", s_4.perc("C"))
print("The percentage of T is: ", s_4.perc("T"))




