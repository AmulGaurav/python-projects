print("Welcome to the BMI calculator ")

#To remove a line
print()

weight = input("Enter your weight in kg : ")
height = input("Enter your height in m : ")

weight = float(weight)
height = float(height)

BMI = round((weight / height ** 2) , 1)
print(BMI)