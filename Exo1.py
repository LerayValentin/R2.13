print("Calcul d'un prêt immobilier ou d'un crédit à la cosommation.")
montant_pret = float(input("Entrer le montant du prêt ou crédit : "))
taux_annuel_prct = float(input("Entrer le taux annuel en % : "))
nbr_annee = float(input("Entrer le nombre d'années : "))


def taux_ann(taux_annuel_prct):
    taux_annuel = 1 + (taux_annuel_prct / 100)
    return taux_annuel

def taux_mens(taux_annuel, nbr_annee):
    taux_mensuel = (1 + taux_annuel)**(1/(12*nbr_annee)) - 1
    return f"Le taux mensuel est de {taux_mensuel}."
def mensualite(montant_pret, taux_annuel_prct, nbr_annee):

    mensualite = (montant_pret * (taux_ann()))

    return f"La mensualité avec intérêts est de {mensualite} euros."

print(mensualite(montant_pret, taux_annuel_prct, nbr_annee))
print(taux_mens(taux_ann(taux_annuel_prct), nbr_annee))
print(taux_ann(taux_annuel_prct))

