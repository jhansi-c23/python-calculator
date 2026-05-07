n1 = int(input("Enter a number:"))
n2 = int(input("Enter a number:"))
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2
print("Please select operator -\n"
      "1.Add\n"
      "2.subtract\n"
      "3.multiply\n"
      "4.division\n")
sel = int(input("select operation(1-4):"))
n1 = int(input("enter a first number:"))
n2 = int(input("enter a second number:"))
if sel ==1:
    print(n1, "+", n2, "=", add(n1,n2))
elif sel ==2:
    print(n1, "-", n2, "=", subtract(n1,n2))
elif sel ==3:
    print(n1, "*", n2, "=", multiply(n1,n2))
elif sel ==4:
    print(n1, "/", n2, "=", division(n1,n2))
else:
    print("Ivalid input, please enter a valid input")