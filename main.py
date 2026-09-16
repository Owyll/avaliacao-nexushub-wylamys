startup = {"nome": "NexusHub"}

with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha1 = arquivo.readline()
    linha2 = arquivo.readline()
    linha3 = arquivo.readline()
    linha4 = arquivo.readline()

print(cabecalho, end="")
print(linha1, end="")
print(linha2, end="")
print(linha3, end="")
print(linha4, end="")

custo1 = float(linha1.split(",")[1].strip())
custo2 = float(linha2.split(",")[1].strip())
custo3 = float(linha3.split(",")[1].strip())
custo4 = float(linha4.split(",")[1].strip())
total = custo1 + custo2 + custo3 + custo4

print("\nPainel final")
print(f"Nome da startup: {startup['nome']}")
print("Bancada alocada: Bancada N1")
print(f"Valor total da infraestrutura Cloud: R$ {total:.2f}")