x_0548 = int(input("Please enter a number: "))

if type(x_0548) is int:
    if 999>=x_0548>99:
        for i in range(2,x_0548):
            if x_0548%i==0:
                print(x_0548, "is not a prime number")
            else:
                print(x_0548, "is a prime number")
            break
    else:
        print("Please enter a 3 digit integer number")
else:
    print("Please enter an integer number")
