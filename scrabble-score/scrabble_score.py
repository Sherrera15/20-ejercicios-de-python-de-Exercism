def score(word):
    
    points = 0
    letter = word.upper()
    
    for words in letter:
        if words in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
            points = points + 1
        elif words in ["D", "G"]:
            points = points + 2
        elif words in ["B", "C", "M", "P"]:
            points = points + 3
        elif words in ["F", "H", "V", "W", "Y"]:
            points = points + 4
        elif words in ["K"]:
            points = points + 5
        elif words in ["J", "X"]:
            points = points + 8
        elif words in ["Q", "Z"]:
            points = points + 10
    return points