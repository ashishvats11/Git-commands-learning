#  we will be creating a code for calculating the BMI of Gym Freaks!!

#BMI - Body Mass Index --> Weight in kgs/ (height in meters)**2
# this is baisc bmi code using if else.
#In this code based on the BMI categories people among, under weight, normal weight and over weight
name = input("enter your name: ")
weight_kg = float(input("Enter your weight in kgs: ")) # when we take input from the console it considers it as string, need to type cast it to the required data type
height_m = float(input("Enter your height in meters: "))
bmi = round(weight_kg/(height_m)**2,2)

if bmi < 18:
    print(f"Hey {name}, your BMI is: {bmi} and you are under weight")
elif bmi >18 and bmi <24:
    print(f"Hey {name}, your BMI is: {bmi} and you are normal weight")
else:
    print(f"Hey {name}, your BMI is: {bmi} and you are over weight")