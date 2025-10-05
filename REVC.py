
file_path = r'C:\Users\Abrap\Desktop\Python project 1\src\test_package\rosalind_revc.txt'
with open(file_path, "r", encoding="utf-8") as f:
    dna = f.read()
    compl = str.maketrans('ACGT','TGCA')
    print(dna.translate(compl)[::-1])

