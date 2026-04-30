class Solution:
    def rotate(self, nums: List[int], k: int) -> None:   
        pt = len(nums)
        res = nums.copy()
        for i in range(len(nums)): 
            idx = (i + k) % pt 
            nums[idx] = res[i] 
        return nums 