class Seq:
    def __init__(self, strbases):   #SIEMPRE
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        empty = ""
        for letter in self.strbases:
            if letter == "A":
                empty += "T"
            if letter == "T":
                empty += "A"
            if letter == "G":
                empty += "C"
            if letter == 'C':
                empty += "G"
        return Seq(empty)   #here i've created an object

    def reverse(self):
        return self.strbases[::-1]

    def count(self, base):
        result = 0
        for e in self.strbases:
            if e == base:
                result += 1
        return result


s_1 = Seq("AAAGCTCTCGATCTGA")
str_1 = s_1.strbases

l1 = s_1.len()
c1 = s_1.complement()
r1 = s_1.reverse()
result_A = s_1.count("A")
result_G = s_1.count("G")
result_C = s_1.count("C")
result_T = s_1.count("T")



print("The length of the sequence is: ", l1)
print("The complementary sequence is: ", c1.strbases) #so it doesnt shows up as an object
print("The reverse sequence is: ", r1)
print("The number of times base A shows up is: ", result_A)
print("The number of times base G shows up is: ", result_G)
print("The number of times base C shows up is: ", result_C)
print("The number of times base T shows up is: ", result_T)

