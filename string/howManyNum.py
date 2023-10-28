def smallerNumbersThanCurrent(nums):
    n = len(nums)
    result = []
    
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and nums[j] < nums[i]:
                count += 1
        result.append(count)
    
    return result

# Example usage
nums = [8, 1, 2, 2, 3]
output = smallerNumbersThanCurrent(nums)
print(output)  # Output: [4, 0, 1, 1, 3]
