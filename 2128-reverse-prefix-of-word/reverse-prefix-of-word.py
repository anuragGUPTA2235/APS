class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        flag = 0
        if ch not in word:
            return word
        else:
            res = ""
            for index,items in enumerate(word):
                if items == ch and flag == 0:
                    res = res + items
                    print(res)
                    a = list(res)
                    a[::] = a[::][::-1]
                    res = "".join(a)
                    flag = 1

                else:
                    res = res + items
            return res  
        