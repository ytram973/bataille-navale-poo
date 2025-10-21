class Grille:
    # Classe grille du jeux bataille navale
    def __init__(self,navires):
        # Methode qui initi la creéation de la grille
        # navire est une liste de navire qui vien de la classe Navire
        self.navires = navires
        # liste pour stocker les tirs
        self.tirs = []
        # dictionnaire pour stocker le resultat de chaque tir
        self.resultats_tirs={}
        
        #colonnes et ligne du jeux
        self.colonnes = [chr(ord('A') + i) for i in range(10)]
        self.lignes = [str(i) for i in range(1, 11)]
    
    
    def enregistrer_tir(self, coord, touche):
        """Mémorise le résultat d'un tir.
        coord :coordonnée du tir 
        touche: bool
        """
        #Ajoute les tirs dans la liste
        self.tirs.append(coord)
        #Enregistre le resultat touche ou non dans le dict
        self.resultats_tirs[coord] = touche
        
        
    def afficher(self):
        """Affiche la grille avec les tirs déjà effectués."""
        # Cree la grille avec des 0 qui represente l'eau
        grille = [["0" for _ in range(10)] for _ in range(10)]
        
        # Parcourt tous les tirs déjà effectués
        for tir in self.tirs:
            # Trouve l'indice de la colonne (ex: 'A' -> 0, 'B' -> 1)
            col = self.colonnes.index(tir[0])
            # Trouve l'indice de la ligne (ex: '1' -> 0, '10' -> 9)
            row = self.lignes.index(tir[1:])
            # Si le tir est enregistré et touche un navire
            if tir in self.resultats_tirs and self.resultats_tirs[tir]:
                grille[row][col] = "X"
            else:
                grille[row][col] = "~"
        
        print("\n   " + " ".join(self.colonnes))
        for i in range(10):
            print(f"{self.lignes[i]:>2} " + " ".join(grille[i]))
            
            
            
    def est_coord_valide(self, guess):
        """Vérifie si la coordonnée entrée est valide pour la grille.
        
        guess : ex: "B7"
        """
        if len(guess) < 2:
            return False
        lettre, chiffre = guess[0], guess[1:]
        
        return lettre in self.colonnes and chiffre in self.lignes