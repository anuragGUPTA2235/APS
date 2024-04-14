class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        hashmap = {}

        for index,items in enumerate(nums):

            if items in hashmap and abs(index-hashmap[items]) <= k:
                return True
            
            hashmap[items] = index
        return False            


