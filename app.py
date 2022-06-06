import random # built in with python

print("--------------------------------------")
print("This is your new Password Generator")
print("-------------------------------------")
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

number = input("How many password do you want to generate? ")
number = int(number)

length= input("Your password length: ")
length = int(length)

print("\n Here are your required passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars) # random char generation from the chars string
    print(passwords)