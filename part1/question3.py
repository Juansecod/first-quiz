################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class Oven:
  ingredients: list
  output: str
  output_freeze: dict = {
    "snow": ["water", "air"],
  }
  output_boil: dict = {
    "gold": ["lead", "mercury"],
    "pizza": ["cheese", "dough", "tomato"],
  }
  output_wait: dict = {
    "sandwich": ["bread", "ham", "cheese"]
  }
  
  def __init__(self):
    self.ingredients = []
  
  def add(self, item: str) -> None:
    self.ingredients.append(item)

  def freeze(self) -> None:
    self.output = "Something freezed"
    for output in self.output_freeze:
      if set(self.output_freeze.get(output)) == set(self.ingredients):
        self.output = output
        break

  def boil(self) -> None:
    self.output = "Something boiled"
    for output in self.output_boil:
      if (set(self.output_boil.get(output)) == set(self.ingredients)):
        self.output = output
        break
  
  def wait(self) -> None:
    self.output = "Ingredients combined"
    for output in self.output_wait:
      if (set(self.output_wait.get(output)) == set(self.ingredients)):
        self.output = output
        break
  
  def get_output(self) -> str:
    return self.output

def make_oven() -> Oven:
  return Oven()

def alchemy_combine(oven: Oven, ingredients: list, temperature: int):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()