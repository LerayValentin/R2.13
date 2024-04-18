print("Calcul d'un prêt immobilier ou d'un crédit à la cosommation.")
montant_pret = float(input("Entrer le montant du prêt ou crédit : "))
taux_annuel_prct = float(input("Entrer le taux annuel en % : "))
nbr_annee = float(input("Entrer le nombre d'années : "))
nbr_mensualite = int(round(nbr_annee) * 12)

##### Fonctions #####

def taux_mens():
    taux_mensuel = taux_annuel_prct / 100 / 12
    return taux_mensuel
def mensualite():
    mensualite = (montant_pret * taux_mens() * (1 + taux_mens())**nbr_mensualite) / ((1 + taux_mens())**nbr_mensualite - 1)
    return mensualite
def interets_cumules():
    interets_cumules = mensualite() * 12 * nbr_annee - montant_pret
    return interets_cumules

def tableau_amortissement():
    print("Tableau d'amortissement : ")
    print("Mois -- Mensualité -- Intérêts -- Capital remboursé -- Capital restant dû -- Intérêts remboursés")
    mois = 0
    interets_rembourses = 0
    capital_restant_du = montant_pret
    for i in range(nbr_mensualite):
        mois += 1
        interet = taux_mens() * capital_restant_du
        capital_rembourse = (mensualite() - interet)
        capital_restant_du -= capital_rembourse
        interets_rembourses += interet
        print(f"  {mois}  --    {round(mensualite(), 1)}   --   {round(interet, 1)}   --       {round(capital_rembourse, 1)}       --       {round(capital_restant_du, 1)}      --        {round(interets_rembourses, 2)}")


##### Affichage #####
print(f"La mensualité avec intérêts est de {round(mensualite(), 2)} eu  ros.")
print(f"Le montant des intérêts remboursés est de {round(interets_cumules(), 2)} euros.")
print(f"Le taux mensuel est de {taux_mens()}")
tableau_amortissement()
