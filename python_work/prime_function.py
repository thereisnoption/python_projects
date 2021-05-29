primes = [value for value in range(2,101)]

for even in primes:
	if even == 2:
		continue
	elif even % 2 == 0:
		primes.remove(even)

for composite in primes:
	for i in (composite // 2):
		if composite % i == 0:
			primes.remove(composite)

print(primes)
print(len(primes))