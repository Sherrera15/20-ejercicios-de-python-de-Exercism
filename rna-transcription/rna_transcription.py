def to_rna(dna_strand):
    stri = ""
    
    for letter in dna_strand:
        if letter == 'G':
            stri = stri + "C"
        if letter == "C":
            stri = stri + "G"
        if letter == "T":
            stri = stri + "A"
        if letter == "A":
            stri = stri + "U"
        
    return stri 
