class Solution:
    def search(self, nums: List[int], target: int) -> int:

# binary search tree
# two pointers
        left, right = 0, len(nums) - 1
        if target not in nums:
            return -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # check left sorted portion
            if nums[left] <= nums[mid]:
                if nums[mid] < target or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
            
