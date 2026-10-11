print("Jeux de Test")

#Création du dictionnaire des élèves
d = {"Alice": 12.0, "Bob": 15.0, "Claire": 9.5}
print("dictionnaire de base: ",d)

#============fonction ajouter un étudiant=========
def ajouter_etudiant(d, nom, note):#prend en paramètre le dictionnaire :"d",le 'nom' et la "note" de élève à rajouter
    d[nom] = float(note)
    return d


# Ajout de David dans le dictionnaire avec la moyenne de 19
ajouter_etudiant(d, "David", 19)
print("le nouveau dictionnaire avec David: ",d)


#============fonction calcule de la moyenne des étudiants=========
def moyenne_classe(d):
    moyenne = sum(d.values()) / len(d) #".sum" calcule la somme des éléments de d et "len" qui détermine le nombre de valeurs de "d"
    return moyenne

print("affichage de la moyenne de classe: ",moyenne_classe(d))


#============fonction qui définit le meilleu étudiant=========
def meilleur_etudiant(d):
    meilleur_nom = "" #on définit un nouveau paramètre comme étant vide pour déterminer le meilleur à son "nom"
    meilleure_note = 0 #on définit un nouveau paramètre comme étant nulle pour déterminer le meilleur à sa "note"
    for nom, note in d.items(): #on parcours le nombres d'élèves qui est présent dans le dictionnaire
        if note > meilleure_note: # condition qui permet de déterminer la meilleur note via la boucle précedante
            meilleur_nom = nom #la nouvelle valeur de nom est la valeur qui à validé la condition
            meilleure_note = note #la nouvelle valeur de note est la valeur qui à validé la condition
    return meilleur_nom, meilleure_note


print("le meilleur est: ",meilleur_etudiant(d))


#============fonction qui permet de sauvegarder le fichier avec le nom et les notes des élèves=========
def sauvegarder(d, fichier):
    with open(fichier, "w") as f:# "w" permet d'écrire
        for nom, note in d.items(): #boucle qui définit combien de fois il doit écrire en fonction du nombre des élèves
            f.write(nom + ":" + str(note) + "\n") #écrit le nom de l'étudiont, sa note est forcé au format text et fait un saut de ligne


#============Recharge le dictionnaire depuis un fichier texte=========
def recharger(fichier):
    d = {}

    with open(fichier, "r") as f: # "r" permet de lire le fichier
        for ligne in f: #boucle en fonction du nombre de lignes
            ligne = ligne.strip()# ".strip()" supprime les espaces inutiles

            nom, note = ligne.split(":", 1) #.split(":", 1) sépare la ligne en deux parties

            d[nom] = float(note)#Conversion de la note, qui est actuellement du texte en nb décimale

    return d


# Sauvegarde le fichier du dictionnaire en "etudiants.txt"
sauvegarder(d, "etudiants.txt")

# Rechargement du fichier "etudiant.txt"
d2 = recharger("etudiants.txt")

print("Dictionnaire rechargé :")#afficahge du fichier
print(d2)