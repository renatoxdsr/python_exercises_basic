# Working with sets
# While building your recipe scaler, you decide to create a shopping list from multiple recipes. You've been collecting ingredients in a list called all_ingredients. Since the same ingredients appear in different recipes, their names appear more than once in the list. You want to create a set to see exactly how many unique ingredients you need to buy. 
# The all_ingredients list has already been created for you.

# Instructions:
# 01-  call set()
# Given sets' unique properties, we might want to convert another data type, such as a list, to a set. This process is known as casting.
# Convert the all_ingredients list to a set
unique_ingredients = set(all_ingredients);

# 02- .sorted() - returning all unique values in alphabetical order
print(sorted(unique_ingredients));

# 02.1- Sort the unique_ingredients to show the items listed alphabetically.
# Convert the all_ingredients list to a set
unique_ingredients = set(all_ingredients)

# Sort unique_ingredients alphabetically
print(sorted(unique_ingredients))
