def output_roster():
    print('ROSTER')
    for player, rating in roster.items():
        print('Jersey number: %d, Rating: %d' % (player, rating)) 

def add_player():
    player = int(input('Enter a new player\'s jersey number:'))
    rating = int(input('Enter the player\'s rating:'))
    roster[player] = rating

def delete_player():
    player = int(input('Enter a jersey number:'))
    del roster[player]

def update_rating():
    player = int(input('Enter a jersey number:'))
    rating = int(input('Enter a new rating for player:'))
    roster[player] = rating

def players_above():
    baseline = int(input('Enter a rating:'))
    print('\nABOVE', baseline)
    for player, rating in roster.items():
        if rating > baseline:
            print('Jersey number: %d, Rating: %d' % (player, rating))
            
i = 1
roster = {}

while i <= 5:
    player = int(input('Enter player %d\'s jersey number:\n' % i))
    rating = int(input('Enter player %d\'s rating:\n' % i))
    print('')
    roster[player] = rating
    i += 1

output_roster()

while True:
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')

    choice = input('\nChoose an option:')
    if choice == 'a':
        add_player()
    elif choice == 'd':
        delete_player()
    elif choice == 'u':
        update_rating()
    elif choice == 'r':
        players_above()
    elif choice == 'o':
        output_roster()
    elif choice == 'q':
        break      
        
        
        

