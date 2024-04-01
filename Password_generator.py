import random
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

number = ['0','1','2','3','4','5','6','7','8','9']

symbol = ['!','@','#','$','%','&','*','~','(',')','?']

print("Welcome to Password Generator : ")
n_letter = int(input("How many Letters you want \n "))
n_number = int(input("How many Nummber you want \n "))
n_symbol= int(input("How many Symbol you want  \n "))
password_list = []

for i in range (1,n_letter+1):
    char=random.choice(letters)
    password_list += char


for i in range (1,n_number+1):
    char=random.choice(number)
    password_list += char
for i in range (1,n_symbol+1):
    char=random.choice(symbol)
    password_list += char
    
random.shuffle(password_list)

password = ""

for char in password_list:
    password += char
print(password)