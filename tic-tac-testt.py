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
        print() #là quand on met cette print(vide) ca nous permet de passer à la ligne 
############ETAPE2################################################################
def jouer_coup(grille,coup,i,j):
        if  i<=2 and j<=2 and grille[i][j]==None:
            grille[i][j]=coup
            return True
        else:
            return False   
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
##############ETAPE4############################################################
termine=False
afficher_grille(grille)
joueur="joueur 1"
while not termine:
    coup=input("jouer un coup :")    
    if joueur=="joueur 1":
        coup="x"
    if joueur=="joueur 2":
        coup="o"
    coup_line=int(input(" entrer la position en ligne :"))
    coup_colone=int(input("entrer la position en colone :"))
    while not jouer_coup(grille,coup,coup_line,coup_colone):
        coup_line=int(input(" position incorrecte entrer STP une nouvelle position en ligne :"))
        coup_colone=int(input("position incorrecte entrer STP une nouvelle position en colone :"))   
    afficher_grille(grille)
    if test_gagne(grille):
        termine=True
        print(joueur,"a gagné")
    else:
        if joueur=="joueur 1":
            joueur="joueur 2"  
        else:
            joueur="joueur 1"       
#############FINCODE#######################################################
#question: comment interdir le deuxieme joueur de jouer au meme coup (x ou o) que le 1er   
    
     

 
 



    
    
