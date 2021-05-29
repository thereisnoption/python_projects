alien_0 = {"x_position" : 15, "y_position" : 15, "speed" : "fast"}
print(f"Original position : {alien_0['x_position']}")

if alien_0['speed'] == "slow":
	x_increment = 1
elif alien_0['speed'] == "medium":
	x_increment = 2
elif alien_0['speed'] == "fast":
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position : {alien_0['x_position']}")

for key, value in alien_0.items():
	print(f"\nKey : {key}")
	print(f"Value : {value}")