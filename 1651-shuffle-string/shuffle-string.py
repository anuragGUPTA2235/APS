class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        hashmap = {}
        for index,items in enumerate(indices):
            hashmap[items] = s[index]

        print(hashmap)

        indices.sort()

        res = ""

        for i in range(len(indices)):
            res = res + hashmap[indices[i]]

        return res    