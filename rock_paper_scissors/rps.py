#!/usr/bin/python

import sys
def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  combos = []

  def addCombo(playedSoFar, rounds):
    if rounds < 1:
      combos.append(playedSoFar)
    else:
      for i in range(len(options)):
        addCombo(playedSoFar + [options[i]], rounds - 1)
    
  addCombo([],n)
  return combos

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')