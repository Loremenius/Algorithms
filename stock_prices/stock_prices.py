#!/usr/bin/python

import argparse

def find_max_profit(prices):
  minPrice = prices[0]
  maxProfit = prices[1] - prices[0]
  for i in range(len(prices)-1):
    if prices[i] < minPrice:
      minPrice = prices[i]
    
    if prices[i+1] - minPrice > maxProfit:
      maxProfit = prices[i+1] - minPrice
  
  return maxProfit

print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]))



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))