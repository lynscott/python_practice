ans=list()

car=input("What's your dream car?")
with open("car.txt","w") as f:
    f.write(car)
    

print("Duly noted! Thank you!")
