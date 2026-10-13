weight = float(input("Enter the weight: "))
unit = input("Kilograms (K) or Pounds (P): ").lower()

if unit == "k":
    weight = weight *2.205
    unit = "Lbs"
    print (f"The weight is {round(weight,1)}{unit}")
elif unit == "p":
    weight = weight/ 2.205
    unit = "Kgs"
    print (f"The weight is {round(weight,1)}{unit}")
else:
    print ("Invalid unit")



