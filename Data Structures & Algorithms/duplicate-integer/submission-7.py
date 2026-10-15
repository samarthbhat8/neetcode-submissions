class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numberSet = {}
        for number in nums:
            if number in numberSet and numberSet[number] > 0:
                return True
            
            numberSet[number] = numberSet.get(number, 0) + 1
        
        return False