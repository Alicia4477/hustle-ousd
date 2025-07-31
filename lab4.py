# Task 1

continue_checking = "yes"

while continue_checking == 'yes':
    age = int(input("Enter an age: "))
    if age >= 18:
        print ("Elgible to vote")
    else:
        print ("Not elgible to vote")

    print("Would you like to check another age?" )
    yesorno = input("Enter yes or no. ")
    continue_checking = yesorno

# Task 2

numbers = [4,0,-7,10,15,-12,25,28,0,-2]

for i in numbers:
    if i > 0 :
        print (f"This number {i} is positive")
    elif i < 0 :
        print (f"This number {i} negative")
    else:
        print (f"The number {i} is zero")

#Task 3

blocks = ["Coal", "dirt", "diamond", "gravel", "stone"]

for i in blocks:
    if i == "diamond":
        print("You found a diamond. Jackpot!")
    else:
        print(f"You found {i} instead")
    

