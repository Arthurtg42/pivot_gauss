from xmlrpc.client import boolean

def echange_ligne(matrice, i, j):
    """échange Li <--> Lj de matrice"""
    copy = matrice[i]
    matrice[i] = matrice[j]
    matrice[j] = copy

def multiplie_ligne(matrice, i, j, coef, col):
    """Li = Li + coef*Lj"""
    if(col == 1):
        matrice[i] = matrice[i] + coef*matrice[j]
    else:
        for k in range(col):
            matrice[i][k] = matrice[i][k] + coef*matrice[j][k]

def indice_pivotmax(matrice, j, ligne):
    """Renvoi l'indice du pivot le plus grand (en valeur absolu) pour des raisons de précision sur le type float"""
    ipiv = j
    for k in range(j+1, ligne):
        if(abs(matrice[k][j]) > abs(matrice[ipiv][j])):
            ipiv = k
    return ipiv

print("Résolution de Ax = b :\n\n NOTE : il faut que la matrice A que vous allez saisir soit inversible, le programme ne le vérifie pas\n\n")
ligne = int(input("Entrez le nombre de ligne : "))
col = int(input("Entre les nombre de colonne : "))

if(ligne==col):
    second_membre = []
    print("Entrer les valeurs du second membre (cliquez sur entrée après chaque valeur saisie): ")
    for i in range(ligne):
        second_membre.append(float(input()))

    chaine = []
    matrice = [[0]*col for i in range(ligne)]
    for i in range(ligne):
        chaine = input("Saisissez les valeurs de la "+str((i+1))+"e ligne de la matrice, séparés par des espaces :\n")
        chaine = chaine.split(" ")
        for j in range(col):
            matrice[i][j] = float(chaine[j])

    for j in range(col-1):
        ipiv = indice_pivotmax(matrice, j, ligne)
        echange_ligne(matrice, j, ipiv)
        echange_ligne(second_membre, j, ipiv)
        for i in range(j+1, ligne):
            coef = matrice[i][j]/matrice[j][j]
            multiplie_ligne(matrice, i, j, -coef, col)
            multiplie_ligne(second_membre, i, j, -coef, 1)

    solutions = [0 for i in range(ligne)]

    solutions[ligne-1] = float(second_membre[ligne-1])/matrice[ligne-1][ligne-1]
    print("x"+str(ligne-1)+" = "+str(solutions[ligne-1])+"\n")
    for i in range(ligne-2, -1, -1):
        s = 0
        for j in range(i+1, col):
            s = s + matrice[i][j]*float(solutions[j])
        solutions[i] = float(second_membre[i]-s)/matrice[i][i]
        print("x"+str(i)+" = "+str(solutions[i])+"\n")
    
else:
    print("Si la matrice n'est pas carrée, je doute qu'elle soit inversible !!!")
