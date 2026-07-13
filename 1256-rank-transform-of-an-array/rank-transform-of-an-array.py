class Solution(object):
    def arrayRankTransform(self, arr):
        temp = sorted(set(arr))

        d = {}

        for i in range(len(temp)):
            d[temp[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = d[arr[i]]

        return arr