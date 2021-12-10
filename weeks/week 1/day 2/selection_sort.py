# https://practice.geeksforgeeks.org/problems/selection-sort/1#

class Solution:
    def select(self, arr, i):
        val = arr[i]  # The value of the current element
        pos = i  # initial selection
        for j in range(i+1, len(arr)):
            if arr[j] < arr[pos]:
                pos = j
        return pos

    def selectionSort(self, arr, n):
        for i in range(n-1):
            p = self.select(arr, i)
            arr[p], arr[i] = arr[i], arr[p]  # Swap


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
