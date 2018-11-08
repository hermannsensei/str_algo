i=1 #i de la boucle while
	duree_courante =0 
	liste_fcfs = fcfs(liste_taches) # classer les taches par ordre d'arrivée 
	duree_Totale = duree_totale(liste_fcfs)
	list_sjf=[] # liste à retourner
	list_sjf.append(liste_fcfs[0]) # on ajoute la première tache par défaut
	          # pour sortir de la boucle la somme des durée des tache doivent  etre égale 
		     #calculer le temps d'exécution restant pour la tache précédente et la comparer aux taches arrivantes
	taches_restantes = len(liste_fcfs) 
	while taches_restantes!=0:
		tache_precedente = liste_fcfs[i-1]
		tache_suivante = liste_fcfs[i]
		temps_execution = tache_suivante.arivee - tache_precedente.arivee
		tache_suivante.temps_restant = tache_suivante.temps_restant- temps_execution
		# tache_suivante.temps_execution=temps_execution

		#les cas de figures 
		if tache_precedente.temps_restant == 0:
			list_sjf.append(tache_suivante)
			taches_restantes -=1
		elif tache_precedente.temps_restant <= tache_suivante.duree:
			list_sjf.append(tache_suivante)
			tache_precedente.arivee = tache_suivante.arivee
		elif tache_precedente.temps_restant > tache_suivante.duree:
			list_sjf.append(tache_suivante)
		i+=1