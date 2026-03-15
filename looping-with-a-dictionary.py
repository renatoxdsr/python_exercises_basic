
# Looping with a dictionary
# Your recipe scaler is coming together! 
# You have a dictionary called recipe that contains ingredient names as keys and their quantities in grams as values for your tomato and basil pasta. Now you need to scale all the quantities by a factor of 2 to serve more guests at your party. 
# You'll loop through the dictionary items and calculate the scaled quantities.

# Instructions:
# Use a for loop to iterate through the recipe dictionary, using ingredient and qty as your iterators.
# Inside the loop, create a variable called scaled_qty that multiplies the original quantity by the scaling factor of 2.

recipe = {
    "fusilli": 500,
    "tomatoes": 400,
    "basil": 20,
    "garlic": 15,
    "olive oil": 15,
    "salt": 7
}

# Loop through the recipe dictionary items
for ingredient, qty in recipe.items():
    # Calculate the scaled quantity by multiplying by 2
    scaled_qty = qty * 2;
    
    print(ingredient, ":", scaled_qty, "g")
