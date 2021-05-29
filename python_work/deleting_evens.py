odds = [value for value in range(1,101)]

for odd in odds:
	if odd % 2 == 0:
		odds.remove(odd)

print(odds)