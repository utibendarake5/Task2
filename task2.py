import string
import random


#Function to collect Employee Details
def collect_details():
    first_name = input("Your First Name:  ")
    last_name = input("Your Last Name: ")
    email = input("Your Email: ")
    initials = [first_name, last_name, email]
    return initials


#Function to automatically generate password by slicing the initials list above
def gen_password(initials):
    random_string = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(random_string) for i in range(length))
    password = str(initials[0][0:2] + initials[1][-2:] + random_password)
    return password


status = True
user_data = []

while status:
    initials = collect_details()
    password = gen_password(initials)
    print(f"Your auto-generated password is: {password}")
    password_like = input("Is the generated password ok? Y or N? ").upper()

    unique_password = True
    while unique_password:
        if password_like == "Y":
            initials.append(password)
            user_data.append(initials)
            print(f'Your details are: {initials}')
            break
        else:
            preferred_password = input('Enter password longer than or equal to 7 ')

            while len(preferred_password) < 7:
                print("Your password doesn't meet the required minimum length of 7")
                preferred_password = input("Input your desired password again: ")

            else:
                initials.append(preferred_password)
                user_data.append(initials)
                print(f'Your details are: {initials}')
                break

    #Another Employee prompt
    another_user = input('Is there another new user? Y or N?').upper()
    if another_user == 'N':
        status = False
        for userDetails in user_data:
            print(userDetails)
    else:
        status = True






