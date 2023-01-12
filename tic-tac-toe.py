###############ETAPE0#############################################################
grille = {
        0 : [None,None,None],
        1 : [None,None,None],
        2 : [None,None,None]
        }
###############ETAPE1#############################################################
def afficher_grille(grille):
    """afficher une grille c'est une fonction qui affiche une grille 
    """
    for clé in grille:
        for elt in grille[clé]:
            print("|",elt,end="|") #là quand on met end ou sep la fonction print prend pas le passage à la ligne.
        print() #là quand on met cette print(vide) ce nous permet de passer à la ligne 
############ETAPE2################################################################
def jouer_coup(grille, coup,i,j):
        if grille[i][j]==None:
            grille[i][j]=coup
        else:
            print("On peut pas jouer dans cette case")       
#############ETAPE3############################################################  
def test_gagne(grille):
    for i in range(3):
        if grille[i][0]== grille[i][1]== grille[i][2] and grille[i][2]!= None:
            return True
            
    for j in range(3):
        if grille[0][j]==grille[1][j]==grille[2][j] and grille[2][j]!= None:
            return True
    
    if (grille[0][0]==grille[1][1]==grille[2][2] and grille[2][2]!= None) or (grille[0][2]==grille[1][1]==grille[2][0] and grille[2][2]!= None):
                 return True
    return False

#print(test_gagne(grille))
jouer_coup(grille, "x",0,0)
afficher_grille(grille)
print(test_gagne(grille))
##############ETAPE4########################################################### 





 
 



    
    
