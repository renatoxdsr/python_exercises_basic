# Using a while loop
# You're building the recipe scaler and need to count how many guests have confirmed attendance for your pasta party. 
# You've received RSVPs and want to process them one by one using a while loop. You have a variable total_confirmations representing the number of RSVPs received, and you need to count through them to determine the final guest count. 
# This will help you know how much to scale the tomato and basil pasta recipe.

# Note that if your while loop takes too long to run, or your session is expiring, you might have created an infinite loop. In particular, remember to indent the contents of the loop using four spaces or auto-indentation, and make sure the conditions are such that the loop has a stopping point.

# Instructions:

# Write a while loop that continues as long as guest_count is less than total_confirmations.
# Inside the while loop, increment guest_count by 1 each time to count another confirmation.

total_confirmations = 10
guest_count = 0

# Count confirmations using a while loop
while guest_count < total_confirmations:
    guest_count = guest_count + 1;
    print(guest_count, "guests so far!")

print("We have", guest_count, "guests coming!")
