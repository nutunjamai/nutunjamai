secret_number = 14
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number from - to 20: '))
print('Perfect! You have guessed the secret number.')