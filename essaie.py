x = (input('entrez les heures:'))
t = float(x)
y = (input('entrez le taux:'))
n = float(y)
if t <= 40:
    print(t * n)
elif t > 40:
    print(40* n + (t-40)*1.5*n)