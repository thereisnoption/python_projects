usernames = ["andi", "daniel", "sasha", "maya"]

new_username = input("Input your username here: ")

if new_username.lower() not in usernames:
	usernames.append(new_username.lower())
	print(f"Congratulation {new_username.title()}! your username has been added.")
else:
	print(f"{new_username.title()} already used!")

input()