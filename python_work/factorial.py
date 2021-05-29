print("Welcome to Factorial Calculator")

# Factorial function
def factorial(x):
	if x < 0:
		return 0
	elif x == 0 or x == 1:
		return 1
	else:
		fact = 1
		while x > 1:
			fact *= x
			x -= 1
		return fact

# Set the flag to indicate that the calculator is active.
calc_active = True

while calc_active:
	# Prompt user to input number.
	n = input("\nType your number here: ")
	n = int(n)

	# Print out the result.
	print(f"Factorial of {n} is {factorial(n)}")

	# Find out if the user wants to calculate again.
	repeat = input("\nWant to calculate again? (yes/no) ")
	if repeat.lower() == "no":
		calc_active = False