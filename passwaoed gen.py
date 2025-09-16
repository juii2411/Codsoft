import random
char=" abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Length=int(input("Enter length"))
password=" "
for a in range (Length):
    password +=random.choice(char)
print("Password:",password)    
