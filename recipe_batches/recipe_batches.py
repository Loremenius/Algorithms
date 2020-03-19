#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  maxBatch = None
  for key in recipe:
    if ingredients.setdefault(key, 0) > 0:
      currentBatch = ingredients[key]// recipe[key] 
      if maxBatch is None:
        maxBatch = currentBatch
      elif currentBatch < maxBatch:
        maxBatch = currentBatch
    else:
      return 0

  return maxBatch 

print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))