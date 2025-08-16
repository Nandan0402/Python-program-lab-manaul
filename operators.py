def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "Error if divided by 0!"
    return a/b
def mod(a,b):
    if b==0:
        return "Error if divided by 0!"
    return a%b
def power(a,b):
    return a**b
def floor_div(a,b):
    if b==0:
        return "Error if divided by 0!"
    return a//b

n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))

print("Select the operations:")

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Exponentiation (Power)")
print("7.Floor Division")

c=int(input("Enter the choice(1/2/3/4/5/6/7):"))

if c==1:
    print("Addition:",add(n1,n2))
elif c==2:
    print("Subtraction:",sub(n1,n2))
elif c==3:
    print("Multiplication:",mul(n1,n2))
elif c==4:
    print("Division:",div(n1,n2))
elif c==5:
    print("Modulus:",mod(n1,n2))
elif c==6:
    print("Power:",power(n1,n2))
elif c==7:
    print("Floor Division:",floor_div(n1,n2))
else:
    print("Invalid choice")
