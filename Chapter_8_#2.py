def print_classlist():
    alphabetical = sorted(classlist)
    print('\nClasslist')
    for i in alphabetical:
        print(i)
    print('')
num = int(input('Enter the number of students in the class: \n'))
classlist = []
for i in range(num):
    student = input('Enter student %d\'s name: \n' % (i+1))
    classlist.append(student)
print_classlist()
while True:
    more = input('Would you like to enter any more students? (yes or no)\n')
    if more == 'no':
        break
    classlist.append(input('Enter a student\'s name: \n'))
print_classlist()
while True:
    less = input('Would you like to remove any students? (yes or no)\n')
    if less == 'no':
        break
    classlist.remove(input('Enter the student whom you wish to remove from the class: '))
print_classlist()
