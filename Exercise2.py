# # Question 1: Arithmetic and Assignment Operators

# # TODO: Add 3 to x using the += operator
# x = int(input("Type in the value of x: "))
# x += 3

# # TODO: Multiply y by 2 using the *= operator
# y = int(input("Type in the value of y: "))
# y *= 2

# # TODO: Divide x by y and store the result in a variable called 'result'
# result = x/y

# # TODO: Print the value of 'result'
# print(x, "/", y, "=", result)

#------------------------------------------------------------------------------------
# # Question 2: Comparison and Logical Operators

# # TODO: Create a condition that checks if a is greater than b
# a = 5
# b = 1
# if a > b:
#   print("a is greater than b?", a > b)

# # TODO: Create a condition that checks if b is even (hint: use the modulus operator)
# if b % 2 == 0:
#   print("b is even")
# else:
#   print("b is uneven")

# # TODO: Create a condition that checks if c is less than or equal to a
# c = 5
# if c <= a:
#   print("Is c less than or equal to a?", c <= a)

# # TODO: Combine the above conditions using logical operators to create a 'final_condition'
# #       The 'final_condition' should be True if either:
# #       - a is greater than b, or
# #       - b is even and c is less than or equal to a
# def final_condition():
#   return a > b or b % 2 == 0 and c <= a

# # TODO: Print the value of 'final_condition'
# print("Final Condition:", final_condition())

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# # TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
# score = int(input("Enter the test score (0 - 100): "))

# # TODO: Implement a grading system using if-elif-else statements:
# #       90-100: A
# #       80-89: B
# #       70-79: C
# #       60-69: D
# #       Below 60: F
# grade = ""
# def grading(score):
#   if score >= 90:
#     grade = "A"
#   elif score >= 80 and score < 90:
#     grade = "B"
#   elif score >= 70 and score < 80:
#     grade = "C"
#   elif score >= 60 and score < 70:
#     grade = "D"
#   elif score < 60:
#     grade = "F"
#   return grade

# # TODO: Print the grade for the given score
# print("The student's grade:", grading(score))

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'

# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
# TODO: Handle the case of division by zero


# TODO: Print the result of the operation
