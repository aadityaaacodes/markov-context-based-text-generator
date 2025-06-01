import json

mFile = 'json/map.json'
pFile = 'json/prob.json'
tFile = 'json/total.json'



def filter_text(txt):
    """ 
    Remove special characters and extra spaces 
    """
    txt = txt.strip()
    s = ""
    for i in txt:
        if (65 <= ord(i) <= 90):
            s+=chr(ord(i) + 32)
        elif (97 <= ord(i) <= 122) or (ord(i)==32):
            s+=i
        else:
            continue
    return(s)


def array_maker(arr):
    """Makes an array with all unique triad words"""
    return [' '.join(arr[i:i+3]) for i in range(0, len(arr), 3)]
    # return [arr[i:i+3] for i in range(0, len(arr), 3)]


def array_spiltter(txt):
    return(txt.split(' '))


def filter_array(arr, red_list):
    return [item for item in arr if item not in red_list]
    # return [item for item in arr if item in red_list]


def count_occurences(arr):
    """Count occurences for each token"""
    map = {}
    for i in range(0, (len(arr)-1)):
        j = i + 1
        if arr[i] in map:
            map[arr[i]] = map[arr[i]] + 1
        else:
            map[arr[i]] = 1
    return(map)


def tokeniser(arr):
    """Makes a map for the outcomes for each token
    Call only when updating map.json"""

    with open(mFile, "r") as f:
        map = json.load(f)
    
    # setup
    for i in range(0,len(arr)):
        if str(arr[i]) not in map.keys():
            map[arr[i]] = {}

    with open(mFile, "w") as f:
        json.dump(map, f, indent=4)
    
    for k in range(0,(len(arr)-1)):
        i = arr[k]
        j = arr[k+1]
        if j in map[i].keys():
            map[i][j] = map[i][j] + 1
        else:
            map[i][j] = 1

    with open(mFile, "w") as json_file:
        json.dump(map, json_file, indent=4)

    # return(map)


def totaller():
    """Makes a map to find the total outcomes for each token"""
    with open(mFile, "r") as f:
        n_step = json.load(f)
    
    total_map = {}
    total = 0
    for i in n_step.keys():
        for j in (n_step[i].keys()):
            total += n_step[i][j]
        total_map.update({i:total})
        total = 0
    
    with open(tFile, "w") as json_file:
        json.dump(total_map, json_file, indent=4)
    # return(total_map)


def restartMap():
    '''Used to empty .json files'''
    newMap = {}
    for i in [mFile, pFile, tFile]:
        with open(i, "w") as f:
            json.dump(newMap, f, indent=4)
    # with open(pFile, "w") as f:
    #     json.dump(newMap, f, indent=4)
    # with open(pFile, "w") as f:
    #     json.dump(newMap, f, indent=4)


def processFeed(feed):
    with open(feed, 'r') as file:
        unfiltered_text = file.read()
    return(unfiltered_text)

# unfiltered_text = '''
# Under a sky streaked with shades of lavender and gold, a small fox darted through the tall grass, its ears twitching at every rustle. The wind carried the scent of pine and wildflowers, and somewhere in the distance, a creek bubbled over smooth stones. A worn leather satchel lay forgotten near an ancient oak, its contents spilling slightly—an old map, a compass, and a journal filled with sketches of strange symbols. The forest seemed to hold its breath, as if waiting for someone to notice the clues hidden in plain sight.
# '''

# print(array_maker(txt=filter_text(txt=unfiltered_text)))
# print(count_occurences(array_maker(txt=filter_text(txt=unfiltered_text))))
# print(tokeniser(array_maker(txt=filter_text(txt=unfiltered_text))))
# print(totaller(n_step=tokeniser(array_maker(txt=filter_text(txt=unfiltered_text)))))

