from navire import Navire
from grille import Grille

class BatailleNavale:
    def __init__(self):
        self.navires= [
            Navire('aircraft', ['B2', 'C2', 'D2', 'E2', 'F2']),
            Navire('cruiser', ['A4']),
            Navire('destroyer', ['C5', 'C6', 'C7']),
            Navire('submarine', ['H5', 'I5', 'J5']),
            Navire('torpedo', ['E9', 'F9'])
        ]
        self.grille = Grille(self.navires)
        

game = BatailleNavale()

for navire in game.navires:
    print(f"{navire.nom} : {navire.positions}")