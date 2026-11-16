class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[left] < nums[right]:
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            # [4, 5, 1, 2, 3]
            elif nums[mid] < nums[right] < nums[left]:
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # [3, 4, 5, 6, 1, 2]
            else:
                if nums[mid] == target:
                    return mid
                elif nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1