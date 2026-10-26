"""
Conversão de tipos também chamado de:
- Coerção
- Type Convertion, typecasting, coercion
É o ato de converter um tipo
"""
datas = ["40", 11]
i = 0
print()

datas[0] = int(datas[0])

for data in datas:
    print(type(data))

print("--------------------")

for data in datas:
    print(type(data))

print("--------------------")

datas[1] = str(datas[1])
print(type(datas[1]))

# pode usar também para outros tipo: float(), str("")