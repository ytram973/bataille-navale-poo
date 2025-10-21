# 🛳️ Jeu de Bataille Navale

## 🎯 Objectif

Ce projet est une implémentation en Python du célèbre jeu **Bataille Navale** (version solo).  
Le joueur tire sur des coordonnées de la grille pour tenter de **toucher et couler tous les navires ennemis**.

---

## ⚙️ Instalation

### 1. Cloner le projet
```bash
git clone https://github.com/ton-compte/bataille-navale.git
cd bataille-navale

```

### 2. Lancer le jeu

```bash
python bataille_navale.py

```

#### 💡 Assurez-vous d’avoir Python 3 installé sur votre machine.
---

# 🧩 Description des classes

## 🔹 Class `Navire`

### Represente un navire avec :

- Un nom (`nom`)
- Une liste de positions (`positions`)

### Methodes principales:

  - `navire_touche(guess)`-> revoie True si la case correspond à une partie du navire:
  - `tirer(guess)` -> marque la case comme touchée, affiche un message si le navire est coulé
  - `navire_coule()` -> renvoie True si toutes les positions du navire sont détruites

---

## 🔹 Class `Grille`
### Gère l'affichage du jeu et les tirs du joueur.

### Attributs :

- `navires`: liste des navires sur la grille
- `tirs`: liste des coordonnées déjà jouées
- `resultats_tirs`: dictionnaire `{coordonnée: résultats }`

### Methodes principales:

  - `afficher()`-> affiche la grille avec les tirs (`X` pour touché, `~` pour manqué)
  - `enregistrer_tir(coord, touche)` -> stocke le résultat du tir
  - `est_coord_valide(coord)` -> vérifie que la coordonnée saisie est valide (ex: "B5")
---

## 🔹 Class `Grille`

### La Logique du jeu. 

### Fonctionnement :
1. Initialise plusieurs navires de tailles différentes 
2. Affiche la grille
3. Demande une coordonnée au joueur
4. Vérifie la validité du tir
5. Met à jour la grille et affiche le résultat
6. Continue jusqu’à ce que tous les navires soient coulés

## 🏁 Conditions de victoire

#### La partie se termine quand tous les navires sont coulés 

