
def PCC(A,s):
    i,j = s[0],s[1]
    #liste des poids
    λ = []    
    λ.append(A[i][j])
    
    #nombre de points de λ
    n = len(λ)

    #sommets à explorer
    Q = [s]
    
    while len(Q)!=0 :
        poids_min = min(λ)
        indice = λ.index(poids_min)
        for j in range len(A[indice]):
            if A[indice][j] !=0:
                
            
