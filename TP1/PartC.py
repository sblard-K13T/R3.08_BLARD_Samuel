import random #permet de choisir un élément au hasard dans une liste

print("Jeux de Test")

#Liste de mots utilisée pour le jeu
mots = ["python", "ordinateur", "clavier", "reseau", "serveur", "programme"]
print("liste de mots: ", mots)


#============fonction qui choisit un mot au hasard=========
def choisir_mot(liste): #prend en paramètre la liste de mots
    mot = random.choice(liste) #"random.choice" renvoie un élément de la liste au hasard
    return mot.upper() #".upper()" met le mot en MAJUSCULES


print("mot choisi: ", choisir_mot(mots))


#============fonction qui construit le masque du mot=========
def masque(mot): #prend en paramètre le mot à cacher
    return ["_"] * len(mot) #crée une liste de "_" de la même longueur que le mot ("len" donne le nombre de lettres)


print("masque de PYTHON: ", masque("PYTHON"))
