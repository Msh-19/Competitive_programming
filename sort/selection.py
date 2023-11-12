class Solution:
    #Function to select the maximum element and its index in the array.
    def select(self, arr, i):
        max = arr[0]
        idx = 0
        for j in range(1,i+1):
            #updating the index and maximum value if a larger element is found.
            if arr[j] > max:
                idx = j
                max = arr[j]
        return idx
    
    #Function to perform selection sort on the array.
    def selectionSort(self, arr, n):
        
        #iterating over the array in reverse order.
        for i in range(n-1,0, -1):
            
            #selecting the maximum element and its index.
            j = self.select(arr,i)
    
            #swapping the maximum element with the current element.
            arr[i], arr[j] = arr[j], arr[i]

