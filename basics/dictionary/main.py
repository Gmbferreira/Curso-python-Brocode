#Ordered and changeable, but no duplicates

capitals = {"USA": "Washington, D.C.", 
            "France": "Paris", 
            "Japan": "Tokyo", 
            "India": "New Delhi", 
            "Brazil": "Brasília"}

#print(capitals.get("USA"))


#if capitals.get("France"):
#    print("The capital of France is", capitals.get("France"))
#else:
#    print("That capital does not exist.")

#capitals.update({"Germany": "Berlin"})

#capitals.update({"USA": "Detroit"})
#capitals.pop("Japan")
#capitals.popitem() # removes last item in the dictionary
#capitals.clear()

keys = capitals.keys()

#for key in capitals.keys():
#    print(key)

values = capitals.values()

#for value in capitals.values():
#    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")