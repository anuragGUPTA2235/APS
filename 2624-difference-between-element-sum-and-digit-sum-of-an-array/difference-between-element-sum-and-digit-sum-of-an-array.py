class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum = 0
        for items in nums:
            digit_sum += items

        element_sum = 0
        ele_list  = [str(items) for items in nums]
        for items in ele_list:
            for jtems in items:
                element_sum += int(jtems)


        return abs(digit_sum - element_sum)           
        