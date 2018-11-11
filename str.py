#importations 
from processus import Tache 
from random import randint
import matplotlib.pyplot as plt

#fonction pour creer une liste de taches 5  aléatoires 
def creationTacheAleatoire( nbre_taches):
	i = 0
	l = []
	while i < nbre_taches :
		t = Tache("Tache {}".format(i),randint(0,5), randint(1,10))
		l.append(t)
		i =i+1

	return l


def duree_totale(liste_taches):
	''' Rteourne la durée totale des taches de la liste passée en paramètres '''
	duree_totale =0
	for tache in liste_taches :
		duree_totale +=tache.duree 
	return duree_totale
def duree_totale_execution(liste_taches):
	''' Rteourne la durée totale des taches de la liste passée en paramètres '''
	duree_totale =0
	for tache in liste_taches :
		duree_totale +=tache.temps_execution 
	return duree_totale
#First Come First serve 
def fcfs(liste_taches):
	# classement par ordre d'arrivée 
	return sorted(liste_taches, key=lambda tache: tache.arivee)
#Shortest JOb First
def temps_restant_ord(liste_taches):
	temps_execution = liste_taches[-1].arivee-liste_taches[0].arivee # trouver le temps d'execution de la tache en cours
	if liste_taches[0].temps_restant < temps_execution :
		i=1
		while i<len(liste_taches):
			liste_taches[i].arivee = liste_taches[0].arivee+liste_taches[0].temps_restant
			i+=1
		liste_taches[0].temps_restant = 0
	else :
		liste_taches[0].temps_restant-=temps_execution

	return sorted(liste_taches, key=lambda tache: tache.temps_restant)
#fonction pour mettre a jour les temps d'arriver des taches 
def set_temps_arrive(liste_taches):
	for tache in liste_taches:
		tache.arivee=liste_taches[-1].arivee
	return liste_taches

def sjf(liste_taches):
	#ranger la liste des taches par ordre d'arivée <==> appliquer un fcfs 
	liste_fcfs = fcfs(liste_taches)
	#liste des taches ordonnancées à retourner 
	list_sjf=[]
	list_sjf.append(liste_fcfs[0])
	#liste des taches courantes  : ltc
	ltc = [liste_fcfs[0],liste_fcfs[1]]
	taches_restantes = len(liste_fcfs)
	i=2
	while len(ltc)>0 :
		ltc=temps_restant_ord(ltc)
		list_sjf.append(ltc[0])
		if ltc[0].temps_restant==0 :
			del ltc[0]
		else:
			set_temps_arrive(ltc)
		ltc.append(liste_fcfs[i])
		if i<taches_restantes :
			i+=1
	return list_sjf
#Fonction pour adapter les séquencements afin de les tracer	
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


def awt_fcfs(liste_taches):
	i=1
	liste_taches[0].waiting_time=0
	while i<len(liste_taches) :
		j=0
		temp_time=0
		while j<=i :
			temp_time += liste_taches[j].duree
			j+=1
		liste_taches[i].waiting_time = temp_time-liste_taches[i].arivee
		i+=1
	return liste_taches

def average_wt(liste_taches):
	i=0
	somme = 0
	while i<len(liste_taches) :
		somme+=liste_taches[i].waiting_time
		i+=1
	return somme/len(liste_taches)



#programme principal
liste = creationTacheAleatoire(3)
# print("---Liste des taches ----")
# for tache in liste :
# 	print(tache)

print("---Ordonnancement des taches : FCFS ---")
fcfs_list = fcfs(liste)
for tache in fcfs_list:
	print(tache)

print("---Waiting Time ---")
fcfs_list = fcfs(liste)
for tache in awt_fcfs(fcfs_list):
	print("{} |vWaiting Time {}".format(tache.nom,tache.waiting_time))
print("AWT : {}".format(average_wt(awt_fcfs(fcfs_list))))
 
# print('---Tache avec duree accumulée')
# for tache in suite_tache(fcfs_list) :
# 	print(tache)

# print('---Ordonnancement SJF---')
# for tache in sjf(fcfs_list) :
# 	print(tache)
