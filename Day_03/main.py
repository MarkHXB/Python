""""
Logical operators
"""
print('''        888             888                                          888      
        888             888                                          888      
        888             888                                          888      
88888b. 88888b.  .d88b. 888888 .d88b.  .d88b. 888d888 8888b. 88888b. 88888b.  
888 "88b888 "88bd88""88b888   d88""88bd88P"88b888P"      "88b888 "88b888 "88b 
888  888888  888888  888888   888  888888  888888    .d888888888  888888  888 
888 d88P888  888Y88..88PY88b. Y88..88PY88b 888888    888  888888 d88P888  888 
88888P" 888  888 "Y88P"  "Y888 "Y88P"  "Y88888888    "Y88888888888P" 888  888 
888                                        888               888              
888                                   Y8b d88P               888              
888                                    "Y88P"                888
''')
amount = 0

height = int(input("Enter your height here in cm: "))
if height < 120:
    print("Can't ride")
else:
    age = int(input("Enter your age please: "))
    if age < 12:
        amount +=5
    elif age >= 12 and age <= 18:
        amount += 7
    else:
        amount += 12
    photo = input("Do you want photo( Y if yes ; N if no ) : ")
    if photo.find("y") or photo.find("Y"):
        amount += 3

print(f"The total bill ${amount}")
