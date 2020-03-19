#!/usr/bin/python

import sys
def addCombo(arr, n):
  plays = ['rock', 'paper', 'scissors'] 
  if n > 0:
    for play in plays:
      newArr = []
      newArr = [play] + addCombo(newArr, n-1)
      arr = arr + newArr
  return arr

print(addCombo([],2))

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  arr = []
  for play in plays:
    arr = arr + addCombo([play], n-1)
  
  return arr

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')