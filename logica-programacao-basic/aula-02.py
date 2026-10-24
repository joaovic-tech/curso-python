"""
output:
nome: João | data de nascimento: 22-01-2004
nome: Antonio | data de nascimento: 21-10-2006
"""
SEP = "-"
userA = "João"
userB = "Antonio"

print("nome:", userA, end=" | ")
print("data de nascimento: ", end="")
print(22, "01", 2004, sep=SEP)
print("nome:", userB, end=" | ")
print("data de nascimento: ", end="")
print(21, 10, 2006, sep=SEP)