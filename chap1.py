## test
def binary_search(list, guess):
    low = 0
    high = len(list) -1
    

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        item = list[mid]
        print(guess," ","this is the item", item)
        if guess == item:
            return mid
        if guess > item:
            low = mid + 1
        else:
            high = mid - 1
    return None

my_list = [2,3,4,5,6,7,8,9,11,13,15,17]

print (binary_search(my_list, 4))
## print (binary_search(my_list, -1))
