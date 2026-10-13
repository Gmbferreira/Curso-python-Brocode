item = input ("What item would you like to buy: ")
price = float(input("What is its price: "))
quantity = int(input(f"How many {item}(s) would you like to buy?: "))

total = price*quantity

print (f"the total is ${total}")