A = float(input("Veillez saisir la valeur de A : "))
op = (input("Veiller saisir l'operateur :"))
B = float(input("Veillez saisir la valeur de B : "))
if op == "+" :
    print("A + B = ", A+B )
elif op == "-" :
    print("A - B = ", A-B )
elif op == "/" :
    if B != 0 :
        print("A / B = ", A/B)
    else :
        print("Impossible")
elif op == "*" :
    print("A * B = ", A*B )
else:
    print("L'operateur est incorrect")
