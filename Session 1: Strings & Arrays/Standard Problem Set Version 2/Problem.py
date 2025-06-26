def welcome():
    print('welcome to the hundred acre world')

welcome()

def greeting(name):
    print('welcome to the hundred acre world '+ name + '! My name is Robin.')

greeting('Grace')

def print_catchphrase(char):
    if char == 'Pooh':
        print('Oh bother!')
    elif char == 'Tigger':
        print('Ta-ta for now!')
    elif char == 'Eeyore':
        print('Thanks for noticing me!')
    elif char == 'Chrtistpoher':
        print('Silly old bear')
    else: 
        return None

print(print_catchphrase('Poola'))

def get_item(items,x):
    if 0 <= x < len(items):
        return items[x]
    return None
    
items = ["piglet", "pooh", "roo", "rabbit"]
x = -2
print(get_item(items,x))

