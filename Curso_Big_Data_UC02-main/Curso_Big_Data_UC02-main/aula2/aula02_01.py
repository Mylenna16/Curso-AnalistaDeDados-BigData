# Usando código usando listas

media = [80,90,10,40,20,40,50,90,20,50]
ap = []
rep = []

for i in range(len(media)):
    if media[i] >= 70:
        ap.append(media[i])
    else:
        rep.append(media[i])

print(ap)
print(rep)