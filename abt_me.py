my_favs={"height":"6'3","color":"olive","food":"donuts"}

q=input("Whats do you want to know about me?")
if q in my_favs:
	facts=my_favs[q]
	print(facts)
else:
        print("Not Found.")
