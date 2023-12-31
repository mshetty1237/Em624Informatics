import re

print("\n Code run by Mohit Shetty" )

# While loop initiation
while True:
    print("Enter a password meeting the following requirements-")
    print("- Minimum length: 5")
    print("- Maximum length: 12")
    print("- Any combination of numerical and alphabetical characters (either small or capital letters)")
# input password
    pwd = input("\nEnter a password with the above given characteristics, if you are finished just type done:")
# If input is done then output "goodbye!"
    if pwd == 'done':
        print("goodbye!")
        break
# length should be more than 5 to satisfy the condition .
    elif len(pwd) < 5:
        print("This error has occurred because your password is below the required minimum length ")
# length should be less than 12 to satisfy the condition .
    elif len(pwd) > 12:
        print("This error has occurred because your password is more than the required maximum length")
# if special character is entered then it will prompt "This error has occurred because it has non alphabetical and non numerical characters"
    elif not (bool(re.match('^[a-zA-Z0-9]+$',pwd)) == True):
        print("This error has occurred because it has non alphabetical and non numerical characters")
#  checks whether the password has number or not
    elif not any(i.isdigit() for i in pwd):
         print("This error has occurred because your password has no numerical character")
#  checks whether the password has alphabets or not
    elif not any(i.isalpha() for i in pwd):
        print("This error has occurred because your password has no alphabetic character")
# if all the conditions are satisfied program prompts the response "Password accepted"
    else:
        print("Password accepted!")


