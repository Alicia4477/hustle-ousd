#Code Snippet 1:
# Incorrect: Undefinded if divided by 0, fixed by adding another number other than 0
x = 10
y = 7
result = x / y
print("Result:", result)

#Code Snippet 2:
# Incorrect: It had i +1 but that wasn't going to work, fixed by taking i and only +1
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[+1])

#Code Snippet 3:
# Incorrect: After the () in line 16 it had no sintex, fixed by adding :
def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

#Code Snippet 4:
# Incorrect: Missing sintex and fixed by adding :
def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

#Code Snippet 5:
# Incorrect: Also missing an sintex and fixed by adding :
for i in range(5):
   print(i)

#Code Snippet 6:
# Incorrect: They weren't added together, fixed by adding +
def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

#Code Snippet 7:
# Incorrect: They were missing indent, fixed by doing an indent on line 51
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers:", sum)

 #Code Snippet 8:
# Incorrect: The equation was wrong, fixed by adding (n-1)
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

#Code Snippet 9:
# Incorrect: Says my name instead of stranger, fixed by addingg () on line 67
name = input("Enter your name: ")
if name == ("Alice" or "Bob"):
   print("Hello, " + name)
else:
   print("Hello, stranger!")

#Code Snippet 10:
# Incorrect: Undefind if 0, fixed by changing num2 = 4
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 4
print(divide_numbers(num1, num2))