# Lab 3

# Task 1: Working with Strings
food = 'tacos'
#print (food[0:3]) #print first 3 characters 
#print(food[-3:]) #print last 3 characters 
first_last = food[0] + food[-1] #combine first and last characters 
#print(first_last)
food_list = food.split()
#print(food_list)
joined_food = ' '.join(food_list)
#print(joined_food)

# Task 2: Working with lists
number_list = [4, 7, 14, 25, 28, 44,]
number_list.append(10)
#print(number_list)
number_list.insert(7,28) #3
#print(number_list)
number_list.pop() #4
number_list.remove(7) #5
print(number_list)
print(number_list[0:3])
print(number_list[-3:])



# Task 3: working with Dictionaries (key: value)
books = {"Mary Downing Hahn" : "Wait Till Helen Comes", 
"Assata Shakur" : "Assata", 
"Raina Telgemeier" : "Ghost", 
"Tommy Orange" : "There There"} #1
print(books.keys()) #2
print(books.values()) #3
print(books.get("Tommy Orange")) #4