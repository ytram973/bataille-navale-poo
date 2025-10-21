class Grille:
    def __init__(self,navires):
        self.navires = navires
        self.tirs = []
        self.resultats_tirs={}
        self.colonnes = [chr(ord('A') + i) for i in range(10)]
        self.lignes = [str(i) for i in range(1, 11)]
    
    
    def enregistrer_tir(self, coord, touche):
        """Mémorise le résultat d'un tir."""
        self.tirs.append(coord)
        self.resultats_tirs[coord] = touche
        
        
    def afficher(self):
        grille = [["0" for _ in range(10)] for _ in range(10)]
        
        for tir in self.tirs:
            col = self.colonnes.index(tir[0])
            row = self.lignes.index(tir[1:])
            
            if tir in self.resultats_tirs and self.resultats_tirs[tir]:
                grille[row][col] = "X"
            else:
                grille[row][col] = "~"
        
        print("\n   " + " ".join(self.colonnes))
        for i in range(10):
            print(f"{self.lignes[i]:>2} " + " ".join(grille[i]))
            
    def est_coord_valide(self, guess):
        if len(guess) < 2:
            return False
        lettre, chiffre = guess[0], guess[1:]
        return lettre in self.colonnes and chiffre in self.lignes