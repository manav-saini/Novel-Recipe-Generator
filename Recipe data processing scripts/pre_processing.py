import pandas as pd
import math
recipes = pd.read_pickle("Recipe.pkl")
recipes = recipes[(recipes['ingredient_count']>=3)&(recipes['instruction_length']>=10)]
recipes['combined'] = ' \n Ingredients: \n ' + recipes.ingredients.str.join(' \n ') + ' \n Instructions: \n ' + recipes['instructions'] + ' <|endoftext|> '
recipes.to_pickle("processed_recipes.pkl")