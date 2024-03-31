class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                res = ""
                if i != j:
                    res = res + nums[i] +  nums[j]
                   
                    if res == target:
                        print(res)
                        count += 1
        return count