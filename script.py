def DNA_strand(dna):
    complementary = ""
    for nucleotide in dna:
        if nucleotide == "A":
            complementary += "T"
        elif nucleotide == "T":
            complementary += "A"
        elif nucleotide == "C":
            complementary += "G"
        elif nucleotide == "G":
            complementary += "C"
    return complementary


# Example usage
print(DNA_strand("ATTGC"))  # Output: "TAACG"
print(DNA_strand("GTAT"))  # Output: "CATA"    
