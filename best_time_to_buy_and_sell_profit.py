def profit(prices):

    max_profit= 0
    min_val = prices[0]
    for val in range(1,len(prices)):
        if prices[val] < min_val:
            min_val = prices[val]
        max_profit = max(max_profit, prices[val] - min_val)            
    return max_profit


print(profit([7,6,4,3,1]))