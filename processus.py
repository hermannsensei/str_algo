class Tache():
	""" 
	Représente les taches, leur durée d'execution, leurs temps d'arrivé, et eventuellement leur burst time"""
	def __init__(self, nom, arivee, duree):
		self.arivee = arivee
		self.duree = duree
		self.nom = nom
		self.temps_execution =0
		self.temps_restant = duree
	def __repr__(self):
		return "<{} (Arivée : {} , Durée : {}, Restant {})> ".format(self.nom,self.arivee,self.duree,self.temps_restant)
