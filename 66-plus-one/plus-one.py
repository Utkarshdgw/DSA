class Solution(object):
    def plusOne(self, digits):

        digit = digits[::-1]

        for i in range(len(digit)):
            if digit[i] < 9:
                digit[i] += 1
                return digit[::-1]
            else:
                digit[i] = 0

        return [1] + digit[::-1]
        