from calculator_logo import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  if n2 != 0:
    return n1 / n2
  else:
    return "Invalid input denominator cannot be equal to 0"

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  while True:
    operation = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    function = operations[operation]
    answer = function(num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if should_continue != "y":
      calculator()
    num1 = answer

calculator()