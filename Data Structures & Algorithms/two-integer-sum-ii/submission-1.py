class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                while numbers[r - 1] == numbers[r]:
                    r -= 1
                r -= 1

            else:
                while numbers[l + 1] == numbers[l]:
                    l += 1
                l += 1