#Looping through a list
# You're doing a trial run of cooking the pasta dish. First, you need to list all your ingredients to make sure you have everything ready.

# Then, you'll add them one by one as you cook — seven ingredients in total.

# Instructions:
# Create a for loop that iterates through the ingredients list, using item as the iterator variable.
ingredients = ["fusilli", "tomatoes", "garlic", "basil", "olive oil", "salt"]

# Loop through each ingredient in the list
for item in ingredients:
    print(item)

#Now create a for loop that iterates from 1 to 6 to keep track of how many ingredients you've added.
# Iterate over the number of ingredients
for item in range(1, 7):
    print("Adding ingredient", item)
