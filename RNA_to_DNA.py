file_path = r'C:\Users\Abrap\Desktop\Python project 1\src\test_package\rosalind_rna.txt'
with open(file_path, "r", encoding="utf-8") as f:
    dna = f.read()
    rna = dna.replace('T','U')
    print(rna)