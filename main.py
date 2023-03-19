#Password Generator Project
import random
# list of letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# list of numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# list of symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# random letters
password =[]
for num_let in range(0, nr_letters):
  num_let = letters[random.randint(0, len(letters) - 1)]
  password.append(num_let)

# random symbols
for num_sym in range(0, nr_symbols):
  num_sym = symbols[random.randint(0, len(symbols) - 1)]
  password.append(num_sym)

# random number
for num_num in range(0, nr_numbers):
  num_num = numbers[random.randint(0, len(numbers) - 1)]
  password.append(num_num)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password1 = "".join(password)
# print(f"This is your generated password: {password1}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pass = len(password)
for hard in range(0, hard_pass):
  hard = str(password[random.randint(0, len(password) - 1)])
  password.remove(hard)
  password.append(hard)

password2 = "".join(password)
print(f"This is your generated password: {password2}")
