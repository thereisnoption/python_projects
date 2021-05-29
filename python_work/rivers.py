rivers = {'egypt' : "nile", 'brazil' : "amazon", 'china' : "mekong"}

for country, river in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.values():
	print(river.title())

for country in rivers.keys():
	print(country.title())