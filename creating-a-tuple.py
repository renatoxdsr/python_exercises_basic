# Creating a tuple
# As you build your recipe scaler, you may need to convert between units. 
# Let's say you need to store standard conversion factors that should never change (like cups to milliliters: 1 cup = 240 ml). 
# A great way to store this is using tuples to represent the conversion pair. 
# Tuples are perfect for this because they're immutable - conversion factors won't accidentally change during calculations.

# Instructions:
# Create a tuple called cup_conversion that stores the values 1 and 240.
# Check the type of cup_conversion.
# Create a tuple
cup_conversion = (1, 240);

# Check the type
print(type(cup_conversion));
