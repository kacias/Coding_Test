from typing import List
import sys



#주식 최대 수익율 계산하기
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
        return max_price

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        print(min_price)
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

'''

#=======================================
if __name__ == "__main__":

    #===========================
    a = Solution()
    b= a.maxProfit([1,4,3,6,2])

    print(b)
    #===========================
