grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

grades['Anne'] = 'A'
grades.update({'John': 'A'})
print(grades)