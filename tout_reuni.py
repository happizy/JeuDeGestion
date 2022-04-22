from random import*
liste = ["Voulez-vous augmenter les impôts?","Nous manquons de ressources. Devons-nous piller l'Etat voisin?","Voulez-vous censurer les médias?"]#liste des questions à poser, qui ne bouge pas
reponses=[15,-20,5,-10,1,0,20,-10,-30,-20,-5,15,1,-20,-20,-1,20,20]#les valeurs à changer pour chaque réponse (oui/non) de chaque question

economie=50
peuple=50
relationsInternationales=50 #la valeur initiale des 'jauges'
c="vous avez gagné!"

pseudo=str(input("quel est votre nom?"))

def fin(j): # la fonction détecte si une jauge est à 0 et "casse" la boucle while
    if (j<=0):
        global c
        c="fin:vous avez perdu..."
        for k in range(0, len(liste)):
            del(liste[k])     #supprimer les questions s'il en reste pour sortir de la boucle while
            
    

while((len(liste))>0): #tant que toutes les questions de la liste ne sont pas posées
          i=randint(0,len(liste)-1)#choisir une question au hasard
          
          reponse= str(input(liste[i]))
          
          n=0
          if (reponse=="non"):
            n=3#parce que les 3 premiers chiffres sont pour le "oui", et les trois suivants pour le "non"
               #n sert à décaler les chiffres pris     
          
          economie=economie+(reponses[(i*6)+n+0])#6, parce qu'il y a 6 chiffres par question
        
          peuple=peuple+(reponses[(i*6)+n+1])
      
          relationsInternationales=relationsInternationales+(reponses[(6*i)+n+2])
         
                  
          if(reponse=="non"):n=0
         
          del(liste[i])
          del(reponses[(i*6+n):(i*6+n+6)])
          #supprimer les réponses correspondant à la question déjà posée, pour que le système avec la place du i
          #marche même si des éléments de reponses se suppiment au fur et à mesure
          fin(economie)
          fin(peuple)
          fin(relationsInternationales)#pour vérifier si une des jauges est à 0
print(c)
score = economie+peuple+relationsInternationales
yehehe=["a","b"]
if (c=="vous avez gagné!"):
    print ("votre score:",score)

    #va chercher le classement dans un fichier texte
    file = open('fichier_à _lire.txt', "r")
    classement=file.readlines()
    yehehe=classement
        
    file.close()

    #transforme les valeurs lues dans le texte en entiers
    for w in range (0,len(classement)):
        caracteres=list(classement[w])
        if (w<(len(classement)-1)):
            del(caracteres[len(caracteres)-1])
        yehehe[w]=int("".join(caracteres))
    yehehe.append(score)

    #réordonne la liste et donne le classement
    for i in range (0,(len(yehehe))):
        b=1
        while (b!=len(yehehe)):
            if(yehehe[len(yehehe)-b]>yehehe[len(yehehe)-(b+1)]):
                yehehe[len(yehehe)-(b+1)], yehehe[len(yehehe)-b] = yehehe[len(yehehe)-b],yehehe[len(yehehe)-(b+1)]
            b=b+1
            #on part du dernier nombre de la liste, et s'il est plus grand que celui à sa gauche, il prend sa place. 
    print("Bravo", pseudo,", vous êtes en position ", (yehehe.index(score))+1, "dans le classement!")
    print("Classement:",yehehe)







    
