class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        list = [str(items) for items in nums]
        print(list)

        ans = []

        for items in list:
            for jtems in items:
                ans.append(jtems)

        answer = [int(items) for items in ans]         
        return answer
        