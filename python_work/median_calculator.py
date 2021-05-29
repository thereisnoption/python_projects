# Median calculator

numbers = []
number = "something"

print("Welcome to Median Calculator \n")

while number.lower() != "stop":
	number = input("Enter your data set: ")
	numbers.append(number)

del numbers[-1]
numbers.sort()

if len(numbers) % 2 == 0:
	i = (len(numbers) / 2)
	n = i + 1
	i, n = int(i), int(n)
	median = (numbers[i-1] + numbers[n-1]) / 2
	print("\nMedian:", median)
else:
	i = (len(numbers) + 1) / 2
	i = int(i)
	print("\nMedian:", numbers[i-1])

input()