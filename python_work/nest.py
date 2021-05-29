# Graduation wishes

students = {
	'albertein' : {
	'first' : "albert",
	'last' : "einstein",
	'grade' : 12,
	'gpa' : 3.9,
	},

	'mariecu' : {
	'first' : "marie",
	'last' : "curie",
	'grade' : 12,
	'gpa' : 3.6,
	},

	'newton' : {
	'first' : "isaac",
	'last' : "newton",
	'grade' : 12,
	'gpa' : 4,
	},

	'niktel' : {
	'first' : "nikola",
	'last' : "tesla",
	'grade' : 12,
	'gpa' : 3.89,
	}
}

for student_information in students.values():
	full_name = f"{student_information['first']} {student_information['last']}"
	grade = student_information['grade']
	gpa = float(student_information['gpa'])

	# To define the praise for the graduate
	if gpa <= 3.7:
		praise = "cum laude"
	elif gpa <= 3.9:
		praise = "magna cum laude"
	elif gpa >= 4:
		praise = "summa cum laude"

	# The wishes
	print(f"\nCongratulations {full_name.title()} on your graduation from University of Indonesia!")
	print(f"Your GPA is {gpa} ({praise.title()})")

input()