x = input('entrez les heures:')
y = input('entrez le taux:')
try:
 heure = flotteur(x)
 taux = flottant(y)
except:
 print('Erreur,Veuillez saisir le chiffre numérique:')
 exit()
if heure<=40 :
 print(heure*taux)
else:
 print((((heure-40)*taux)*1.5)+taux*40)