notas = [
('Alice', [85, 90, 92]),
('Bob', [78, 80, 85]),
('Charlie', [92, 88, 94])
]


dic_notas = {}


for item in notas:
    chave = item[0]
    value = item[1]
    media = sum(value)/len(value)
    dic_notas[chave] = media
    
    
print(dic_notas)

    