#Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

a = int(input ("Enter the number in an argument:"))
#lambda function to find the value 
add_the_number_25 = lambda x: x + 25 
result = add_the_number_25(a)
print(f"The result of adding 25 to {a} is: {result}")