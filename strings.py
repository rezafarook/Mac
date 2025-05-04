names = ['Joe', 'Jessica', 'Martin', 'Clive']

for name in names:
    print(name)

new_list = list()

for name in names:
    new_list.insert(0, name)
print(names)
print(new_list)

name_entered = input("Enter Name: ")

if len(name_entered) < 3:
    print("Name Should Greater than 3 Characters !")
elif len(name_entered) >50:
    print("Name cant be more than 50 characters")
else:
    print("Perfect")



secret_number = 7


index = 0

while index < 3:
    guess = int(input("Enter Number: "))
    if (guess == secret_number):
        print("You guessed correctly !")
        break
    index += 1
else:
    print("You did not guess correctly !")