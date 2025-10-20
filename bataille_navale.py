def grill_navale(tirs, navires_origine):
    """
    Affiche la grille de jeu actuelle en fonction des tirs effectués et des positions initiales des navires.

    Les cases sont marquées :
    - "X" si un tir touche un navire
    - "~" si un tir est manqué
    - "0" si aucune action n'a encore été effectuée sur cette case

    Args:
        tirs (list of str): Liste des coordonnées tirées (ex: ["B2", "C5"]).
        navires_origine (dict): Dictionnaire contenant les positions initiales des navires.

    Returns:
        tuple: Deux listes représentant les lettres des colonnes et les chiffres des lignes.
    """
    
    grille = [["0" for _ in range(10)] for _ in range(10)]

    colonnes_lettres = [chr(ord('A') + i) for i in range(10)]
    lignes_chiffres = [str(i) for i in range(1, 11)]

    for tir in tirs:
        col = colonnes_lettres.index(tir[0])
        row = lignes_chiffres.index(tir[1:])

        touche = any(tir in positions for positions in navires_origine.values())
        grille[row][col] = "X" if touche else "~"

    # Affichage
    print("\n   " + " ".join(colonnes_lettres))
    for i in range(10):
        print(f"{lignes_chiffres[i]:>2} " + " ".join(grille[i]))

    return colonnes_lettres, lignes_chiffres

# table de hachage

navires_origine = {
    'aircraft': ['B2', 'C2', 'D2', 'E2', 'F2'],
    'cruiser': ['A4'],
    'destroyer': ['C5', 'C6', 'C7'],
    'submarine': ['H5', 'I5', 'J5'],
    'torpedo': ['E9', 'F9'],
}

# La vraie table qui va être modifiée pendant le jeu
navires = {k: v.copy() for k, v in navires_origine.items()}

def bataille_navale():
    tirs=[]
    while any(navires[navire] for navire in navires):
        colonnes_lettres, lignes_chiffres=grill_navale(tirs, navires_origine)
        
        guess = input('choisiez un endroit ou tirer capitaine: ').upper()
        
        
        if not check_input(guess, colonnes_lettres, lignes_chiffres):
            print("Coordonnée invalide. Réessayez.")
            continue

        if guess in tirs:
            print("Vous avez déjà tiré ici !")
            continue

        tirs.append(guess)
        
        
        check_input(guess,colonnes_lettres,lignes_chiffres)
        retirer_coord(navires,coord=guess)
    
    
       
 
# function qui check le tir si les cordonner sont bonne et qui affiche si cest toucher ou pas
def check_input(guess, colonnes_lettres, lignes_chiffres):
    # 
    if len(guess) < 2:
        print(f"Coordonnée invalide : {guess}")
        return False

    lettre = guess[0]
    chiffre = guess[1:]

    if lettre in colonnes_lettres and chiffre in lignes_chiffres:
        index_lettre = colonnes_lettres.index(lettre)
        print(f"Coordonnée valide : {lettre}{chiffre} (Index lettre : {index_lettre})")

        trouve = False
        for nom, positions in navires.items():
            if guess in positions:
                print(f"Tir réussi ! {guess} touche le navire : {nom}")
                trouve = True
                break
        if not trouve:
            print(f"Tir manqué à la position : {guess}")
        return True
    else:
        print(f"Coordonnée invalide : {guess}")
        return False






# function qui retire les cordonner dans le dictionaire par rapport au tir de lutilisateur
def retirer_coord(navires,coord):
    for nom, positions in navires.items():
        if coord in positions:
            positions.remove(coord)
            print(f"{coord} une partie du navire est toucher : {nom}")
            if not positions:
                print(f"LE navire {nom} est coulé")
            return
    print(f"{coord} ne correspond a aucun navires")
        
        
        
        
        
if __name__ == '__main__':
    bataille_navale()