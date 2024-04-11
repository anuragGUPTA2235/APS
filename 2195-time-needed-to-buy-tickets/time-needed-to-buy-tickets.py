class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0
        while tickets[0] != 1 or k != 0:
            
            if tickets[0] != 1:
                tickets[0] -= 1
                man = tickets.pop(0)
                tickets.append(man)

            elif tickets[0] ==  1:
                tickets.pop(0)

            k = (k - 1) % len(tickets)
            
            counter += 1


                



           
            

        

        return counter + 1     



            

        