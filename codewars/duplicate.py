word = 'Success'

def duplicate_encode(word):
    new_dict = {}
    encode = ''
    to_lower = word.lower()
    
    for char in to_lower:
        if char in new_dict:
            new_dict[char] += 1
        else:
            new_dict[char] = 1
            
    for w in to_lower:
        if new_dict[w] == 1:
            encode += '('
        else:
            encode += ")"

    return encode
            
print(duplicate_encode(word))