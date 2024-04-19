"""

print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an.")
placement_d = float(input("Entrer le placement de départ : "))
versement_mens = float(input("Entrer le montant du versement mensuel : "))
taux_ann = float(input("Entrer le taux annuel en % : "))
nbr_ann = int(input("Entrer le nombre d'années : "))
capital_avec_interets = placement_d
total_interets = 0
capital_sans_interets = placement_d + versement_mens * 12 * nbr_ann
##### Calculs #####
for i in range(nbr_ann):
    capital_avec_interets += (versement_mens * 12)
    interets = capital_avec_interets * (taux_ann / 100)
    capital_avec_interets += interets
    total_interets += interets

##### Affichage #####
print(f"Le capital acquis avec intérêts est de {round(capital_avec_interets, 2)} euros au bout de {nbr_ann} ans avec des versements mensuels de {round(versement_mens, 2)} euros.")
print(f"Le intérêts gagnés au taux annuel de {taux_ann} % sont de {round(total_interets, 2)} euros.")
print(f"Sans placement avec intérêts, le capital acquis serait de {capital_sans_interets} euros.")

"""

def c(n):
    if n == 0:
        return placement_d
    else:
        return (c(n-1) + 12 * versement_mens) * (1 + taux_ann / 100)


print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an.")
placement_d = float(input("Entrer le placement de départ : "))
versement_mens = float(input("Entrer le montant du versement mensuel : "))
taux_ann = float(input("Entrer le taux annuel en % : "))
nbr_ann = int(input("Entrer le nombre d'années : "))
print(round(c(nbr_ann), 2))