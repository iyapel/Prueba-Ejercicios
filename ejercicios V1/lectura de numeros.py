msg = input("Ingrese un mensaje que sea messi pa pq es campion del mundo joda ")
N = 0

for i in msg:
    if i == ",":
        
        continue
    Na = int(i)
    N = Na + N

print(N)



