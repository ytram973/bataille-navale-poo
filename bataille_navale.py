from navire import Navire
from grille import Grille

class BatailleNavale:
    def __init__(self):
        self.navires = [
            Navire('aircraft', ['B2', 'C2', 'D2', 'E2', 'F2']),
            Navire('cruiser', ['A4']),
            Navire('destroyer', ['C5', 'C6', 'C7']),
            Navire('submarine', ['H5', 'I5', 'J5']),
            Navire('torpedo', ['E9', 'F9'])
        ]
        self.grille = Grille(self.navires)

    def game(self):
        print("🛳️  Bataille navale game\n")

        while any(not n.navire_coule() for n in self.navires):
            self.grille.afficher()
            guess = input("Choisissez une case à tirer : ").upper()

            if not self.grille.est_coord_valide(guess):
                print("❌ Coordonnée non valide. Réessayez.")
                continue

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