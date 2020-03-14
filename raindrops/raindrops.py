def convert(num):
    raind = ""
    
    if (num % 3 == 0):
        raind = raind + "Pling"
    
    if  (num % 5 == 0):
        raind = raind + "Plang"
    
    if  (num % 7 == 0):
        raind = raind + "Plong"
    
    
    if (raind == ""):
        return str(num)
    else:
        return raind