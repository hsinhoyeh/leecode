class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        bestBuy = prices[0]
        bestSell = prices[0]
        bestProfit = bestSell - bestBuy

        for i in range(1, len(prices)):
            price = prices[i]
            if price > bestSell:
                bestSell = price
                profit = bestSell - bestBuy
                if profit > bestProfit:
                    bestProfit = profit
            if price < bestBuy:
                bestBuy = price
                bestSell = price

        return bestProfit
