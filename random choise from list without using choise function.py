import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇 
#print(names)
x = len(names) - 1  
random_choise = random.randint(0,x)
person_who_will_pay = names[random_choise]

print(f"{person_who_will_pay} is going to buy the meal today!")
