def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
        
items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
print(linear_search(items, target))

def final_value_after_operations(operations):
    tigger = 1
    for i in operations:
        if i == 'bouncy' or i == 'flouncy':
            tigger += 1
        elif i == 'trouncy' or i == 'pouncy':
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

def tiggerfy(word):
    word = word.lower()
    for sb in ['t','i','gg','er']:
        word = word.replace(sb,'')
    return word

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))

def non_decreasing(nums):
    count = 0
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            count += 1
            if count > 1:
                return False 
        if i > 0 and nums[i-1] > nums[i+1]:
            nums[i+1] = nums[i]
        else:
            nums[i] = nums[i+1]
    return True

nums = [4, 2, 3]
print(non_decreasing(nums))

nums = [4, 2, 1]
print(non_decreasing(nums))


