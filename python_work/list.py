# Lists

motorcycle_brands = ["honda", "yamaha", "suzuki", "ducati", "BMW"]

# This line of code changes the specific element in the list by its index.
# motorcycle_brands[0] = "kawasaki"

# This line of code adds a new element at the end of the list.
# motorcycle_brands.append("kawasaki")

# This line of code adds a new element at any position by its index.
# motorcycle_brands.insert(5, "kawasaki")

# These lines of code remove elements in the list (for more specific I will write the information next to the codes).
# del motorcycle_brands[0] removes an element in the list by its index and NEVER use it again.
# popped_motorcycle = motorcycle_brands.pop() removes an element in the list by its index and use it in some cases (don't have to use variable).
# motorcycle_brands.remove("honda") removes by value.

message = f"My motorcycle is {motorcycle_brands[0].title()}. But I want a {motorcycle_brands[-1].title()} motorcycle."

print(message)