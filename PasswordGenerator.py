"""
Import libraries needed to create a random string
Random: To use random.choice()
String: To use string.ascii_letters, string.digits, string.punctuation
string.ascii_letters :::: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits :::: 0123456789
string.punctuation :::: !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~

"""
import random
import string

#Create a function to which specifies the number of letters, digits and special characters as inputs

def random_password_generator(letters, digits, special_char):
    password_string = ''.join((random.choice(string.ascii_letters) for i in range(letters)))
    password_string += ''.join((random.choice(string.digits) for i in range(digits)))
    password_string += ''.join((random.choice(string.punctuation) for i in range(special_char)))

    # Convert string to a list of letters and digits to use random.shuffle()
    password_list = list(password_string)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    return final_password

# Creating a password with 4 letters, 3 numbers and 1 special character
print("Your strong password is:", random_password_generator(4, 3, 1))

