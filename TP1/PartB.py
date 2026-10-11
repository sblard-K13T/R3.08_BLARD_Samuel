import random #permet d'utiliser la fonction qui tire un nombre au hasard

print("Devine le nombre")

#============Paramètres du jeu=========
nombre_secret = random.randint(1, 100) #"randint(1, 100)" tire un nombre entier au hasard entre 1 et 100 compris
essais_max = 10 #nombre d'essais maximum autorisés
essai = 0 #compteur du nombre d'essais déjà utilisés
gagne = False #devient True quand le joueur trouve le nombre


#============Boucle principale du jeu=========
while essai < essais_max and gagne == False: #on continue tant qu'il reste des essais et que le joueur n'a pas gagné
    proposition = int(input("Proposition : ")) #"input" demande une valeur et "int" la convertit en nombre entier
    essai = essai + 1 #on compte un essai de plus

    if proposition < nombre_secret: #la proposition est plus petite que le nombre secret
        print("Trop petit")
    elif proposition > nombre_secret: #la proposition est plus grande que le nombre secret
        print("Trop grand")
    else: #ni trop petit ni trop grand : c'est le bon nombre
        print("Gagné")
        gagne = True


#============Fin de partie=========
if gagne == False: #le joueur a utilisé tous ses essais sans trouver
    print("Perdu, le nombre était", nombre_secret)