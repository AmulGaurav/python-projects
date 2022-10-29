print("Welcome to the BMI calculator!")

#To remove a line
print()

weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))

BMI = round((weight / height ** 2) , 1)
print(BMI)