class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:

        res = ""

        for items in words:
            res = res + items[0]

        return res == s   
        