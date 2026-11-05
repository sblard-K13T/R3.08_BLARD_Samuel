import csv
#==============Création de la classe Livre=========

class Livre:  # Création de la classe Livre

    def __init__(self, titre, auteur, annee):
        # Enregistrement des informations du livre
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

        # Au départ, le livre est disponible
        self.disponible = True

        # Aucun utilisateur n'a encore emprunté le livre
        self.emprunteur = None

    def afficher(self):
        # Affichage des informations du livre
        print("Titre :", self.titre)
        print("Auteur :", self.auteur)
        print("Année :", self.annee)

        # Affichage de l'état du livre
        if self.disponible == True:
            print("Disponible")
        else:
            print("Emprunté par", self.emprunteur)

    def emprunter(self, nom):
        # Vérification si le livre est disponible
        if self.disponible == True:
            self.disponible = False  # Le livre devient indisponible
            self.emprunteur = nom  # Enregistrement de l'emprunteur
            return True  # L'emprunt a réussi
        else:
            return False  # Le livre est déjà emprunté

    def rendre(self):
        # Vérification si le livre est actuellement emprunté
        if self.disponible == False:
            self.disponible = True  # Le livre redevient disponible
            self.emprunteur = None  # Suppression du nom de l'emprunteur
            return True  # Le retour a réussi
        else:
            return False  # Le livre était déjà disponible

#==============Création de la classe Utilisateur=========

class Utilisateur:  # Création de la classe Utilisateur

    def __init__(self, nom):
        self.nom = nom  # Enregistrement du nom de l'utilisateur
        self.emprunts = []  # Liste vide des livres empruntés

    def emprunter_livre(self, livre):
        # Demande au livre si l'emprunt est possible
        if livre.emprunter(self.nom) == True:
            self.emprunts.append(livre)  # Ajout du livre dans la liste
            print(self.nom, "a emprunté", livre.titre)
            return True
        else:
            print("Le livre n'est pas disponible")
            return False

    def rendre_livre(self, livre):
        # Vérification si l'utilisateur possède ce livre
        if livre in self.emprunts:

            # Demande au livre d'effectuer le retour
            if livre.rendre() == True:
                self.emprunts.remove(livre)  # Retrait de la liste
                print(self.nom, "a rendu", livre.titre)
                return True

        # Si l'utilisateur ne possède pas le livre
        print("Cet utilisateur n'a pas emprunté ce livre")
        return False

    def afficher_emprunts(self):
        # Affichage des livres empruntés par l'utilisateur
        print("Livres empruntés par", self.nom, ":")

        # Vérification si la liste est vide
        if len(self.emprunts) == 0:
            print("Aucun emprunt")
        else:
            # Parcours de la liste des livres empruntés
            for livre in self.emprunts:
                print("-", livre.titre)

#==============Gestion de la bibliothèque=========

class Bibliotheque:

    def __init__(self):
        # Dictionnaire des livres : titre -> livre
        self.livres = {}

        # Dictionnaire des utilisateurs : nom -> utilisateur
        self.utilisateurs = {}

    def ajouter_livre(self, livre):
        # Vérification si le livre existe déjà
        if livre.titre in self.livres:
            print("Ce livre existe déjà")
            return False

        # Ajout du livre dans le dictionnaire
        self.livres[livre.titre] = livre
        print("Livre ajouté :", livre.titre)
        return True

    def ajouter_utilisateur(self, utilisateur):
        # Vérification si l'utilisateur existe déjà
        if utilisateur.nom in self.utilisateurs:
            print("Cet utilisateur existe déjà")
            return False

        # Ajout de l'utilisateur dans le dictionnaire
        self.utilisateurs[utilisateur.nom] = utilisateur
        print("Utilisateur ajouté :", utilisateur.nom)
        return True

    def emprunter(self, nom, titre):
        # Vérification si l'utilisateur existe
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu")
            return False

        # Vérification si le livre existe
        if titre not in self.livres:
            print("Livre inconnu")
            return False

        # Récupération de l'utilisateur et du livre
        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        # Tentative d'emprunt
        return utilisateur.emprunter_livre(livre)

    def rendre(self, nom, titre):
        # Vérification si l'utilisateur existe
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu")
            return False

        # Vérification si le livre existe
        if titre not in self.livres:
            print("Livre inconnu")
            return False

        # Récupération de l'utilisateur et du livre
        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        # Tentative de retour
        return utilisateur.rendre_livre(livre)

    def afficher_livres(self):
        # Vérification si la bibliothèque est vide
        if len(self.livres) == 0:
            print("Aucun livre dans la bibliothèque")
            return

        # Parcours de tous les livres
        for livre in self.livres.values():
            livre.afficher()
            print("--------------------")

    def sauvegarder(self, fichier="bibliotheque.csv"):
        # Ouverture du fichier en écriture
        with open(fichier, "w", newline="", encoding="utf-8") as f:

            # Création du lecteur CSV
            writer = csv.writer(f)

            # Écriture de la première ligne
            writer.writerow([
                "titre", "auteur", "annee",
                "disponible", "emprunteur"
            ])

            # Écriture des informations de chaque livre
            for livre in self.livres.values():
                writer.writerow([
                    livre.titre,
                    livre.auteur,
                    livre.annee,
                    livre.disponible,
                    livre.emprunteur or ""
                ])

        print("Bibliothèque sauvegardée")

    def charger(self, fichier="bibliotheque.csv"):
        # Tentative d'ouverture du fichier
        try:
            with open(fichier, "r", newline="", encoding="utf-8") as f:

                # Lecture du fichier CSV
                reader = csv.DictReader(f)

                # Parcours des lignes du fichier
                for ligne in reader:
                    livre = Livre(
                        ligne["titre"],
                        ligne["auteur"],
                        int(ligne["annee"])
                    )

                    # Restauration de la disponibilité
                    livre.disponible = (
                        ligne["disponible"] == "True"
                    )

                    # Restauration du nom de l'emprunteur
                    nom = ligne["emprunteur"]
                    livre.emprunteur = nom if nom else None

                    # Ajout du livre à la bibliothèque
                    self.livres[livre.titre] = livre

                    # Restauration des utilisateurs ayant emprunté un livre
                    if nom:
                        if nom not in self.utilisateurs:
                            self.utilisateurs[nom] = Utilisateur(nom)

                        self.utilisateurs[nom].emprunts.append(livre)

            print("Bibliothèque chargée")

        except FileNotFoundError:
            # Le fichier n'existe pas encore au premier lancement
            print("Aucune sauvegarde trouvée, nouvelle bibliothèque")


#==============Test du programme=========

# Création d'un livre
l = Livre("1984", "Orwell", 1949)

# Création de deux utilisateurs
u1 = Utilisateur("Ana")
u2 = Utilisateur("Léo")

# Affichage des informations du livre
l.afficher()

# Ana emprunte le livre
u1.emprunter_livre(l)

# Léo essaie d'emprunter le même livre
u2.emprunter_livre(l)

# Affichage des emprunts d'Ana
u1.afficher_emprunts()

# Ana rend le livre
u1.rendre_livre(l)

# Vérification de l'état du livre
l.afficher()


#==============Test de la classe Bibliotheque=========

# Création d'une bibliothèque
bib = Bibliotheque()

# Ajout de livres dans la bibliothèque
bib.ajouter_livre(Livre("1984", "Orwell", 1949))
bib.ajouter_livre(Livre("Le Petit Prince", "Saint-Exupéry", 1943))

# Ajout d'utilisateurs dans la bibliothèque
bib.ajouter_utilisateur(Utilisateur("Ana"))
bib.ajouter_utilisateur(Utilisateur("Léo"))

# Ana emprunte un livre via la bibliothèque
bib.emprunter("Ana", "1984")

# Léo essaie d'emprunter le même livre (doit échouer)
bib.emprunter("Léo", "1984")

# Léo emprunte un autre livre
bib.emprunter("Léo", "Le Petit Prince")

# Affichage de tous les livres de la bibliothèque
bib.afficher_livres()

# Ana rend son livre
bib.rendre("Ana", "1984")

# Sauvegarde de la bibliothèque dans un fichier CSV
bib.sauvegarder()

# Chargement de la bibliothèque depuis le fichier CSV
bib2 = Bibliotheque()
bib2.charger()

# Affichage de la bibliothèque rechargée
bib2.afficher_livres()