first = input("Enter first number: ")
second = input('Enter second number: ')
print('Before swapping:', first, second)
first = second
second = first
print('Before swapping:', first, second)


first = input("Enter first number: ")
second = input('Enter second number: ')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('Before swapping:', first, second)


first = input("Enter first number: ")
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('Before swapping:', first, second)

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort(reverse=True)
print(top_cities)

top_cities = ['New York City', 'Los Angeles', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)