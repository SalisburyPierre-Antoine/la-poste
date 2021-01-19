# Ouverture du fichier prenoms.txt
f = open('input/prenoms.txt', 'r')

#liste_prenoms=[]

for line in f:
    print(line)
    # liste_prenoms.append(line.strip()) #la fonction .strip() permet de retirer le '\n' dans la liste 


# print(liste_prenoms)

# Fermeture du fichier prenoms.txt
f.close()
