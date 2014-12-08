questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}
ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
answers = {
  "strong": "",
  "salty": "",
  "bitter": "",
  "sweet": "",
  "fruity": ""
}

import random

def type_drink(yes, no):
'''Function assigns True or False to the values in answers dictanary depending on users input'''
  for x in questions :
    if raw_input(questions[x]) == "yes":
      answers[x] = True
    else: 
      answers[x] = False 
  return answers
  
def make_drink():
  '''If values in answer dictonary are true, function will randomlly append an item from corresponding value in the ingredients dictonary to the drink list'''
  drink = []
  for x in answers:
    if answers[x] == True:
      drink.append(random.choice(ingredients[x]))
  print drink
  return drink
      
      
if __name__ == '__main__':
  type_drink("yes","no")
  make_drink()
