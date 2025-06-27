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

def sum_honey(hunny_jars):
    count = 0
    for i in hunny_jars:
        count += i
    return count
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

def doubled(hunny_jars):
    new_list = []
    for i in hunny_jars:
        i *= 2
        new_list.append(i)
    return new_list
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

def count_less_than(race_times, threshold):
    count = 0
    for i in race_times:
        if i < threshold:
            count += 1
    return count
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print ( count_less_than(race_times, threshold) )

race_times = []
threshold = 4
print( count_less_than(race_times, threshold) )

def print_todo_list(task):
    print("Pooh's To Dos:")
    for i in range(len(task)):
        print(f'{i+1}.{task[i]}')

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)

def can_pair(item_quantities):
    for i in item_quantities:
        if i%2 != 0:
            return False
        else:
            return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

def split_haycorns(quantity):
    divisors = []
    for i in range(1, quantity+1):
        if quantity % i == 0:
            divisors.append(i)
    return divisors
    
quantity = 6
print(split_haycorns(quantity))

def tiggerfy(s):
    remove_char = ['t','i','g','e','r']
    result = ''
    for ch in s:
        if ch.lower() not in remove_char:
            result += ch
    return result

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

def locate_thistles(items):
    remove_s = 'thistle'
    result = []
    for i in range(len(items)):
        if items[i] == remove_s:
            result.append(i)
    return result

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))
items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))