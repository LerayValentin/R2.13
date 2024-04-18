print("Calcul d'un prêt immobilier ou d'un crédit à la cosommation.")
montant_pret = float(input("Entrer le montant du prêt ou crédit : "))
taux_annuel_prct = float(input("Entrer le taux annuel en % : "))
nbr_annee = float(input("Entrer le nombre d'années : "))
nbr_mensualite = nbr_annee * 12

def taux_ann(taux_annuel_prct):
    taux_annuel = (taux_annuel_prct / 100)
    return taux_annuel

def taux_mens():
    taux_mensuel = taux_ann(taux_annuel_prct) / 12
    return taux_mensuel
def mensualite(montant_pret, taux_annuel):
    mensualite = (montant_pret * taux_annuel * (1 + taux_annuel)**nbr_mensualite) / ((1 + taux_annuel)**nbr_mensualite - 1)
    return f"La mensualité avec intérêts est de {mensualite} euros."

def interets():
    

print(mensualite(montant_pret, taux_mens()))
print(f"Le taux mensuel est de {taux_mens()}")
#print(taux_ann(taux_annuel_prct))

