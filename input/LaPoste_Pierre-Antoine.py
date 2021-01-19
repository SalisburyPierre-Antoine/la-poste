#Question 1

#Modes d'ouverture : r (lecture seule)
                   # w (écriture avec remplacement)
                   # a (écriture avec ajout en fin de fichier)
                   # x (lecture et ecriture)
                   # r+ (lecture/écriture dans un même fichier)

f = open(r"/Users/p-asalisbury/Desktop/LaPoste/input/connexion.log","r")
ut = open (r"/Users/p-asalisbury/Desktop/LaPoste/input/utilisateur.txt","w")
for line in f:
    liste_prenoms= line.split(";")
    print (liste_prenoms[1])    
    ut.write (line.split(";")[1] +"\n")

f.close()
if f.closed:
    print("Fichier fermé")
else : 
    print("Fichier encore ouvert")    

#Question 2

f = open(r"/Users/p-asalisbury/Desktop/LaPoste/input/connexion.log","r")

for line in f:
    heure = line.split(" ") [1]
    # print(heure)
    sIP=line.split(";")[0]
    sID=line.split(";")[1]
    if heure<"08:00" or heure>"19:01":
        print(sIP,sID)
        break

f.close()    

#Question 3

f2 = open (r"/Users/p-asalisbury/Desktop/LaPoste/input/warning.txt","r")
f = open("/Users/p-asalisbury/Desktop/LaPoste/input/connexion.log","r")

list_warning = []

suspects = open ("/Users/p-asalisbury/Desktop/LaPoste/input/suspects.txt","w")
for line in f2:
    list_warning.append(line)
    
danger = [ x.replace('\n', '') for x in list_warning]
print(danger)
    
f= open("/Users/p-asalisbury/Desktop/LaPoste/input/connexion.log","r")

list_warningS=[]
for line in f:
    parti=line.split(";") 
    ip=parti[0]

    for ip_s in danger:
        if ip==ip_s:
           list_warningS.append(parti[1])
        else:
            pass
print(list_warningS)

for s in set(list_warningS):
    times=list_warningS.count(s)
    suspects.write("{},{}\n".format(s,times))

    print("{},{}".format(s,times))
suspects.close()
