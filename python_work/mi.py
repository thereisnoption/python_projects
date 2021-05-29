orders = ["mi goreng", "mi rebus", "mi rebus telur", "mi goreng telur"]
finished_orders = []

while orders:
	cooking = orders.pop()

	finished_orders.append(cooking)

for order in finished_orders:
	print(f"{order.title()} is done.")