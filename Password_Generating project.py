import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Easy method(In the ordered manner)
'''password=''
for char in range(1,nr_letters+1):
    random_letters=random.choice(letters)
    password+=random_letters
for symb in range(1,nr_symbols+1):
    random_symbols=random.choice(symbols)
    password+=random_symbols
for num in range(1,nr_numbers+1):
    random_numbers=random.choice(numbers)
    password+=random_numbers
print(password)
'''
#Difficult Method (In the unordered way)
password=[]
for char in range(1,nr_letters+1):
    random_letters=random.choice(letters)
    password.append(random_letters)
for symb in range(1,nr_symbols+1):
    random_symbols=random.choice(symbols)
    password.append(random_symbols)
for num in range(1,nr_numbers+1):
    random_numbers=random.choice(numbers)
    password.append(random_numbers)
print(password)
random.shuffle(password)
print(password)
gen_pass=''
for  i in password:
   gen_pass+=i
print(f'Suggested Password is: {gen_pass}')