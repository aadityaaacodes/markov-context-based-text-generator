# filter prompt sentence (rem spl chars)
def filter_prompt(txt):
    s = ""
    for i in txt:
        if (65 <= ord(i) <= 90):
            s+=chr(ord(i) + 32)
        elif (97 <= ord(i) <= 122) or (ord(i)==32):
            s+=i
        else:
            continue
    return(s)

# function to make words array
def append_unique(txt):
    return(txt.split(' '))

# function to tokenise words and count occurences
def tokenise(arr):
    tokens = {}
    for i in arr:
        if i in tokens:
            tokens.update({f'{i}':(tokens[i]+1)})
        else:
            tokens.update({f'{i}':1})
    return(tokens)


# function to count probablity
def markov_chain(words):
    mat = {}
    # assigning rows:
    for i in range(len(words)):
        if i < len(words)-1:
            if not words[i] in mat:
                mat.update({f'{words[i]}' : None})
            else:
                continue
    # assigning cols
    for i in range(len(words)):
        if i < len(words) - 1:
            mat.update({f'{words[i]}' : {f'{words[i+1]}' : None}})
        else:
            continue
    # adding cell values
    for i in range(len(words)):
        if i < len(words) - 1:
            if mat[words[i]][words[i+1]] is None:
                mat.update({f'{words[i]}' : {f'{words[i+1]}' : 1}})
            else:
                mat.update({f'{words[i]}' : {f'{words[i+1]}' : (mat[words[i]][words[i+1]] + 1)}})
    
    print(mat)

# function to count probability

# function for matrix multiplication

# function for genrating text



t = '''
Bro was just walking sideways down the hallway humming the SpongeBob theme song while juggling three flaming croissants and yelling "I am the CEO of broken printers!" Meanwhile, a raccoon in sunglasses was giving him financial advice about investing in moon cheese, and every time he blinked, the floor turned into spaghetti. Nobody questioned it, not even the inflatable duck that kept screaming about taxes in Latin. Tuesdays, am I right?
'''
count = 0
while t[0] == ' ':
        count+=1

# print(t[count:len(t)])
print(t[(count+1):len(t)])
# sentence = (append_unique(txt=(" "+t+" ")))
# print(sentence)


# words = append_unique(txt=filter_prompt(txt=t))
# tokens = tokenise(arr=words)
# markov_chain(words=words)
# print(tokens)