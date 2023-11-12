class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c**0.5)
        current_sum = a**2 + b**2
        while a <= b:
            current_sum = a**2 + b**2
            if current_sum == c:
                return True
            elif current_sum < c: 
                a+=1
            else: 
                b-=1
        return False
            
