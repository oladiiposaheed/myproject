class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18
try:
    age = int(input('How Old are you: '))
    if age < number:
        raise InvalidAgeException
    else:
        print('Eligible to Vote')
except InvalidAgeException:
    print("Exception occurred: Invalid Age")