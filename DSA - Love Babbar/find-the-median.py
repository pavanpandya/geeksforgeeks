# User function Template for python3

class Solution:
    def find_median(self, v):
        sorted_value = v.copy()
        sorted_value.sort()
        length = len(sorted_value)
        if length % 2 == 0:
            m1 = int((length / 2)-1)
            m2 = int(length / 2)
            summation = sorted_value[m1] + sorted_value[m2]
            return int(summation/2)
        else:
            median = sorted_value[int(length/2)]
        return median


ob = Solution()
ans = ob.find_median([1, 5, 9, 8, 7, 3])
# ans = ob.find_median([1, 3, 5, 7, 8, 9])
print(ans)
