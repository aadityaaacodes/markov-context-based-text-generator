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

def append_unique(txt):
    return(txt.split(' '))

t = '''
Bro was just walking sideways down the hallway humming the SpongeBob theme song while juggling three flaming croissants and yelling "I am the CEO of broken printers!" Meanwhile, a raccoon in sunglasses was giving him financial advice about investing in moon cheese, and every time he blinked, the floor turned into spaghetti. Nobody questioned it, not even the inflatable duck that kept screaming about taxes in Latin. Tuesdays, am I right?
'''

print(append_unique(txt=filter_prompt(txt=t)))