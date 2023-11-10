class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(arr):
            if arr[i] > arr[i+1]:
                return 0
