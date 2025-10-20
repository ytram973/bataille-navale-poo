class Navire():
    def __init__(self,nom,positions):
        # Attribut
        self.nom = nom
        self.positions = positions
    
        # 
    def navire_touche(self,guess):
        return guess in self.positions

    def tirer(self,guess):
        if guess in self.positions:
            self.positions.remove(guess)
            if not self.positions:
                print(f"la navire {self.nom} est coulé !")
            else:
                print(f"Touché sur le {self.nom} !")
            return True
        return False
    
    def navire_coule(self):
        return len(self.positions) == 0