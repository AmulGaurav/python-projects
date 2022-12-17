print("Welcome to the Love Calculator!")

gender = input("Are you a Boy or a Girl?\n")

name1 = input("What is your name?\n")

if (name1 == "Boy") or (name1 == "boy"):
    name2 = input("What is her name?\n")
else:
    name2 = input("What is his name?\n")

combined_name = name1.lower() + name2.lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

true_count = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')

love_count = l + o + v + e

love_score = int(str(true_count) + str(love_count))

print(f"Your love score is: {love_score}")