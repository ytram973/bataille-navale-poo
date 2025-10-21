from navire import Navire
from grille import Grille

class BatailleNavale:
    # Classe principale du jeu de bataille navale
    def __init__(self):
        """
        Initialise le jeu :
        - Crée les navires avec leur nom et leurs positions
        - Crée la grille et y associe les navires
        """
        self.navires = [
            Navire('aircraft', ['B2', 'C2', 'D2', 'E2', 'F2']),
            Navire('cruiser', ['A4']),
            Navire('destroyer', ['C5', 'C6', 'C7']),
            Navire('submarine', ['H5', 'I5', 'J5']),
            Navire('torpedo', ['E9', 'F9'])
        ]
        self.grille = Grille(self.navires)

    def game(self):
        """
        Boucle principale du jeu.
        - Affiche la grille
        - Demande à l'utilisateur une coordonnée à tirer
        - Vérifie si le tir est valide et s'il touche un navire
        - Enregistre le tir et affiche les résultats
        """
        
        print("🛳️  Bataille navale game\n")
        # Tant qu'il reste au moins un navire non coulé
        while any(not n.navire_coule() for n in self.navires):
            # Affiche la grille actuelle avec les tirs déjà effectués
            self.grille.afficher()
            # Demande à l'utilisateur une coordonnée (ex: "B4") et met en majuscules
            guess = input("Choisissez une case à tirer : ").upper()
            
            # Vérifie si la coordonnée est valide
            if not self.grille.est_coord_valide(guess):
                print("❌ Coordonnée non valide. Réessayez.")
                continue
            
            # Vérifie si cette case a déjà été tirée
            if guess in self.grille.tirs:
                print("⚠️ Vous avez déjà tiré ici.")
                continue

            # Vérifie si un navire est touché
            touche = False
            for navire in self.navires:
                if navire.tirer(guess):
                    touche = True
                    break

            # Enregistre le tir et son résultat
            self.grille.enregistrer_tir(guess, touche)

            if not touche:
                print("🌊 Tir manqué.")

        print("\n🎉 Tous les navires ont été coulés !")


if __name__ == "__main__":
    jeu = BatailleNavale()
    jeu.game()