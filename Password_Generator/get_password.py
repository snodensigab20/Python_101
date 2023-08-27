import random

print("Welcome to MyPassword Generator!")

num_letters = int(input("How many letters you want in your password?\n"))

num_symbols = int(input("How many symbols you want in your password?\n"))

num_numbers = int(input("How many numbers you want in your password?\n"))


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

numbers = ['1','2', '3','4','5','6','7','8','9','0']


my_password = ''


for lett in range(num_letters):
    select_letter = random.choice(letters)
    my_password = my_password+select_letter

for sym in range(num_symbols):
    select_sym = random.choice(symbols)
    my_password = my_password+select_sym
    
    
for n in range(num_numbers):
    select_numbers = random.choice(numbers)
    my_password = my_password+select_numbers

print(f"Your password is: {my_password}")




