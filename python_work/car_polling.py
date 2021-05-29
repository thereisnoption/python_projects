# Favorite Car Polling

responses = {}

# Set the flag to indicate that the polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	response = input("What is your favorite car? ")

	# Store the response in the dictionary.
	responses[name] = response

	# Find out if anyone else want to take the poll.
	repeat = input("Would you like to submit another response? (yes/no) ")
	if repeat.lower() == "no":
		polling_active = False

# Print out the polling results.
print("\n--- Poll Results ---\n")

for name, response in responses.items():
	print(f"{name.title()}'s favorite car is {response.title()}.")

# Just to make sure that the terminal doesn't close itself when the code is done.
input()