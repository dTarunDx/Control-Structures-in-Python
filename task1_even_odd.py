#Greeting message
print("Hello!Enter an integer to find out if it's even or odd")

# Input from User
a = int(input("Enter an integer: "))
# Result
if a % 2 == 0:
    print (a,"is an even Number")
else:
    print (a,"is an odd Number")