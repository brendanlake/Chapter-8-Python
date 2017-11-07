a = {}
for i in range(1,6):
    j = int(input("Enter player {}'s jersey number:\n".format(i)))
    r = int(input("Enter player {}'s rating:\n\n".format(i)))
    
    if j<0 and j>99 and r<0 and r>9:
        print('Invalid Entry')
        break
    else:
        a[j]=r
print('ROSTER')
for j,r in a.items():
    print('Jersey number: {}, Rating: {}'.format(j,r))

def ini():
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    k = input()
    if k == 'a':
        add()
    elif k =='d':
        rem()
    elif k =='u':
        upd()
    elif k =='r':
        rat()
    elif k =='o':
        show()
    elif k == 'q':
        exit()
    
def add():
    j = int(input("Enter player's jersey number:"))
    r = int(input("Enter player's rating:"))

    if j<0 or j>99 and r<0 and r>9:
        print('Invalid Entry')
    else:
        a[j]=r
    ini()

def rem():
    n = int(input('Enter a jersey number: '))
    if n in a:
        del a[n]
    ini()
def rat():
    n = int(input('Enter a rating: '))

    for j,r in a.items():
        if r>n:
            print(print('Jersey number:{}, Rating:{}'.format(j,r)))
    ini()

def show():
    for j,r in a.items():
        print(print('Jersey number:{}, Rating:{}'.format(j,r)))
    ini()

def upd():
    j = int(input("Enter player's jersey number:"))
    r = int(input("Enter player's rating:"))
    if r<0 and r>9:
        print('Invalid Entry')

    else:
        if j in a:
            a[j]=r
    ini()
ini()
