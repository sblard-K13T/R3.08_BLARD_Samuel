
#==============Création de la grille de jeu=========

class Grille_jeu: #création de la classe "Grille_jeu"

    def __init__(self): #fonction qui initialise la grille
        self.tab = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def afficher_jeu(self): #affiche le tableau de jeu
        for i in range(3):
            print(" | ".join(self.tab[i])) #pour chaque ligne, rajouter un séparateur " | "
            if i < 2:
                print("__________") #rajoute un séparateur entre les lignes

    def jouer(self, x, y, joueur):
        if not (0 <= x < 3 and 0 <= y < 3): #vérification des coordonnées
            print("Les coordonnées sont mauvaises")
            return False

        if self.tab[x][y] != " ": #vérification si la case est occupée
            print("La case est déjà occupée")
            return False

        if joueur not in ("X", "O"): #vérification du symbole joué
            print("Le symbole est invalide")
            return False

        self.tab[x][y] = joueur #place le symbole dans la case
        return True

    def gagnant(self, j):
        # Vérification des lignes horizontales
        for i in range(3):
            if (self.tab[i][0] == j
                    and self.tab[i][1] == j
                    and self.tab[i][2] == j):
                print("Bravo")
                return True

        # Vérification des colonnes verticales
        for i in range(3):
            if (self.tab[0][i] == j
                    and self.tab[1][i] == j
                    and self.tab[2][i] == j):
                print("Bravo")
                return True

        # Vérification de la première diagonale
        if (self.tab[0][0] == j
                and self.tab[1][1] == j
                and self.tab[2][2] == j):
            print("Bravo")
            return True

        # Vérification de la seconde diagonale
        if (self.tab[2][0] == j
                and self.tab[1][1] == j
                and self.tab[0][2] == j):
            print("Bravo")
            return True

        return False

    def grille_plein(self):
        for ligne in self.tab:
            for case in ligne:
                if case == " ":
                    return False
        return True


#==============Fonction qui permet de jouer une partie=========

def partie():
    g = Grille_jeu()
    joueur = "X"

    while True:
        g.afficher_jeu() #affichage de la grille
        print("Au tour du joueur", joueur)

        # Demander les coordonnées
        try:
            x = int(input("Ligne (0, 1 ou 2) : "))
            y = int(input("Colonne (0, 1 ou 2) : "))
        except ValueError:
            print("Entre des nombres entiers.")
            continue

        # Essayer de jouer
        if not g.jouer(x, y, joueur):
            print("Coup invalide, recommence.")
            continue

        # Vérifier la victoire
        if g.gagnant(joueur):
            g.afficher_jeu()
            print("Le joueur", joueur, "a gagné !")
            break

        # Vérifier le match nul
        if g.grille_plein():
            g.afficher_jeu()
            print("Match nul !")
            break

        # Changer de joueur
        if joueur == "X":
            joueur = "O"
        else:
            joueur = "X"

#==============Lancement du jeu=========

partie()
