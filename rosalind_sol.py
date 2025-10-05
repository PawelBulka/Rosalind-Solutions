file_path = r'C:\Users\Abrap\Desktop\Python project 1\src\test_package\rosalind_dna.txt'
with open(file_path, "r", encoding="utf-8") as f:
    dna = f.read()

print(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))
