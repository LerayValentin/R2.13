n = 24

u = 500
montant_cotis = 0
for i in range(n):
    u = u * 0.95 + 30
    montant_cotis += u * 10
print(u)
print(montant_cotis)