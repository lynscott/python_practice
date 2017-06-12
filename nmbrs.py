nmbs=["1","4","5","3","8","21","0"]


while True:
    print("Pick a number")
    n=input()
    if n in nmbs:
        print("Correct!")
    else:
        print("Nope! Try again!")


    print("Type q to quit")
    a=input()
    if a=="q":
        break

