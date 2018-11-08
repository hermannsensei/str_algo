
#importations 
from processus import Tache 
from random import randint
import matplotlib.pyplot as plt

#fonction pour creer une liste de taches 5  aléatoires 
def creationTacheAleatoire( nbre_taches):
	i = 0
	l = []
	while i < nbre_taches :
		t = Tache("Tache {}".format(i),randint(0,10), randint(1,20))
		l.append(t)
		i =i+1

	return l


def duree_totale(liste_taches):
	''' Rteourne la durée totale des taches de la liste passée en paramètres '''
	duree_totale =0
	for tache in liste_fcfs :
		duree_totale +=tache.duree 
	return duree_totale
#First Come First serve 
def fcfs(liste_taches):
	# classement par ordre d'arrivée 
	return sorted(liste_taches, key=lambda tache: tache.arivee)
#Shortest JOb First

def sjf(liste_taches):
	j=0
	liste_fcfs = fcfs(liste_taches) # classer les taches par ordre d'arrivée 
	list_sjf=[] # liste à retourner
	list_sjf.append(liste_fcfs[0]) # on ajoute la première tache par défaut
	while j!= len(liste_fcfs): # pour sortir de la boucle la somme des durée des tache doivent  etre égale 
		#calculer le temps d'exécution restant pour la tache précédente et la comparer aux taches arrivantes
	    i=1 #i de la boucle while
		while i<len(liste_fcfs):
			temps_execution = liste_fcfs[i].arivee-liste_fcfs[i-1].arivee
			liste_fcfs[i-1].temps_restant = liste_fcfs[i-1].temps_restant- temps_execution
			liste_fcfs[i-1].temps_execution=temps_execution
			#les cas de figures 
			if liste_fcfs[i-1].temps_restant == 0:
				list_sjf.append(liste_fcfs[i-1])
				j+=1
			elif liste_fcfs[i-1].temps_restant <= liste_fcfs[i].duree:
				list_sjf.append(liste_fcfs[i-1])
			elif liste_fcfs[i-1].temps_restant > liste_fcfs[i].duree:
				list_sjf.append(liste_fcfs[i])	
			i=i+1
	return list_sjf
	
	
def suite_tache(liste_taches):
	i=1
	while i<len(liste_taches):
		liste_taches[i].duree = liste_taches[i].duree + liste_taches[i-1].duree
		i = i+1 
	return liste_taches

def diagramme_gant(liste_taches):
	durees =[]
	arivees =[]
	for tache in liste_taches:
		durees.append(tache.duree)
		arivees.append(tache.arivee)
	plt(arivees,"r",linewidth=10)



#programme principal
liste = creationTacheAleatoire(3)
# print("---Liste des taches ----")
# for tache in liste :
# 	print(tache)

print("---Ordonnancement des taches : FCFS ---")
fcfs_list = fcfs(liste)
for tache in fcfs_list:
	print(tache)

# print('---Tache avec duree accumulée')
# for tache in suite_tache(fcfs_list) :
# 	print(tache)

print('---Ordonnancement SJF---')
for tache in sjf(liste) :
	print(tache)
