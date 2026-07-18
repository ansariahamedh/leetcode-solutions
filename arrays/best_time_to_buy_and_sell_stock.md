# Best Time to Buy and Sell Stock (#121)

## Pattern

Running Minimum / Greedy

## Idea

Keep track of the lowest stock price seen so far.
For every new price, calculate the profit if sold today.
Update the maximum profit whenever a better profit is found.

## Time Complexity

O(n)

Reason:
We traverse the array only once.

## Space Complexity

O(1)

Reason:
We only use three variables:
- min_price
- max_profit
- num