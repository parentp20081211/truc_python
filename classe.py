class Personnage:
    def __init__(self, sante, protection, force):
        self.sante = sante
        self.protection = protection
        self.force = force

    def démarrer(self):
        print("La " + self.marque + " démarre.")