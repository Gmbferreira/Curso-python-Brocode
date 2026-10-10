age = int(input("What is your age?: "))

if age >= 18 and age <200:
    print("You are now signed up!")
    
elif age<0:
    print ("You must be forn first")

elif age >= 200:
    print ("You must be human")
else:
    print("You must be 18 years or older")