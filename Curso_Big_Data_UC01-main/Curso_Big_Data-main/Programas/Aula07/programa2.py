temperaturas = []
resp = "s"

while resp == "s" or resp == "S":
    temperaturas.append(float(input("Digite a temperatura: ")))
    resp = input("Deseja continuar? ")
print(f"A media de temperaturas é {(sum(temperaturas)/len(temperaturas)):.1f}")
print(f"A maior temperatura é {max(temperaturas)}")
print(f"A menor temperatura é {min(temperaturas)}")