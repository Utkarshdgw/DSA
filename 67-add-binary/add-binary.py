class Solution(object):
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)

        total = a + b

        return bin(total)[2:]