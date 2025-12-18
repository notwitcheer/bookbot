

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()
    
def get_word_count(text):
    return len(text.split())

def character_count(text):
    return {
        'a': text.lower().count('a'),
        'b': text.lower().count('b'),
        'c': text.lower().count('c'),
        'd': text.lower().count('d'),
        'e': text.lower().count('e'),
        'f': text.lower().count('f'),
        'g': text.lower().count('g'),
        'h': text.lower().count('h'),
        'i': text.lower().count('i'),
        'j': text.lower().count('j'),
        'k': text.lower().count('k'),
        'l': text.lower().count('l'),
        'm': text.lower().count('m'),
        'n': text.lower().count('n'),    
        'o': text.lower().count('o'),
        'p': text.lower().count('p'),    
        'q': text.lower().count('q'),
        'r': text.lower().count('r'),
        's': text.lower().count('s'),
        't': text.lower().count('t'),
        'u': text.lower().count('u'),
        'v': text.lower().count('v'),
        'w': text.lower().count('w'),
        'x': text.lower().count('x'),
        'y': text.lower().count('y'),
        'z': text.lower().count('z'),
    }

def sort_dict(d):
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}