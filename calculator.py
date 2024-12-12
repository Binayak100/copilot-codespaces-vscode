def add(a,b):
   return(a+b)

def sub(a,b):
   return(a-b)

print("Welcome to calculator")
print("Choose 1 for add and 2 for sub")
x = int(input("Enter the value u want"))
if x == 1:
      num1=int(input("Enter value a"))
      num2=int(input("Enter value b"))
      addition = add(num1,num2)
      print(f"The sum is : {addition}")
elif x == 2:
      num1=int(input("Enter value a"))
      num2=int(input("Enter value b"))
      subtraction = sub(num1,num2)
      print(f"The sub is{subtraction}")
else:
     print("This is either add or sub")

       

