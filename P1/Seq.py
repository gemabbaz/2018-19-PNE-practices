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



s_1 = Seq("AAAGCTCTCGATCTGA")
str_1 = s_1.strbases

l1 = s_1.len()
c1 = s_1.complement()
r1 = s_1.reverse()



print(l1)
print(c1.strbases) #so it doesnt shows up as an object
print(r1)
