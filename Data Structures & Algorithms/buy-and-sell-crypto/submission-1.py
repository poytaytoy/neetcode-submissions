class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_list = [0] * len(prices)
        current_max = float('-inf')

        for i in range(len(prices) - 1, -1, -1): 
            max_list[i] = current_max
            current_max = max(prices[i], current_max)


        best_price = 0
        for i in range(0, len(prices)):
            best_price = max(best_price, max_list[i] - prices[i])

        return best_price