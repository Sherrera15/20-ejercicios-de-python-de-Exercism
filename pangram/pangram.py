def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for word in alphabet:
        if word not in sentence.lower():
            return False
    return True
