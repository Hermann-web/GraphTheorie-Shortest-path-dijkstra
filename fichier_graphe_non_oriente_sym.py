import random
import numpy as np

####nombre de sommets
N= 8
INF = float('inf')
R=50000000

####definir la matrice d'adjacence
def p(i,j):
    p = random.randint(1,R)
    return 0 if p > 3*R/4 else p
#test
# for i in range(10):
#     print(p(0,4))
A = [ [ p(i,j)  for j in range(N)] for i in range(N)]


#avoir une matrice symétrique à coeff diagonaux nulls
for i in range(N):
	A[i][i]=0
	for j in range(i):
		A[i][j] = A[j][i]

#aucun noeud ne doit être isolé
nb = 0
for i in range (len(A)):
	if N-A[i].count(0)<1 : #si le noeuds est isolé
		try:
			noeuds_choisi = random.randint(i+1,N-1)
		except:
			noeuds_choisi = random.randint(1,i)

		poids_choisi = random.randint(1,50)
		A[i][noeuds_choisi] = A[noeuds_choisi][i] = poids_choisi
	nb+= N-A[i].count(0)

def afficher_matrice(A):
	for i in range(len(A)):
		for j in range(len(A[0])):
			str = (2 + int(np.log(R)/np.log(10))- int(np.log(A[i][j])/np.log(10)) ) * " " if A[i][j]!=0 else (2+ int(np.log(R)/np.log(10)))*" "
			print(A[i][j],end=str)
		print("\n")
	print("\n")



afficher_matrice(A)
print("nbInt={} sur {} elements ".format(nb,len(A)**2), end = "\n\n")



Matrice_Adjacence = A

afficher_matrice(Matrice_Adjacence)

####sommet de départ
sommet_depart = 0   
print("sommet de départ= ",sommet_depart,end = "\n\n")




def PCC(A,s): #A est une matrice (n,n) et s, un entier entre 0 et len(A)-1
	#des vérifications
	B = np.array(A)
	if (B != np.transpose(B)).any():
		print("matrice d'adjacence non symétrique")
		return
	if s not in range(0,len(A)): 
		print("sommet inexistant")
		return
	if (B.diagonal()!=0).any():
		print("retranchez les valeurs des diagonales")
		return

	#des initialisations
	λ = [INF for i in range(len(A))]  #liste des distances à s  
	λ[s] = 0 
	Q = [s] #liste des sommets en cours
	D = [] #liste des sommets déjà visités

	while len(Q)!=0:

		print(λ)
		#identifier le sommet courant
		distance_min = INF; sommet_courant=0;
		for somet in Q:
			if λ[somet] < distance_min:
				distance_min = λ[somet]
				sommet_courant = somet
				break

		#enlever le sommet couant de la liste des sommets à visitet
		print("\n")
		print("tentative d'enlever {} de Q".format(sommet_courant))
		Q.remove(sommet_courant); print("opération réussie: distance min entre {} et {} touvé = {}".format(s,sommet_courant,distance_min))
		D.append(sommet_courant)


		#actualiser les distances
		liste_poids_successeurs = A[sommet_courant]
		for sommet_sucesseur in range(len(liste_poids_successeurs)):
			if liste_poids_successeurs[sommet_sucesseur]!=0:
				#ajouter le sommet à liste des sommets à visiter
				if sommet_sucesseur not in Q and sommet_sucesseur not in D: 
					Q.append(sommet_sucesseur)
					print("le sommet {} a été ajouté".format(sommet_sucesseur))
					#voir si la distance à s est plus petite quand on passe par le sommet courant
					distance = λ[sommet_sucesseur]
					distance_passant_par_s = distance_min + A[sommet_courant][sommet_sucesseur]
					λ[sommet_sucesseur] = min(distance, distance_passant_par_s)
	return λ
                
print(PCC(Matrice_Adjacence,sommet_depart) ,end="\n\n")

