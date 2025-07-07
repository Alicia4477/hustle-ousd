# Lab 5 Alicia Pablo

# Cat Function 
def cat_greeting(word):
    print(f'Cat says {word}')
    print(f'Cat says {word}')
    print(f'Cat says nothingg')

cat_greeting("mua mua")

# Step 2
def generate_superhero_power():
    name = "Alicia"
    power = "invisible"
    print(f"{name}'s power is {power}")

generate_superhero_power()

# Step 3
def generate_superhero_power1():
    power = "invisible"
    return power

print (generate_superhero_power1())

# Step 4
def generate_superhero_power2(user_name, super_power):
    message = user_name + "has the power of" + super_power + "!"
    return message

print(generate_superhero_power2 ("Fredy", "flying"))

# Step 5
def cat_greeting_loop():
    #for i in range (7):
   #     print(f'The cat says {greeting}')

    greetings = ["mua mua", "meow", "grrrrr", "mmmmm"]

    for i in greetings:
      print(" The cat says", i)

cat_greeting_loop()

# Step 6 
def generate_multiple_power(powers):
    for i in powers:
        print(i)

powers_tests = ["flying", "Invisible", "speed", "teleport", "super strength"]
generate_multiple_power(powers_tests)