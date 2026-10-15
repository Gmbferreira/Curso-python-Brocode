fruits = ["apple", "orange", "banana", "coconuts"]
vegetables = ["celery", "carrots","potatoes"]
meats = ["chicken", "fish", "turkey"]

#groceries = [fruits, vegetables, meats]

groceries = [["apple", "orange", "banana", "coconuts"],
            ["celery", "carrots","potatoes"],
            ["chicken", "fish", "turkey"]]

# print (fruits)
# fruits[0] #=apple

#print (groceries[0]) # fruits
#print (groceries[0][0]) # apple
#print (groceries[1][2]) # potatoes

for collection in groceries:
    for item in collection:
        print (item, end=" ")
    print()