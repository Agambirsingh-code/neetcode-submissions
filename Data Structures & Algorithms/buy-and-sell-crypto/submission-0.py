class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        highest = 0
        for i in prices:
            if i < lowest:
                lowest = i
            elif i - lowest > highest:
                highest = i-lowest
        return highest
            