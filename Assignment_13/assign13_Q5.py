def Grades(No):
    
    if No>=75:
        return "Distinction"
    elif No>=60:
        return "First Class"
    elif No>=50:
        return "Second class"
    else:
        return "Fail"
    
No=int(input("Enter your marks: "))
Res=Grades(No)
print(f"Grade is : {Res}")