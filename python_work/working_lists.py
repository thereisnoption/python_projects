# magicians = ["alice", "david", "carolina", "daniel", "jack", "paul"]

# for magician in magicians:
#	print(f"{magician.title()}, that was an amazing trick!")

numbers = [2, 2, 1, 2, 2, 2, 5, 1]
modes = []

m = 0
for i in numbers:
	n = numbers.count(i)
	modes.append(n)
	if n >= m:
		m = n
	else:
		mode = i

print(modes)
print(max(modes))
print(m)
print(mode)	