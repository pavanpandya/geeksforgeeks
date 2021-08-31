class Solution:

    def rowWithMax1s(self, arr, n, m):
        # code here
        pass


# if __name__ == '__main__':
#     tc = int(input())
#     while tc > 0:
#         n, m = list(map(int, input().strip().split()))

#         inputLine = list(map(int, input().strip().split()))
#         arr = [[0 for j in range(m)] for i in range(n)]

#         for i in range(n):
#             for j in range(m):
#                 arr[i][j] = inputLine[i * m + j]
#         ob = Solution()
#         ans = ob.rowWithMar1s(arr, n, m)
#         print(ans)
#         tc -= 1

n, m = list(map(int, input().strip().split()))

inputLine = list(map(int, input().strip().split()))
arr = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = inputLine[i * m + j]

ans = arr[:1, :]
print(ans)
