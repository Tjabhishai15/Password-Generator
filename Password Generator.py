import random
print("Welcome to the Password Generator!")
print("Please enter the length of the password you would like (minimum 8 characters):")

password_length = int(input())
if password_length < 8:
    print("Password length must be at least 8 characters.")
    quit()

print("Would you like to include uppercase letters? (y/n)")
include_uppercase = input().lower() == "y"

print("Would you like to include lowercase letters? (y/n)")
include_lowercase = input().lower() == "y"

print("Would you like to include numbers? (y/n)")
include_numbers = input().lower() == "y"

print("Would you like to include special characters? (y/n)")
include_special = input().lower() == "y"

possible_characters = ""
if include_uppercase:
    possible_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if include_lowercase:
    possible_characters += "abcdefghijklmnopqrstuvwxyz"
if include_numbers:
    possible_characters += "0123456789"
if include_special:
    possible_characters += "!@#$%^&*()_+-=[]{}|;':\",./<>?"

if not possible_characters:
    print("You must select at least one type of character to include.")
    quit()

password = "".join(random.sample(possible_characters, password_length))
print("Your password is: " + password)