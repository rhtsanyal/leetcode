class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_with_indices = [[i,nums[i]] for i in range(len(nums))]
        nums_with_indices.sort(key=lambda x:x[1])
        i = 0
        j = len(nums_with_indices) - 1
        while i < j:
            if nums_with_indices[i][1] + nums_with_indices[j][1] > target:
                j-=1
            elif nums_with_indices[i][1] + nums_with_indices[j][1] < target:
                i += 1
            else:
                return [nums_with_indices[i][0],nums_with_indices[j][0]]


print(Solution().twoSum([3,2,4],6))