import random
import string

def passwordElements(length): #* This was created by Ramy Mohammed

    # defines the elements need for the password, which includes case-sensitive letters, numbers, and symbols.
    lowercaseLetters = string.ascii_lowercase # all the lowercase letters in the alphabet
    uppercaseLetters = string.ascii_uppercase # all the uppercase letters in the alphabet
    numbers = string.digits # all the numbers from 0-9
    symbols = string.punctuation # symbols such as !@#$%^&*()-=+,.<>/?;:'"[{}]\|`~

    # In order to create the password we must combine all of the elements together.
    all = lowercaseLetters + uppercaseLetters + numbers + symbols

    # randomly jumbles together the elements all together
    combined = random.sample(all, length)

    # joins the entire password together and presents it to the user
    password = ''.join(combined)
    return password

def creating_the_password():
    print('\nHello user! Welcome to the Password Generator. Follow the steps below to generate a secure password. ')
    length = range(5, 16)
    length = int(input('\nEnter the length of the password (5 - 16) you would like: \n')) # takes input from the user for password length

    while ((length < 5 or length > 16) and (length != (range(5, 16))) and (length != int)):
        print("Sorry, you must pick the length between 5 to 16.")
        length = int(input('\nEnter the length of the password (5 - 16) you would like: \n'))
    password = passwordElements(length)

    answer1 = input('\nWhat is this password for? Just for your records. ') # takes the input for the use of this password, if it's for a site or app

    print('\nGreat! Here you go: ')
    print(password) # presents the password to the user

    passwordStorage(password, answer1)

def passwordStorage(password, answer1):
    answer2 = input('\nDo you like this password? Yes or No? ') # does the user like this password?
    if (answer2 == 'Yes' or answer2 == 'yes'):
        passwordStorage = open('Password Storage.txt', 'a') # Creates the folder for the password storage
        
        passwordStorage.write('Password: ' + password + ' <- ' + answer1 + '\n') # if they like it it will output the password into 
        passwordStorage.close()
        
        print('\nThere you go! ')
        print('Check Password Storage.txt in the same directory to view the newly created password. Keep it safe! ')
        return None
    elif (answer2 == 'No' or answer2 == 'no'):
        userResponse()

def userResponse():
    answer3 = input('Do you want to create another password? Yes or No? ') # If user doesn't like the password, they can generate a new password.
    if answer3 == 'Yes' or answer3 == 'yes':
        creating_the_password()
    elif answer3 == 'No' or answer3 == 'no':
        print('Well, we tried. Sorry. Come back again! ') 
        return None

creating_the_password()
