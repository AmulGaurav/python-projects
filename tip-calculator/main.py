print("Welcome to the Tip calculator!")

bill = float(input("What is the total bill? $"))

tip_percentage = int(input("What percentage tip would you like to give: 10 , 12 or 15? "))

no_of_people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (tip_percentage / 100 + 1)

bill_per_person = bill_with_tip / no_of_people

print(f"Each person should pay : ${bill_per_person:.2f}")