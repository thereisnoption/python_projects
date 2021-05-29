# Printing each design.
def printing(unprinted_designs, completed_models):
	while  unprinted_designs:
		current_design = unprinted_designs.pop()
		completed_models.append(current_design)
		print(f"Printing model {current_design}")

# Completed models.
def finished(completed_models):
	for completed_model in completed_models:
		print(completed_model)

# The list of designs that need to be printed.
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

printing(unprinted_designs, completed_models)
finished(completed_models)