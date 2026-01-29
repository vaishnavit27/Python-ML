import Arithematic

print("Inside Client : ",__name__)

Result=0
No1=int(input("Enter first number : "))
No2=int(input("Enter Second Number : "))

Result=Arithematic.Add(No1,No2)
print(f"The addition of {No1} and {No2} is {Result}")

Result1=Arithematic.Sub(No1,No2)
print(f"The Subtraction of {No1} and {No2} is {Result1}")

Result2=Arithematic.Mul(No1,No2)
print(f"The multiplication of {No1} and {No2} is {Result2}")

Result3=Arithematic.Div(No1,No2)
print(f"The Division of {No1} and {No2} is {Result3}")
