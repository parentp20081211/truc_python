class Voiture:
    def __init__(self, couleur, marque):
        self.couleur = couleur
        self.marque = marque

    def démarrer(self):
        print("La " + self.marque + " démarre.")

ma_voiture1 = Voiture("rouge", "Toyota")
ma_voiture1.démarrer()  # Utilisation de la méthode démarrer de l'objet ma_voiture1

ma_voiture2 = Voiture("bleu", "Honda")
ma_voiture2.démarrer()
