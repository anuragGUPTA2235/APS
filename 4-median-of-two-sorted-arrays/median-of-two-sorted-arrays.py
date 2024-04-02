class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        res = nums1 + nums2
        print(res)
        res.sort()
        print(res)

        if len(res) % 2 != 0:
            index = len(res) // 2
            return res[index]


        else:
            index = len(res) // 2
            print(index)
            return (res[index] + res[index-1]) / 2    



        return 7
        