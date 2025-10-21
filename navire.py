class Navire():
    def __init__(self,nom,positions):
        # Attribut
        self.nom = nom
        self.positions = positions
    
        # 
    def navire_touche(self,guess):
        """revoie True si la case correspond à une partie du navire"""
        return guess in self.positions

    def tirer(self,guess):
        """
        Marque la case comme touchée si elle correspond à une partie du navire.
        
        guess : coordonnée du tir
        Si la case touche le navire :
            - Supprime cette position de la liste des positions restantes
            - Affiche un message :
        Retourne True si le tir touche le navire, False sinon.
        """
        if guess in self.positions:
            self.positions.remove(guess)
            if not self.positions:
                print(f"la navire {self.nom} est coulé !")
            else:
                print(f"Touché sur le {self.nom} !")
            return True
        return False
    
    def navire_coule(self):
        """renvoie True si toutes les positions du navire sont détruites"""
        return len(self.positions) == 0