class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ 
        maxprofit = 0
        for i in range(len(prices)-1):
            currentprice = prices[i]
            maxprice = max(prices[i+1:])
            if maxprice > currentprice:
                profit = maxprice  - currentprice
                if profit  > maxprofit:
                    maxprofit = profit

        return maxprofit 
        """         
        maxprofit = 0
        minvalue = float(inf)
        for i in range(1,len(prices)):
            if prices[i-1] < minvalue:
                minvalue = prices[i-1]
            profit = prices[i] - minvalue
            if profit > maxprofit:
                maxprofit  = profit  

        return maxprofit        
                
  
    
        