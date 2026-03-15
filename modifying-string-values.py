# Modifying string values
# Your recipe scaler project needs to handle ingredient names that users might enter in different formats. 
# You want to update any generic entries to make your recipe clearer. 
# Additionally, to ensure your shopping list doesn't have duplicate entries, you need to standardize all ingredient names to lowercase.

# Instructions:

# Use the .replace() method to update pasta_type by changing "pasta" to "fusilli pasta".
# Convert the ingredient_one variable to lowercase using the .lower() method.

# explaining .replace()
# .replace() expected at least 2 arguments
# .replace("pasta", "fusilli pasta")

pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta", "fusilli pasta");

ingredient_one = "BASIL";

# Standardize ingredient_one to lowercase
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)
