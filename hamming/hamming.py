def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError("The strands must be the same length")
        
    return len([i for i, j in zip (strand_a, strand_b) if i != j])
