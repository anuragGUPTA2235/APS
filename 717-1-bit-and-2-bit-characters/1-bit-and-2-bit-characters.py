class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        tracker = 0
        while tracker < len(bits) - 1:
            i =tracker
            if bits[i] == 0:
                tracker += 1
            elif bits[i] == 1:
                tracker += 2
        if tracker ==  len(bits) - 1:
            return True
        else:
            return False               
