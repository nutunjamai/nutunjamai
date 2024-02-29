print('Hello World')
length = len('hello')
print(length)
number = input('What is the number?')
print_return = print('Hello World!')
print(print_return)

x = None

if x:
    print('None is True')
elif x is False:
    print('None is False')
else:
    print('None is not True, or Fales, None is just None')
    
    
x = None
if x is None:
    print('yes')
if x == None:
    print('it does')
    
def greet():
    print('hello!')
    
x = greet()
print(x)