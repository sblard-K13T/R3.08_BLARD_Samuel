import random #permet de choisir un élément au hasard dans une liste

print("Jeu du Pendu")

#Liste de mots utilisée pour le jeu
mots = ["python", "ordinateur", "clavier", "reseau", "serveur", "programme"]


#============fonction qui choisit un mot au hasard=========
def choisir_mot(liste): #prend en paramètre la liste de mots
    mot = random.choice(liste) #"random.choice" renvoie un élément de la liste au hasard
    return mot.upper() #".upper()" met le mot en MAJUSCULES


#============fonction qui construit le masque du mot=========
def masque(mot): #prend en paramètre le mot à cacher
    return ["_"] * len(mot) #crée une liste de "_" de la même longueur que le mot


#============Paramètres du jeu=========
mot = choisir_mot(mots) #le mot à deviner
mot_masque = masque(mot) #le mot caché sous forme de "_"
erreurs = 0 #compteur d'erreurs
erreurs_max = 7 #nombre d'erreurs maximum autorisé
lettres_proposees = [] #liste des lettres déjà proposées par le joueur


#============Boucle principale du jeu=========
while "_" in mot_masque and erreurs < erreurs_max: #on continue tant qu'il reste des "_" et que le joueur n'a pas perdu
    print(" ".join(mot_masque)) #affiche le mot masqué ("join" colle les éléments de la liste avec un espace)
    print("erreurs: ", erreurs, "/", erreurs_max)
    print("lettres déjà proposées: ", lettres_proposees)

    lettre = input("Lettre : ").upper() #le joueur entre une lettre, ".upper()" la met en majuscule

    if lettre in lettres_proposees: #la lettre a déjà été proposée : pas d'erreur de plus
        print("Lettre déjà proposée")
    else:
        lettres_proposees.append(lettre) #".append" ajoute la lettre à la liste des lettres proposées

        if lettre in mot: #la lettre est présente dans le mot
            for i in range(len(mot)): #on parcourt toutes les positions du mot
                if mot[i] == lettre: #si la lettre est à cette position
                    mot_masque[i] = lettre #on la révèle dans le masque
        else: #la lettre est absente du mot
            erreurs = erreurs + 1 #on incrémente le compteur d'erreurs


#============Fin de partie=========
if "_" not in mot_masque: #plus de "_" : le joueur a trouvé le mot
    print("Gagné, le mot était", mot)
else: #le joueur a atteint le nombre maximum d'erreurs
    print("Perdu, le mot était", mot)
