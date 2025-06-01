arr = ['under', 'a', 'sky', 'streaked', 'with', 'shades', 'of', 'lavender', 'and', 'gold', 'a', 'small', 'fox', 'darted', 'through', 'the', 'tall', 'grass', 'its', 'ears', 'twitching', 'at', 'every', 'rustle', 'the', 'wind', 'carried', 'the', 'scent', 'of', 'pine', 'and', 'wildflowers', 'and', 'somewhere', 'in', 'the', 'distance', 'a', 'creek', 'bubbled', 'over', 'smooth', 'stones', 'a', 'worn', 'leather', 'satchel', 'lay', 'forgotten', 'near', 'an', 'ancient', 'oak', 'its', 'contents', 'spilling', 'slightlyan', 'old', 'map', 'a', 'compass', 'and', 'a', 'journal', 'filled', 'with', 'sketches', 'of', 'strange', 'symbols', 'the', 'forest', 'seemed', 'to', 'hold', 'its', 'breath', 'as', 'if', 'waiting', 'for', 'someone', 'to', 'notice', 'the', 'clues', 'hidden', 'in', 'plain', 'sight']

dic = {
    "hello" : {
        "world" : 1,
        "Hamsa" : 3
    }
}

map = {}

# setup
for i in range(0,len(arr)):
    map[arr[i]] = {}


for k in range(0,(len(arr)-1)):
    i = arr[k]
    j = arr[k+1]
    if j in map[i].keys():
        map[i][j] = map[i][j] + 1
    else:
        map[i][j] = 1

print(map)

