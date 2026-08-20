class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longetc = 1
        currc = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                currc +=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                currc = 1
            if longetc < currc:
                longetc = currc
        return longetc
