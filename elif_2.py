user_age = int(input('What is your age?: '))
user_country = input('What is your country? ')

if user_age <25 and user_country == 'Germany':
    print('You can apply for a german student exchange programme')
else:
    print('Sorry, you do not qualify')
    
if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange programme')
else:
    print('Sorry, you do not qualify')