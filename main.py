# DAY1 👇
# print("hi") 
# city = input ("Wha city did you grow up in?\n")
# pet = input ("Wha pet name?\n")
# print ("The name of your band: " + city + pet)

# DAY2 👇
#print ("Gello"[4])

# Преобразование типов данных
# two_digit_number = input()

# first_num = int(two_digit_number[0])
# sec_num = int(two_digit_number[1])

# two_digit_number = first_num + sec_num
# print (two_digit_number)

# height = input()
# weight = input()

# height_1 = int(height)
# weight_1 = int(weight)

# bmi = weight_1/(height_1**2)
# print (bmi)

#CALCULATOR

print ("Welcome to the tip calculator!")
total_bill = input ("What was the total bill? $ ")
tip = input ("How much would you like to give? 10, 12, or 15? ")
people = input ("How many people to split the bill? ")

total_bill_tip = ((int(total_bill)/100*int(tip) + int(total_bill)))
result = total_bill_tip/int(people)
result1 = round (result, 2)
print (f"Each person should pay: ${result1}")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")


height = float(input())  # in meters e.g., 1.55
weight = int(input())  # in kilograms e.g., 72
# Your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")


print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


#DAY4 👇
names = names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice])


line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Your code below
letter = position[0].lower() #делаем текст мелким и ставим инпут в нулевую позицию
abc = ["a", "b", "c"] 
letter_index = abc.index(letter)  #находим индекс буквы в списке abc
number_index = int(position[1]) - 1 #
map[number_index][letter_index] = "X" #Схлапывает число 

print(f"{line1}\n{line2}\n{line3}")


#DAY5 👇
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) #Convert into list

total_height = 0
for height in student_heights:
  total_height += height
  print(f"total height = {total_height}")

