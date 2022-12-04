from tkinter import *                                #| Import Bibli
from tkinter.ttk import *
from PIL import Image,ImageTk
from random import *


    ##----- Le Routeur -----##


fen_active = None                                   #| Variable fenêtre active

#---------------------------------------------#

    ##----- Les Global -----##

longeur_case_joueur = 30                     
nombre_case_joueur = 8                          
case_joueur = []                                    #| Grille Joueur                     

longeur_case_ordi = 60
nombre_case_ordi = 8
case_ordi = []                                      #| Grille Ordinateur

rota = [0]

pos = []                                            #| Liste des tirs joueur
pos_prec = []

tir = []                                            #| Liste des tirs ordi
tir_prec = []

count_sm = 1                                        #| Compteur de placement des bateaux        
count_pa = 1
count_tp = 1
count_fg = 1

#------------- tir joueur ----------------

log_tir_sm = []                                     #| Liste des cases touchées ( par bateaux )
log_tir_pa = []
log_tir_tp = []
log_tir_fg = []

log_tir = []                                        #| Listes des cases touchées ( générale )

check_tir_sm = False                                #| Booléen, vérification bateau coulé ( par bateau )
check_tir_pa = False
check_tir_tp = False
check_tir_fg = False

check_tir_bateau = False                            #| Tir valide

check_pos = False                                   #| Position de tir valide

#------------- tir ordi ----------------

log_tir_ordi_sm = []                                #| Même principe pour le tir ordi
log_tir_ordi_fg = []
log_tir_ordi_pa = []
log_tir_ordi_tp = []

log_tir_ordi = []

check_tir_ordi_sm = False
check_tir_ordi_fg = False
check_tir_ordi_pa = False
check_tir_ordi_tp = False

tir_ordi1 = randint(0,7)                            #| Délimitation de (x, y) tir de l'ordinateur
tir_ordi2 = randint(0,7)

tir_ordi1_backup = tir_ordi1                        #| "Uhmm, sers à rien"
tir_ordi2_backup = tir_ordi2

check_tir_ordi = True


#-----------------------------

start_game = 4                                      #| Compteur ( dépendant des bateaux )
end_game = 4
loose = 4

#---------------------------------------------#

def main():
    global fen_active                               #| Importation dans la fenêtre ( main ) des variables
    global case_joueur
    global case_ordi
    global rota
    global log_tir_sm
    global log_tir_pa
    global log_tir_tp
    global log_tir_fg
    global check_tir_sm
    global check_tir_pa
    global check_tir_tp
    global check_tir_fg
    global count_sm
    global count_pa
    global count_tp
    global count_fg
    global log_tir_ordi_sm
    global log_tir_ordi_fg
    global log_tir_ordi_pa
    global log_tir_ordi_tp
    global log_tir_ordi
    global check_tir_ordi_sm
    global check_tir_ordi_fg
    global check_tir_ordi_pa
    global check_tir_ordi_tp
    global check_IA
    global tir_ordi1
    global tir_ordi2
    global tir_ordi1_backup
    global tir_ordi2_backup
    global check_tir_ordi
    
    global check_tir_bateau
    global check_pos
    global log_tir
    global start_game
    global end_game
    global loose

    try:
        fen_active.destroy()                            #| définir la fenêtre active
    except:
        pass
    
    case_joueur = []
    case_ordi = []
    rota = [0]
    
    #------------- tir joueur ----------------
    
    log_tir_sm = []
    log_tir_pa = []
    log_tir_tp = []
    log_tir_fg = []
    
    check_tir_sm = False
    check_tir_pa = False
    check_tir_tp = False
    check_tir_fg = False
    
    log_tir = []
    
    check_tir_bateau = False
    
    check_pos = False
    
    #------------- tir ordi ----------------

    log_tir_ordi_sm = []
    log_tir_ordi_fg = []
    log_tir_ordi_pa = []
    log_tir_ordi_tp = []
    
    check_tir_ordi_sm = False
    check_tir_ordi_fg = False
    check_tir_ordi_pa = False
    check_tir_ordi_tp = False
    
    log_tir_ordi = []
    
    check_IA = False 
        
    check_tir_ordi = True
    
    #-----------------------------

    count_sm = 1
    count_pa = 1
    count_tp = 1
    count_fg = 1

    start_game = 4
    end_game = 4
    loose = 4

    fen = Tk()                                                          #| Up de la fenêtre de jeu et def de la grille d'affichage (l.187)
    fen.title('Bataille Navale')
    fen.iconbitmap("anchor.ico")

    dessin = Canvas(fen, width = 1200, height = 700)
    dessin.grid(row = 0, column = 0, columnspan=3, padx=3, pady=3)
    
    ##----- BackGround Up -----##

    fond_ocean = (Image.open("ocean.png"))
    resized_image_ocean = fond_ocean.resize((1200,700), Image.ANTIALIAS)
    new_image_ocean = ImageTk.PhotoImage(resized_image_ocean)
    dessin.create_image(0, 0, image = new_image_ocean , anchor ="nw")
    
    ##----- Features -----##

    dessin.create_text(1130, 25, font=('Centaur', 15, "bold", "underline"), text='Bateaux :', fill = "black")       #| Design de Features
    dessin.create_text(1130, 370, font=('Centaur', 15, "bold", "underline"), text='Autres :', fill = "black")
    dessin.create_text(170, 600, font=('Arial', 20, "bold", "underline"), text='Grille Joueur', fill ="black")
    dessin.create_text(750, 600, font=('Arial', 20, "bold", "underline"), text='Grille Ordinateur', fill ="black")
    
    
    dessin.create_line(1030, 10,  1030, 300, fill='SkyBlue2', width = 2)
    dessin.create_line(1030, 300,  1190, 300, fill='SkyBlue2', width = 2)

    dessin.create_line(1030, 340,  1030, 600, fill='SkyBlue2', width = 2)
    dessin.create_line(1030, 340,  1190, 340, fill='SkyBlue2', width = 2)

    ##----- Création des num et lettres grille joueur -----##
    
    dessin.create_text(65,  50, font=('Arial', 10, "bold"), text='A', fill ="black")
    dessin.create_text(95,  50, font=('Arial', 10, "bold"), text='B', fill ="black")
    dessin.create_text(125, 50, font=('Arial', 10, "bold"), text='C', fill ="black")
    dessin.create_text(155, 50, font=('Arial', 10, "bold"), text='D', fill ="black")
    dessin.create_text(185, 50, font=('Arial', 10, "bold"), text='E', fill ="black")
    dessin.create_text(215, 50, font=('Arial', 10, "bold"), text='F', fill ="black")
    dessin.create_text(245, 50, font=('Arial', 10, "bold"), text='G', fill ="black")
    dessin.create_text(275, 50, font=('Arial', 10, "bold"), text='H', fill ="black")
    
    dessin.create_text(40, 75,  font=('Arial', 10, "bold"), text='1', fill ="black")
    dessin.create_text(40, 105, font=('Arial', 10, "bold"), text='2', fill ="black")
    dessin.create_text(40, 135, font=('Arial', 10, "bold"), text='3', fill ="black")
    dessin.create_text(40, 165, font=('Arial', 10, "bold"), text='4', fill ="black")
    dessin.create_text(40, 195, font=('Arial', 10, "bold"), text='5', fill ="black")
    dessin.create_text(40, 225, font=('Arial', 10, "bold"), text='6', fill ="black")
    dessin.create_text(40, 255, font=('Arial', 10, "bold"), text='7', fill ="black")
    dessin.create_text(40, 285, font=('Arial', 10, "bold"), text='8', fill ="black")
    
    
    ##----- Création des num et lettres grille ordi -----##
    
    dessin.create_text(550, 40, font=('Arial', 20, "bold"), text='A', fill ="black")
    dessin.create_text(610, 40, font=('Arial', 20, "bold"), text='B', fill ="black")
    dessin.create_text(670, 40, font=('Arial', 20, "bold"), text='C', fill ="black")
    dessin.create_text(730, 40, font=('Arial', 20, "bold"), text='D', fill ="black")
    dessin.create_text(790, 40, font=('Arial', 20, "bold"), text='E', fill ="black")
    dessin.create_text(850, 40, font=('Arial', 20, "bold"), text='F', fill ="black")
    dessin.create_text(910, 40, font=('Arial', 20, "bold"), text='G', fill ="black")
    dessin.create_text(970, 40, font=('Arial', 20, "bold"), text='H', fill ="black")

    dessin.create_text(500, 90,  font=('Arial', 20, "bold"), text='1', fill ="black")
    dessin.create_text(500, 150, font=('Arial', 20, "bold"), text='2', fill ="black")
    dessin.create_text(500, 210, font=('Arial', 20, "bold"), text='3', fill ="black")
    dessin.create_text(500, 270, font=('Arial', 20, "bold"), text='4', fill ="black")
    dessin.create_text(500, 330, font=('Arial', 20, "bold"), text='5', fill ="black")
    dessin.create_text(500, 390, font=('Arial', 20, "bold"), text='6', fill ="black")
    dessin.create_text(500, 450, font=('Arial', 20, "bold"), text='7', fill ="black")
    dessin.create_text(500, 510, font=('Arial', 20, "bold"), text='8', fill ="black")

#---------------------------------------------#
    
    fen_active = fen                                        #| On enregistre la fenêtre active


    class Tableau_joueur:          #| On créer la grille joueur                      #defini l'objet tableau
        """
        Créer un tableau de bataille navale (joueur)
        """
        def __init__(self, nombre_case_joueur, longeur_case_joueur):
            self.longeur_case_joueur = longeur_case_joueur
            self.nombre_case_joueur = nombre_case_joueur
        
        for ligne in range(nombre_case_joueur):          # Les cases de chaque ligne seront stockées dans "transit"
            transit=[]
            for colonne in range(nombre_case_joueur):    # Conception des cases d'une ligne
                transit.append(dessin.create_rectangle(30+colonne*longeur_case_joueur+20, ligne*longeur_case_joueur+60, 30+(colonne+1)*longeur_case_joueur+20, (ligne+1)*longeur_case_joueur+60))
            case_joueur.append(transit)       # Ajout de la ligne à la liste principale
            
            ##----- Modification des figures créées -----##
        
        for ligne in range(nombre_case_joueur):
            for colonne in range(nombre_case_joueur): 
                dessin.itemconfigure(case_joueur[ligne][colonne], outline='black')
        
    class Tableau_ordi:                #| On créer la grille ordi                     #defini l'objet tableau
        """
        Créer un tableau de bataille navale (ordi)
        """
        def __init__(self, nombre_case_ordi, longeur_case_ordi):
            self.longeur_case_ordi = longeur_case_ordi
            self.nombre_case_ordi = nombre_case_ordi
        
        for ligne in range(nombre_case_ordi):          # Les cases de chaque ligne seront stockées dans "transit"
            transit_ordi=[]
            for colonne in range(nombre_case_ordi):    # Conception des cases d'une ligne
                transit_ordi.append(dessin.create_rectangle(500+colonne*longeur_case_ordi+20, ligne*longeur_case_ordi+60, 500+(colonne+1)*longeur_case_ordi+20, (ligne+1)*longeur_case_ordi+60))
            case_ordi.append(transit_ordi)       # Ajout de la ligne à la liste principale
            
            ##----- Modification des figures créées -----##
        
        for ligne in range(nombre_case_ordi):
            for colonne in range(nombre_case_ordi): 
                dessin.itemconfigure(case_ordi[ligne][colonne], outline='black')


#---------------------------------------------#
    ##----- Ordi Sous-Marin -----##
    
    trash_boucle_debug = 0  
    
    choose_bateau_ordi1 = 0
    choose_bateau_ordi2 = 0
    choose_rota = randint(1, 2)         #| Choix aléatoire de rotation des bateaux de l'ordi
    
    
    if choose_rota == 1:                                            #| Placement des bateaux de l'ordi par l'ordi selon la rotation aléatoire
        choose_bateau_ordi1 = randint(0, 7)
        choose_bateau_ordi2 = randint(1, 6)
        
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2-1] = "S"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "S"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] = "S"
           
    if choose_rota == 2:
        choose_bateau_ordi1 = randint(1, 6)
        choose_bateau_ordi2 = randint(0, 7)
        
        case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2] = "S"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "S"
        case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] = "S"
    
    ##----- Ordi Porte-Avions -----##
        
    choose_rota = randint(1, 2)
    
    if choose_rota == 1:
        choose_bateau_ordi1 = randint(1, 7)
        choose_bateau_ordi2 = randint(0, 4)
        
        while case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+2] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+3] == "S" or case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2+2] == "S" or case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2+3] == "S":
            trash_boucle_debug += 1
            choose_bateau_ordi1 = randint(1, 7)
            choose_bateau_ordi2 = randint(0, 4)
            
        #print(trash_boucle_debug)
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "P"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] = "P"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+2] = "P"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+3] = "P"
        case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2] = "P"
        case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2+1] = "P"
        case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2+2] = "P"
        case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2+3] = "P"
    
    if choose_rota == 2:
        choose_bateau_ordi1 = randint(0, 4)
        choose_bateau_ordi2 = randint(0, 6)
        
        while case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1+2][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1+3][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1+2][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1+3][choose_bateau_ordi2] == "S":
            trash_boucle_debug += 1
            choose_bateau_ordi1 = randint(0, 4)
            choose_bateau_ordi2 = randint(0, 6)
        
        #print(trash_boucle_debug)
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] = "P"
        case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2+1] = "P"
        case_ordi[choose_bateau_ordi1+2][choose_bateau_ordi2+1] = "P"
        case_ordi[choose_bateau_ordi1+3][choose_bateau_ordi2+1] = "P"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "P"
        case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] = "P"
        case_ordi[choose_bateau_ordi1+2][choose_bateau_ordi2] = "P"
        case_ordi[choose_bateau_ordi1+3][choose_bateau_ordi2] = "P"
    
    ##----- Ordi Frégates -----##
        
    choose_rota = randint(1, 2)
    
    if choose_rota == 1:
        choose_bateau_ordi1 = randint(0, 7)
        choose_bateau_ordi2 = randint(1, 6)
        
        while case_ordi[choose_bateau_ordi1][choose_bateau_ordi2-1] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2-1] == "P" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "P" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] == "P":
            trash_boucle_debug += 1
            choose_bateau_ordi1 = randint(0, 7)
            choose_bateau_ordi2 = randint(1, 6)
            
        #print(trash_boucle_debug)
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2-1] = "F"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "F"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] = "F"
    
    if choose_rota == 2:
        choose_bateau_ordi1 = randint(1, 6)
        choose_bateau_ordi2 = randint(0, 7)
        
        while case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2] == "P" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "P" or case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] == "P":
            trash_boucle_debug += 1
            choose_bateau_ordi1 = randint(1, 6)
            choose_bateau_ordi2 = randint(0, 7)
        
        #print(trash_boucle_debug)
        case_ordi[choose_bateau_ordi1-1][choose_bateau_ordi2] = "F"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "F"
        case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] = "F"
        
    ##----- Ordi Torpilleur -----##
        
    choose_rota = randint(1, 2)
    
    if choose_rota == 1:
        choose_bateau_ordi1 = randint(0, 7)
        choose_bateau_ordi2 = randint(0, 6)
        
        while case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "P" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "F" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] == "P" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] == "F":
            trash_boucle_debug += 1
            choose_bateau_ordi1 = randint(0, 7)
            choose_bateau_ordi2 = randint(0, 6)
            
        #print(trash_boucle_debug)
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "T"
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2+1] = "T"
    
    if choose_rota == 2:
        choose_bateau_ordi1 = randint(0, 6)
        choose_bateau_ordi2 = randint(0, 7)
        
        while case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "P" or case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] == "F" or case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] == "S" or case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] == "P" or case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] == "F":
            trash_boucle_debug += 1
            choose_bateau_ordi1 = randint(0, 6)
            choose_bateau_ordi2 = randint(0, 7)
        
        #print(trash_boucle_debug)
        case_ordi[choose_bateau_ordi1][choose_bateau_ordi2] = "T"
        case_ordi[choose_bateau_ordi1+1][choose_bateau_ordi2] = "T"



    
    #print("--------------")
    #print(choose_rota)
    #print(choose_bateau_ordi1, choose_bateau_ordi2)
    print(trash_boucle_debug)                       #| On imprime la boucle de debug qui montre combien de fois l'ordi à du replacer un bateau parce qu'il en superposait un autre
    print(case_ordi[0])                             #| On imprime toutes les lignes de la grille ordi pour connaitre la position des bateaux ennemis ( on triche pour la faire plus court )
    print(case_ordi[1])
    print(case_ordi[2])
    print(case_ordi[3])
    print(case_ordi[4])
    print(case_ordi[5])
    print(case_ordi[6])
    print(case_ordi[7])

#---------------------------------------------#

    #une fonction qui m'a demandé 5h de code

    def rotation(event):                    #| Fonction permettant de tourner nos bateaux dans 4 positions ( selon les 4 tailles possible de la liste rota )
        global rota
        
        
        rota.append(0)
        #print(rota)
        #print(len(rota))
        if (len(rota)) == 1:
            bouton_rota['text'] = "🢂"           #| Features de visualisation graphique de la rotation choisi
        
        if (len(rota)) == 2:
            bouton_rota['text'] = "🢃"
        
        if (len(rota)) == 3:
            bouton_rota['text'] = "🢀"
        
        if (len(rota)) == 4:
            bouton_rota['text'] = "🢁"
        
        if len(rota) == 5:
            rota = [0]
            bouton_rota['text'] = "🢂"

        return rota



    #une autre fonction qui m'a cassée la tête et qui ne sert qu'à détecter un click correct
    
    def motion_joueur(event):                   #| enregistrement du derniers click valide et action opérantes avec 
        global pos
        global pos_prec
        
        if len(pos) == 0:
            x, y = event.x, event.y
            #print(x,y)
            pos_x = (x-50)//30                  #| Fonction permettant de retourver la case clické ( comprendre selon indentations de la grille et taille de chaque cases - d'où division euclidienne )
            pos_y = (y-60)//30
            #print((x-50)//30, (y-50)//30)
            pos.append(x)
            pos.append(y)
            pos.append(pos_x)
            pos.append(pos_y)
            if x<50 or x>290 or y<60 or y>300:
                #print("Hors de la grille")
                pos = []
            try:
                if pos[2]<0 or pos[3]<0:
                    #print("Valeurs Négatives")
                    pos = []
                    #print("Retry in the grid: ",pos)         #| Ne demandez pas pourquoi ici c'est en Anglais, coder à 3h du matin ne fais pas que des miracles 
                    #print(pos_prec)
            except:
                pass
            
            else:
                pos_prec = pos
            #print(pos)
        else:
            pos = []
            x, y = event.x, event.y
            #print(x,y)
            pos_x = (x-50)//30
            pos_y = (y-60)//30
            #print((x-50)//30, (y-50)//30)
            pos.append(x)
            pos.append(y)
            pos.append(pos_x)
            pos.append(pos_y)
            #print(pos)
            if x<50 or x>290 or y<60 or y>300:
                #print("Hors de la grille")
                pos = pos_prec
            try:
                if pos[2]<0 or pos[3]<0:
                    #print("Valeurs Négatives")
                    pos = pos_prec
                    #print("Retry in the grid: ",pos)       
                    #print(pos_prec)
                else:
                    pos_prec = pos
            except:
                pass 
            
        center_x = pos[2]*30+65
        center_y = pos[3]*30+75
        pos.append(center_x)
        pos.append(center_y)
        print("Motion : ",pos)

        return pos                          #| Retour de la liste cnotenant toutes les positions pouvant être utile ( x, y, centre des coordonnées, ect )
    
    
    
    
    def tir(event):                     #| Même fonction que pour Motiono(), mais ici c'est celle qui fait le tir, donc n'a pas la même utilité
        global tir
        global tir_prec
        global start_game
        global case_ordi
        global log_tir_sm
        global log_tir_pa
        global log_tir_tp
        global log_tir_fg
        global check_tir_sm
        global check_tir_pa
        global check_tir_tp
        global check_tir_fg
        global end_game
        
        global check_tir_bateau
        
        save = []
        
        if end_game == -12:                                                                         #| Ne tirer que si on a ni perdu ni gagner, mais que la partie à bien commencée
            dessin.create_text(130, 420, font=('Centaur', 50, "bold"), text='Win', fill ="red")
            pass
        elif loose == -12:
            dessin.create_text(130, 420, font=('Centaur', 50, "bold"), text='Loose', fill ="red")
            pass
        else:
            if start_game == 0:      
                if len(tir) == 0:
                    x, y = event.x, event.y
                    #print(x,y)
                    tir_x = (x-520)//60
                    tir_y = (y-60)//60
                    #print((x-50)//30, (y-50)//30)
                    tir.append(x)
                    tir.append(y)
                    tir.append(tir_x)
                    tir.append(tir_y)
                    if x<520 or x>1000 or y<60 or y>540:
                        #print("Hors de la grille")
                        tir = []
                    try:
                        if tir[2]<0 or tir[3]<0:
                            #print("Valeurs Négatives")
                            tir = []
                            #print("Retry in the grid: ",tir)
                            #print(tir_prec)
                    except:
                        pass
                    
                    else:
                        tir_prec = tir
                    #print(tir)
                else:
                    tir = []
                    x, y = event.x, event.y
                    #print(x,y)
                    tir_x = (x-520)//60
                    tir_y = (y-60)//60
                    #print((x-50)//30, (y-50)//30)
                    tir.append(x)
                    tir.append(y)
                    tir.append(tir_x)
                    tir.append(tir_y)
                    #print(tir)
                    if x<520 or x>1000 or y<60 or y>540:
                        #print("Hors de la grille")
                        tir = tir_prec
                    try:
                        if tir[2]<0 or tir[3]<0:
                            #print("Valeurs Négatives")
                            tir = tir_prec
                            #print("Retry in the grid: ",tir)
                            #print(tir_prec)
                        else:
                            tir_prec = tir
                    except:
                        pass 
                   
                center_x = tir[2]*60+550
                center_y = tir[3]*60+90
                tir.append(center_x)
                tir.append(center_y)
                print("Tir : ",tir)
                
                if log_tir == []:
                    pass
                else:
                    if x<520 or x>1000 or y<60 or y>540:
                        pass
                    else:
                        for i in range(len(log_tir)):
                            #print(log_tir)
                            #print(tir[2], tir[3])
                            if ( log_tir[i][0] == tir[2] ) and ( log_tir[i][1] == tir[3] ):
                                check_tir_bateau = True
                                messagebox.showwarning("Attention !","Vous avez déjà tiré a cette endroit - Retirez")
                                break
                            else:
                                check_tir_bateau = False
        
                if check_tir_bateau == True:
                    pass
                else:
                    
                    ##----- Tir Sous-Marin -----##

                    
                    if case_ordi[tir[3]][tir[2]] == "S":                                                    #| Détection de si bateaux touchés, et lequel, et action en conséquence pour ré-interprétation graphique
                        if check_tir_sm == False:
                            dessin.create_line(tir[4]-30, tir[5]-30,  tir[4]+30,  tir[5]+30, fill = "red")
                            dessin.create_line(tir[4]-30, tir[5]+30,  tir[4]+30,  tir[5]-30, fill = "red")
                            save = [tir[4], tir[5]]
                            log_tir_sm.append(save)
                            save = [tir[2], tir[3]]
                            log_tir.append(save)
                            #print(log_tir_sm)
                            
                            if len(log_tir_sm) >= 3:
                                for i in range(3):
                                    dessin.create_line(log_tir_sm[i][0]-30, log_tir_sm[i][1]-30,  log_tir_sm[i][0]+30,  log_tir_sm[i][1]+30, fill = "black", width = 2)
                                    dessin.create_line(log_tir_sm[i][0]-30, log_tir_sm[i][1]+30,  log_tir_sm[i][0]+30,  log_tir_sm[i][1]-30, fill = "black", width =2)
                                    check_tir_sm = True
                                    end_game = end_game - 1
                        else:
                            messagebox.showwarning("Attention !","Vous avez déjà tiré a cette endroit - Retirez")
                    
                    ##----- Tir Porte-Avion -----##

                   
                    elif case_ordi[tir[3]][tir[2]] == "P":
                        if check_tir_pa == False:
                            dessin.create_line(tir[4]-30, tir[5]-30,  tir[4]+30,  tir[5]+30, fill = "red")
                            dessin.create_line(tir[4]-30, tir[5]+30,  tir[4]+30,  tir[5]-30, fill = "red")
                            save = [tir[4], tir[5]]
                            log_tir_pa.append(save)
                            save = [tir[2], tir[3]]
                            log_tir.append(save)
                            #print(log_tir_sm)
                            
                            if len(log_tir_pa) >= 8:
                                for i in range(8):
                                    dessin.create_line(log_tir_pa[i][0]-30, log_tir_pa[i][1]-30,  log_tir_pa[i][0]+30,  log_tir_pa[i][1]+30, fill = "black", width = 2)
                                    dessin.create_line(log_tir_pa[i][0]-30, log_tir_pa[i][1]+30,  log_tir_pa[i][0]+30,  log_tir_pa[i][1]-30, fill = "black", width = 2)
                                    check_tir_pa = True
                                    end_game = end_game - 1
                        else:
                            messagebox.showwarning("Attention !","Vous avez déjà tiré a cette endroit - Retirez")
                    
                    ##----- Tir Frégate -----##

                    elif case_ordi[tir[3]][tir[2]] == "F":
                        if check_tir_fg == False:
                            dessin.create_line(tir[4]-30, tir[5]-30,  tir[4]+30,  tir[5]+30, fill = "red")
                            dessin.create_line(tir[4]-30, tir[5]+30,  tir[4]+30,  tir[5]-30, fill = "red")
                            save = [tir[4], tir[5]]
                            log_tir_fg.append(save)
                            save = [tir[2], tir[3]]
                            log_tir.append(save)
                            #print(log_tir_sm)
                            
                            if len(log_tir_fg) >= 3:
                                for i in range(3):
                                    dessin.create_line(log_tir_fg[i][0]-30, log_tir_fg[i][1]-30,  log_tir_fg[i][0]+30,  log_tir_fg[i][1]+30, fill = "black", width = 2)
                                    dessin.create_line(log_tir_fg[i][0]-30, log_tir_fg[i][1]+30,  log_tir_fg[i][0]+30,  log_tir_fg[i][1]-30, fill = "black", width = 2)
                                    check_tir_fg = True
                                    end_game = end_game - 1
                        else:
                            messagebox.showwarning("Attention !","Vous avez déjà tiré a cette endroit - Retirez")
                    
                    ##----- Tir Torpilleur -----##
                    
                    elif case_ordi[tir[3]][tir[2]] == "T":
                        if check_tir_tp == False:
                            dessin.create_line(tir[4]-30, tir[5]-30,  tir[4]+30,  tir[5]+30, fill = "red")
                            dessin.create_line(tir[4]-30, tir[5]+30,  tir[4]+30,  tir[5]-30, fill = "red")
                            save = [tir[4], tir[5]]
                            log_tir_tp.append(save)
                            save = [tir[2], tir[3]]
                            log_tir.append(save)
                            #print(log_tir_sm)
                            
                            if len(log_tir_tp) >= 2:
                                for i in range(2):
                                    dessin.create_line(log_tir_tp[i][0]-30, log_tir_tp[i][1]-30,  log_tir_tp[i][0]+30,  log_tir_tp[i][1]+30, fill = "black", width = 2)
                                    dessin.create_line(log_tir_tp[i][0]-30, log_tir_tp[i][1]+30,  log_tir_tp[i][0]+30,  log_tir_tp[i][1]-30, fill = "black", width = 2)
                                    check_tir_tp = True
                                    end_game = end_game - 1
                        else:
                            messagebox.showwarning("Attention !","Vous avez déjà tiré a cette endroit - Retirez")
                    
                    else:
                        dessin.create_arc((tir[4]-30, tir[5]-30),(tir[4]+30, tir[5]+30),start=0, extent=180, style=ARC, outline = "blue")
                        dessin.create_arc((tir[4]-30, tir[5]-30),(tir[4]+30, tir[5]+30),start=180, extent=180, style=ARC, outline = "blue")
                        save = [tir[2], tir[3]]
                        log_tir.append(save)
            
                    tir_ordi()          #| Après notre tir on exécute cette fonction qui fait tirer l'ordinateur
            
            else:
                messagebox.showerror("Erreur !","Placez d'abord tout vos Bateaux pour jouer - Tricheur !")
        
        
        
    def tir_ordi(): # A FAIRE : debug sigmal, IA en file ou pile, ante cercle trigo
        
        global case_joueur
        global loose
        global log_tir_ordi
        global log_tir_ordi_sm
        global log_tir_ordi_fg
        global log_tir_ordi_pa
        global log_tir_ordi_tp
        global check_tir_ordi_sm
        global check_tir_ordi_fg
        global check_tir_ordi_pa
        global check_tir_ordi_tp
        global check_IA
        global tir_ordi1
        global tir_ordi2
        
        # tir_ordi1 = randint(0,7)
        # tir_ordi2 = randint(0,7)
        
        
        
        def reload_tir_IA():    #| Fonction de regénération de nombre aléatoire (x, y) de tir ordinateur
            global tir_ordi1
            global tir_ordi2
            
            tir_ordi1 = randint(0,7)
            tir_ordi2 = randint(0,7)
        
        reload_tir_IA()  
        
        #print("----- tir -----")
        #print(tir_ordi1)
        #print(tir_ordi2)

        save = []
        
        check_tir_ordi = True
        
        #print(check_IA)
        
        def check_ante_tir_ordi():                      #| Vérification que le tir n'a jamais été fait
            global check_tir_ordi
            global log_tir_ordi
            global tir_ordi1
            global tir_ordi2
            
            #print("----- log -------")
            #print(log_tir_ordi)
            #print(tir_ordi1)
            #print(tir_ordi2)
            
            for i in range(len(log_tir_ordi)):
                if ( log_tir_ordi[i][0] == tir_ordi1 ) and ( log_tir_ordi[i][1] == tir_ordi2 ):
                    reload_tir_IA()
                    check_ante_tir_ordi()
                    break
                else:
                    pass
        
        #| A ce niveau un tir jamais effectué a été validé
        
        if log_tir_ordi == []:
            pass
        else:
           check_ante_tir_ordi()
        
        tir_ordi1_backup = tir_ordi1                #| Pas d'utilité à cette back_up de fonction
        tir_ordi2_backup = tir_ordi2
                   
            
        center_tir_ordi1 = tir_ordi1*30+65          #| Calcul du centre du tir validé
        center_tir_ordi2 = tir_ordi2*30+75
        
        if case_joueur[tir_ordi2][tir_ordi1] == "S":        #| Même principe que pour notre tir, ici l'IA vérifie sur quoi il vient de tirer et agis en conséquence
            if check_tir_ordi_sm == False:
                
                dessin.create_line(center_tir_ordi1 - 15, center_tir_ordi2 + 15, center_tir_ordi1 + 15, center_tir_ordi2 - 15, fill = "red" )
                dessin.create_line(center_tir_ordi1 + 15, center_tir_ordi2 + 15, center_tir_ordi1 - 15, center_tir_ordi2 - 15, fill = "red" )
            
                save = [tir_ordi1, tir_ordi2, center_tir_ordi1, center_tir_ordi2]
                log_tir_ordi_sm.append(save)
                log_tir_ordi.append(save)
                check_IA = True
            
            if len(log_tir_ordi_sm) >= 3:
                for i in range(3):
                    dessin.create_line(log_tir_ordi_sm[i][2] - 15, log_tir_ordi_sm[i][3] + 15, log_tir_ordi_sm[i][2] + 15, log_tir_ordi_sm[i][3] - 15, fill = "black", width = 2 )
                    dessin.create_line(log_tir_ordi_sm[i][2] + 15, log_tir_ordi_sm[i][3] + 15, log_tir_ordi_sm[i][2] - 15, log_tir_ordi_sm[i][3] - 15, fill = "black", width = 2 )
                    check_tir_ordi_sm = True
                    loose = loose - 1

        elif case_joueur[tir_ordi2][tir_ordi1] == "F":
            if check_tir_ordi_fg == False:
                dessin.create_line(center_tir_ordi1 - 15, center_tir_ordi2 + 15, center_tir_ordi1 + 15, center_tir_ordi2 - 15, fill = "red" )
                dessin.create_line(center_tir_ordi1 + 15, center_tir_ordi2 + 15, center_tir_ordi1 - 15, center_tir_ordi2 - 15, fill = "red" )
            
                save = [tir_ordi1, tir_ordi2, center_tir_ordi1, center_tir_ordi2]
                log_tir_ordi_fg.append(save)
                log_tir_ordi.append(save)
                check_IA = True
            
            if len(log_tir_ordi_fg) >= 3:
                for i in range(3):
                    dessin.create_line(log_tir_ordi_fg[i][2] - 15, log_tir_ordi_fg[i][3] + 15, log_tir_ordi_fg[i][2] + 15, log_tir_ordi_fg[i][3] - 15, fill = "black", width = 2 )
                    dessin.create_line(log_tir_ordi_fg[i][2] + 15, log_tir_ordi_fg[i][3] + 15, log_tir_ordi_fg[i][2] - 15, log_tir_ordi_fg[i][3] - 15, fill = "black", width = 2 )
                    check_tir_ordi_fg = True
                    loose = loose - 1
                    
        elif case_joueur[tir_ordi2][tir_ordi1] == "P":
            if check_tir_ordi_pa == False:
                dessin.create_line(center_tir_ordi1 - 15, center_tir_ordi2 + 15, center_tir_ordi1 + 15, center_tir_ordi2 - 15, fill = "red" )
                dessin.create_line(center_tir_ordi1 + 15, center_tir_ordi2 + 15, center_tir_ordi1 - 15, center_tir_ordi2 - 15, fill = "red" )
            
                save = [tir_ordi1, tir_ordi2, center_tir_ordi1, center_tir_ordi2]
                log_tir_ordi_pa.append(save)
                log_tir_ordi.append(save)
                check_IA = True
            
            if len(log_tir_ordi_pa) >= 8:
                for i in range(8):
                    dessin.create_line(log_tir_ordi_pa[i][2] - 15, log_tir_ordi_pa[i][3] + 15, log_tir_ordi_pa[i][2] + 15, log_tir_ordi_pa[i][3] - 15, fill = "black", width = 2 )
                    dessin.create_line(log_tir_ordi_pa[i][2] + 15, log_tir_ordi_pa[i][3] + 15, log_tir_ordi_pa[i][2] - 15, log_tir_ordi_pa[i][3] - 15, fill = "black", width = 2 )
                    check_tir_ordi_pa = True
                    loose = loose - 1
            
        elif case_joueur[tir_ordi2][tir_ordi1] == "T":
            if check_tir_ordi_tp == False:
                dessin.create_line(center_tir_ordi1 - 15, center_tir_ordi2 + 15, center_tir_ordi1 + 15, center_tir_ordi2 - 15, fill = "red" )
                dessin.create_line(center_tir_ordi1 + 15, center_tir_ordi2 + 15, center_tir_ordi1 - 15, center_tir_ordi2 - 15, fill = "red" )
            
                save = [tir_ordi1, tir_ordi2, center_tir_ordi1, center_tir_ordi2]
                log_tir_ordi_tp.append(save)
                log_tir_ordi.append(save)
                check_IA = True
            
            if len(log_tir_ordi_tp) >= 2:
                for i in range(2):
                    dessin.create_line(log_tir_ordi_tp[i][2] - 15, log_tir_ordi_tp[i][3] + 15, log_tir_ordi_tp[i][2] + 15, log_tir_ordi_tp[i][3] - 15, fill = "black", width = 2 )
                    dessin.create_line(log_tir_ordi_tp[i][2] + 15, log_tir_ordi_tp[i][3] + 15, log_tir_ordi_tp[i][2] - 15, log_tir_ordi_tp[i][3] - 15, fill = "black", width = 2 )
                    check_tir_ordi_tp = True
                    loose = loose - 1
            
        else:
            dessin.create_arc((center_tir_ordi1-15, center_tir_ordi2-15),(center_tir_ordi1+15, center_tir_ordi2+15),start=0, extent=180, style=ARC, outline = "blue")
            dessin.create_arc((center_tir_ordi1-15, center_tir_ordi2-15),(center_tir_ordi1+15, center_tir_ordi2+15),start=180, extent=180, style=ARC, outline = "blue")
            save = [tir_ordi1, tir_ordi2, center_tir_ordi1, center_tir_ordi2]
            log_tir_ordi.append(save)
            
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#

 

    class Bateau:                                                       #| La classe qui défini tous les bateaux 
        """
        Ensemble des batiments de guerres, qui vont couler, ou pas
        """
        
        def __init__(self, rota, pos, case_joueur, case_ordi, longeur_case_joueur, longeur_case_ordi):  #| Son cnostructeur ( NB: Il n'y a pas de destructeur, caar les bateaux restent graphiquement qu'ils soient coulés ou pas )
            self.case_joueur = case_joueur
            self.case_ordi = case_ordi
            self.longeur_case_ordi = longeur_case_ordi
            self.longeur_case_joueur = longeur_case_joueur
            self.rota = rota
            self.pos = pos

        class SousMarin:                                                          #| La classe qui construit le sous-marin, plus précisément, cette classe contient toutes les foncotions liées au sous-marins, dont la fonction qui le construit
            """
            Le Shape du Sous-Marin
            """
            def __init__(self):
                global rota
                global pos
                global case_joueur
                global count_sm
                global start_game
                global check_pos
                                

            def build_SousMarin(self):                                              #| La dite fonction qui construit le sous-marin
                global count_sm                                                     #| Ce schéma class du bateau + def du bateau est répété pour tout les autres bateaux à l'identique, au différent de ce qui doit être changé comme les noms de variables ect
                global start_game
                global check_pos
                
                if count_sm == 1:
                    #print("Taille de rota:  ", len(rota))
                    if len(rota) == 1:
                        if pos[2] == 0 or pos[2] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]-1] == "P" or case_joueur[pos[3]][pos[2]-1] == "T" or case_joueur[pos[3]][pos[2]-1] == "F" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]+1] == "P" or case_joueur[pos[3]][pos[2]+1] == "T" or case_joueur[pos[3]][pos[2]+1] ==  "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
         
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-20, pos[5]-10,  pos[4]+30, pos[5]-10, fill='#0000FF')
                                dessin.create_arc((pos[4]+10, pos[5]-10),(pos[4]+40, pos[5]+10),start=270, extent=180,style=ARC, outline='#0000FF')
                                dessin.create_line(pos[4]-20, pos[5]+10,  pos[4]+30, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-20, pos[5]-10,  pos[4]-40, pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]-20, pos[5]+10,  pos[4]-40, pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]-40, pos[5]-10,  pos[4]-40, pos[5]+10, width=2, fill='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]-1] = "S"
                                case_joueur[pos[3]][pos[2]] = "S"
                                case_joueur[pos[3]][pos[2]+1] = "S"
                                count_sm = 0
                                start_game = start_game-1
                                bouton_sm_num['text'] = "0"
                                #print(case_joueur)
                        
                    if len(rota) == 2:
                        if pos[3] == 0 or pos[3] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]-1][pos[2]] == "P" or case_joueur[pos[3]-1][pos[2]] == "T" or case_joueur[pos[3]-1][pos[2]] == "F" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]+1][pos[2]] == "P" or case_joueur[pos[3]+1][pos[2]] == "T" or case_joueur[pos[3]+1][pos[2]] == "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-12,  pos[5]-20,  pos[4]-12, pos[5]+30, fill='#0000FF')
                                dessin.create_arc((pos[4]-12,  pos[5]+10),(pos[4]+10, pos[5]+40),start=180, extent=180, style=ARC, outline='#0000FF')
                                dessin.create_line(pos[4]+10,  pos[5]-20,  pos[4]+10, pos[5]+30, fill='#0000FF')
                                dessin.create_line(pos[4]-12,  pos[5]-20,  pos[4]-1,  pos[5]-40, fill='#0000FF')
                                dessin.create_line(pos[4]+10,  pos[5]-20,  pos[4],    pos[5]-40, fill='#0000FF')
                                dessin.create_line(pos[4]-12,  pos[5]-40,  pos[4]+10, pos[5]-40, width=2, fill='#0000FF')
                                
                                case_joueur[pos[3]-1][pos[2]] = "S"
                                case_joueur[pos[3]][pos[2]] = "S"
                                case_joueur[pos[3]+1][pos[2]] = "S"
                                count_sm = 0
                                start_game = start_game-1
                                bouton_sm_num['text'] = "0"
                                #print(case_joueur)
                        
                    if len(rota) == 3:
                        if pos[2] == 0 or pos[2] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]-1] == "P" or case_joueur[pos[3]][pos[2]-1] == "T" or case_joueur[pos[3]][pos[2]-1] == "F" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]+1] == "P" or case_joueur[pos[3]][pos[2]+1] == "T" or case_joueur[pos[3]][pos[2]+1] == "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]+22, pos[5]-10,  pos[4]-32, pos[5]-10, fill='#0000FF')
                                dessin.create_arc((pos[4]-42, pos[5]-10),(pos[4]-12, pos[5]+10), start=90, extent=180, style=ARC, outline='#0000FF')
                                dessin.create_line(pos[4]+22, pos[5]+10,  pos[4]-32, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+22, pos[5]-10,  pos[4]+42, pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]+22, pos[5]+10,  pos[4]+42, pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]+42, pos[5]-10,  pos[4]+42, pos[5]+10, width=2, fill='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]-1] = "S"
                                case_joueur[pos[3]][pos[2]] = "S"
                                case_joueur[pos[3]][pos[2]+1] = "S"
                                count_sm = 0
                                start_game = start_game-1
                                bouton_sm_num['text'] = "0"
                                #print(case_joueur)
                            
                    if len(rota) == 4:
                        if pos[3] == 0 or pos[3] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]-1][pos[2]] == "P" or case_joueur[pos[3]-1][pos[2]] == "T" or case_joueur[pos[3]-1][pos[2]] == "F" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]+1][pos[2]] == "P" or case_joueur[pos[3]+1][pos[2]] == "T" or case_joueur[pos[3]+1][pos[2]] == "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-10, pos[5]-28,  pos[4]-10, pos[5]+22, fill='#0000FF')
                                dessin.create_arc((pos[4]-10, pos[5]-43),(pos[4]+12, pos[5]+12), start=0, extent=180, style=ARC, outline='#0000FF')
                                dessin.create_line(pos[4]+12, pos[5]-28,  pos[4]+12, pos[5]+22, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]+22,  pos[4],    pos[5]+42, fill='#0000FF')
                                dessin.create_line(pos[4]+12, pos[5]+22,  pos[4]+2,  pos[5]+42, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]+42,  pos[4]+12, pos[5]+42, width=2, fill='#0000FF')
                                
                                case_joueur[pos[3]-1][pos[2]] = "S"
                                case_joueur[pos[3]][pos[2]] = "S"
                                case_joueur[pos[3]+1][pos[2]] = "S"
                                count_sm = 0
                                start_game = start_game-1
                                bouton_sm_num['text'] = "0"
                                #print(case_joueur)
                                
                else:
                    messagebox.showerror("Erreur !","Vous avez déjà placé ce Bateau.")
                    pass
            
            def build_PorteAvion(self):
                global count_pa
                global start_game
                
                if count_pa == 1:
                    #print("Taille de rota:  ", len(rota))
                    if len(rota) == 1:
                        if pos[3] == 0 or pos[2] >= 5:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]+1] == "S" or case_joueur[pos[3]][pos[2]+1] == "T" or case_joueur[pos[3]][pos[2]+1] == "F" or case_joueur[pos[3]][pos[2]+2] == "S" or case_joueur[pos[3]][pos[2]+2] == "T" or case_joueur[pos[3]][pos[2]+2] == "F" or case_joueur[pos[3]][pos[2]+3] == "S" or case_joueur[pos[3]][pos[2]+3] == "T" or case_joueur[pos[3]][pos[2]+3] == "F" or case_joueur[pos[3]-1][pos[2]] == "S" or case_joueur[pos[3]-1][pos[2]] == "T" or case_joueur[pos[3]-1][pos[2]] == "F" or case_joueur[pos[3]-1][pos[2]+1] == "S" or case_joueur[pos[3]-1][pos[2]+1] == "T" or case_joueur[pos[3]-1][pos[2]+1] == "F" or case_joueur[pos[3]-1][pos[2]+2] == "S" or case_joueur[pos[3]-1][pos[2]+2] == "T" or case_joueur[pos[3]-1][pos[2]+2] == "F" or case_joueur[pos[3]-1][pos[2]+3] == "S" or case_joueur[pos[3]-1][pos[2]+3] == "T" or case_joueur[pos[3]-1][pos[2]+3] == "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
        
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-5,  pos[5]-40,  pos[4]+80,  pos[5]-40, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]+10,  pos[4]+40,  pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+83, pos[5]+10,  pos[4]+100, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+100,pos[5]+10,  pos[4]+100, pos[5]-9,  fill='#0000FF')
                                dessin.create_line(pos[4]+100,pos[5]-9,   pos[4]+85,  pos[5]-9,  fill='#0000FF')
                                dessin.create_line(pos[4]+80, pos[5]-40,  pos[4]+85,  pos[5]-9,  fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]-40,  pos[4]-10,  pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+25, pos[5]-35,  pos[4]+65,  pos[5]-35, fill='#0000FF')
                                dessin.create_line(pos[4]+25, pos[5]-20,  pos[4]+65,  pos[5]-20, fill='#0000FF')
                                dessin.create_line(pos[4]+25, pos[5]-35,  pos[4]+25,  pos[5]-20, fill='#0000FF')
                                dessin.create_line(pos[4]+65, pos[5]-35,  pos[4]+65,  pos[5]-20, fill='#0000FF')
                                dessin.create_line(pos[4],    pos[5]-10,  pos[4]+85,  pos[5],    fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+5,   pos[4]+80,  pos[5]+15, fill='#0000FF')
                                dessin.create_line(pos[4],    pos[5]-15,  pos[4]-5,   pos[5]+5,  fill='#0000FF')
                                dessin.create_line(pos[4]+85, pos[5],     pos[4]+80,  pos[5]+15, fill='#0000FF')
                                dessin.create_line(pos[4]+35, pos[5]-28,  pos[4]+40,  pos[5]-28, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]+45, pos[5]-28,  pos[4]+50,  pos[5]-28, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]+20, pos[5]-28,  pos[4]+15,  pos[5]-28, width = 3, fill='#0000FF')
                                             
                                case_joueur[pos[3]][pos[2]] = "P"
                                case_joueur[pos[3]][pos[2]+1] = "P"
                                case_joueur[pos[3]][pos[2]+2] = "P"
                                case_joueur[pos[3]][pos[2]+3] = "P"
                                case_joueur[pos[3]-1][pos[2]] = "P"
                                case_joueur[pos[3]-1][pos[2]+1] = "P"
                                case_joueur[pos[3]-1][pos[2]+2] = "P"
                                case_joueur[pos[3]-1][pos[2]+3] = "P"
                                count_pa = 0
                                start_game = start_game-1
                                bouton_pa_num['text'] = "0"
                                #print(case_joueur)
                            
                            
                            
      
                    if len(rota) == 2:
                        if pos[2] == 7 or pos[3] >= 5:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]+1] == "S" or case_joueur[pos[3]][pos[2]+1] == "T" or case_joueur[pos[3]][pos[2]+1] == "F" or case_joueur[pos[3]+1][pos[2]+1] == "S" or case_joueur[pos[3]+1][pos[2]+1] == "T" or case_joueur[pos[3]+1][pos[2]+1] == "F" or case_joueur[pos[3]+2][pos[2]+1] == "S" or case_joueur[pos[3]+2][pos[2]+1] == "T" or case_joueur[pos[3]+2][pos[2]+1] == "F" or case_joueur[pos[3]+3][pos[2]+1] == "S" or case_joueur[pos[3]+3][pos[2]+1] == "T" or case_joueur[pos[3]+3][pos[2]+1] == "F" or case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]+1][pos[2]] == "S" or case_joueur[pos[3]+1][pos[2]] == "T" or case_joueur[pos[3]+1][pos[2]] == "F" or case_joueur[pos[3]+2][pos[2]] == "S" or case_joueur[pos[3]+2][pos[2]] == "T" or case_joueur[pos[3]+2][pos[2]] == "F" or case_joueur[pos[3]+3][pos[2]] == "S" or case_joueur[pos[3]+3][pos[2]] == "T" or case_joueur[pos[3]+3][pos[2]] == "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-10, pos[5]-5,   pos[4]-10,  pos[5]+80, fill='#0000FF')
                                dessin.create_line(pos[4]+40, pos[5]-10,  pos[4]+40,  pos[5]+40, fill='#0000FF')
                                dessin.create_line(pos[4]+40, pos[5]+83,  pos[4]+40,  pos[5]+100, fill='#0000FF')
                                dessin.create_line(pos[4]+40, pos[5]+100, pos[4]+21,  pos[5]+100,  fill='#0000FF')
                                dessin.create_line(pos[4]+21, pos[5]+100, pos[4]+21,  pos[5]+85,  fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]+80,  pos[4]+21,  pos[5]+85,  fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]-5,   pos[4]+40,  pos[5]-10, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+25,  pos[4]-5,   pos[5]+65, fill='#0000FF')
                                dessin.create_line(pos[4]+10, pos[5]+25,  pos[4]+10,  pos[5]+65, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+25,  pos[4]+10,  pos[5]+25, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+65,  pos[4]+10,  pos[5]+65, fill='#0000FF')
                                dessin.create_line(pos[4]+20, pos[5],     pos[4]+30,  pos[5]+85,    fill='#0000FF')
                                dessin.create_line(pos[4]+35, pos[5]-5,   pos[4]+45,  pos[5]+80, fill='#0000FF')
                                dessin.create_line(pos[4]+15, pos[5],     pos[4]+35,  pos[5]-5,  fill='#0000FF')
                                dessin.create_line(pos[4]+30, pos[5]+85,  pos[4]+45,  pos[5]+80, fill='#0000FF')
                                dessin.create_line(pos[4]+2,  pos[5]+35,  pos[4]+2,   pos[5]+40, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]+2,  pos[5]+45,  pos[4]+2,   pos[5]+50, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]+2,  pos[5]+20,  pos[4]+2,   pos[5]+15, width = 3, fill='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]+1] = "P"
                                case_joueur[pos[3]+1][pos[2]+1] = "P"
                                case_joueur[pos[3]+2][pos[2]+1] = "P"
                                case_joueur[pos[3]+3][pos[2]+1] = "P"
                                case_joueur[pos[3]][pos[2]] = "P"
                                case_joueur[pos[3]+1][pos[2]] = "P"
                                case_joueur[pos[3]+2][pos[2]] = "P"
                                case_joueur[pos[3]+3][pos[2]] = "P"
                                count_pa = 0
                                start_game = start_game-1
                                bouton_pa_num['text'] = "0"
                                #print(case_joueur)
                            
                    if len(rota) == 3:
                        if pos[2] <= 2 or pos[3] == 0:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]-1] == "S" or case_joueur[pos[3]][pos[2]-1] == "T" or case_joueur[pos[3]][pos[2]-1] == "F" or case_joueur[pos[3]][pos[2]-2] == "S" or case_joueur[pos[3]][pos[2]-2] == "T" or case_joueur[pos[3]][pos[2]-2] == "F" or case_joueur[pos[3]][pos[2]-3] == "S" or case_joueur[pos[3]][pos[2]-3] == "T" or case_joueur[pos[3]][pos[2]-3] == "F" or case_joueur[pos[3]-1][pos[2]] == "S" or case_joueur[pos[3]-1][pos[2]] == "T" or case_joueur[pos[3]-1][pos[2]] == "F" or case_joueur[pos[3]-1][pos[2]-1] == "S" or case_joueur[pos[3]-1][pos[2]-1] == "T" or case_joueur[pos[3]-1][pos[2]-1] == "F" or case_joueur[pos[3]-1][pos[2]-2] == "S" or case_joueur[pos[3]-1][pos[2]-2] == "T" or case_joueur[pos[3]-1][pos[2]-2] == "F" or case_joueur[pos[3]-1][pos[2]-3] == "S" or case_joueur[pos[3]-1][pos[2]-3] == "T" or case_joueur[pos[3]-1][pos[2]-3] == "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
        
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]+5,  pos[5]-40,  pos[4]-80, pos[5]-40, fill='#0000FF')
                                dessin.create_line(pos[4]+10, pos[5]+10,  pos[4]-40, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-73, pos[5]+10,  pos[4]-100,pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-100,pos[5]+10,  pos[4]-100,pos[5]-9,  fill='#0000FF')
                                dessin.create_line(pos[4]-100,pos[5]-9,   pos[4]-85, pos[5]-9,  fill='#0000FF')
                                dessin.create_line(pos[4]-80, pos[5]-40,  pos[4]-85, pos[5]-9,  fill='#0000FF')
                                dessin.create_line(pos[4]+5,  pos[5]-40,  pos[4]+10, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-15, pos[5]-35,  pos[4]-55, pos[5]-35, fill='#0000FF')
                                dessin.create_line(pos[4]-15, pos[5]-20,  pos[4]-55, pos[5]-20, fill='#0000FF')
                                dessin.create_line(pos[4]-15, pos[5]-35,  pos[4]-15, pos[5]-20, fill='#0000FF')
                                dessin.create_line(pos[4]-55, pos[5]-35,  pos[4]-55, pos[5]-20, fill='#0000FF')
                                dessin.create_line(pos[4],    pos[5]-10,  pos[4]-75, pos[5],    fill='#0000FF')
                                dessin.create_line(pos[4]+5,  pos[5]+5,   pos[4]-70, pos[5]+15, fill='#0000FF')
                                dessin.create_line(pos[4],    pos[5]-10,  pos[4]+5,  pos[5]+5,  fill='#0000FF')
                                dessin.create_line(pos[4]-75, pos[5],     pos[4]-70, pos[5]+15, fill='#0000FF')
                                dessin.create_line(pos[4]-25, pos[5]-28,  pos[4]-30, pos[5]-28, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]-35, pos[5]-28,  pos[4]-40, pos[5]-28, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]-28,  pos[4]-5,  pos[5]-28, width = 3, fill='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]] = "P"
                                case_joueur[pos[3]][pos[2]-1] = "P"
                                case_joueur[pos[3]][pos[2]-2] = "P"
                                case_joueur[pos[3]][pos[2]-3] = "P"
                                case_joueur[pos[3]-1][pos[2]] = "P"
                                case_joueur[pos[3]-1][pos[2]-1] = "P"
                                case_joueur[pos[3]-1][pos[2]-2] = "P"
                                case_joueur[pos[3]-1][pos[2]-3] = "P"
                                count_pa = 0
                                start_game = start_game-1
                                bouton_pa_num['text'] = "0"
                                #print(case_joueur)
                        
                    if len(rota) == 4:
                        if pos[2] == 7 or pos[3] <= 2:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]-1][pos[2]] == "S" or case_joueur[pos[3]-1][pos[2]] == "T" or case_joueur[pos[3]-1][pos[2]] == "F" or case_joueur[pos[3]-2][pos[2]] == "S" or case_joueur[pos[3]-2][pos[2]] == "T" or case_joueur[pos[3]-2][pos[2]] == "F" or case_joueur[pos[3]-3][pos[2]] == "S" or case_joueur[pos[3]-3][pos[2]] == "T" or case_joueur[pos[3]-3][pos[2]] == "F" or case_joueur[pos[3]][pos[2]+1] == "S" or case_joueur[pos[3]][pos[2]+1] == "T" or case_joueur[pos[3]][pos[2]+1] == "F" or case_joueur[pos[3]-1][pos[2]+1] == "S" or case_joueur[pos[3]-1][pos[2]+1] == "T" or case_joueur[pos[3]-1][pos[2]+1] == "F" or case_joueur[pos[3]-2][pos[2]+1] == "S" or case_joueur[pos[3]-2][pos[2]+1] == "T" or case_joueur[pos[3]-2][pos[2]+1] == "F" or case_joueur[pos[3]-3][pos[2]+1] == "S" or case_joueur[pos[3]-3][pos[2]+1] == "T" or case_joueur[pos[3]-3][pos[2]+1] == "F":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
        
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-10, pos[5]+5,   pos[4]-10,  pos[5]-80, fill='#0000FF')
                                dessin.create_line(pos[4]+40, pos[5]+10,  pos[4]+40,  pos[5]-30, fill='#0000FF')
                                dessin.create_line(pos[4]+40, pos[5]-83,  pos[4]+40,  pos[5]-100,fill='#0000FF')
                                dessin.create_line(pos[4]+40, pos[5]-100, pos[4]+21,  pos[5]-100,fill='#0000FF')
                                dessin.create_line(pos[4]+21, pos[5]-100, pos[4]+21,  pos[5]-85, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]-80,  pos[4]+21,  pos[5]-85, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]+5,   pos[4]+40,  pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]-25,  pos[4]-5,   pos[5]-65, fill='#0000FF')
                                dessin.create_line(pos[4]+10, pos[5]-25,  pos[4]+10,  pos[5]-65, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]-25,  pos[4]+10,  pos[5]-25, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]-65,  pos[4]+10,  pos[5]-65, fill='#0000FF')
                                dessin.create_line(pos[4]+20, pos[5],     pos[4]+30,  pos[5]-85, fill='#0000FF')
                                dessin.create_line(pos[4]+35, pos[5]+5,   pos[4]+45,  pos[5]-80, fill='#0000FF')
                                dessin.create_line(pos[4]+20, pos[5],     pos[4]+35,  pos[5]+5,  fill='#0000FF')
                                dessin.create_line(pos[4]+30, pos[5]-85,  pos[4]+45,  pos[5]-80, fill='#0000FF')
                                dessin.create_line(pos[4]+2,  pos[5]-35,  pos[4]+2,   pos[5]-40, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]+2,  pos[5]-45,  pos[4]+2,   pos[5]-50, width = 5, fill='#0000FF')
                                dessin.create_line(pos[4]+2,  pos[5]-20,  pos[4]+2,   pos[5]-15, width = 3, fill='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]] = "P"
                                case_joueur[pos[3]-1][pos[2]] = "P"
                                case_joueur[pos[3]-2][pos[2]] = "P"
                                case_joueur[pos[3]-3][pos[2]] = "P"
                                case_joueur[pos[3]][pos[2]+1] = "P"
                                case_joueur[pos[3]-1][pos[2]+1] = "P"
                                case_joueur[pos[3]-2][pos[2]+1] = "P"
                                case_joueur[pos[3]-3][pos[2]+1] = "P"
                                count_pa = 0
                                start_game = start_game-1
                                bouton_pa_num['text'] = "0"
                                #print(case_joueur)
                            
                            
                else:
                    messagebox.showerror("Erreur !","Vous avez déjà placé ce Bateau.")
                    pass
                
            def build_Fregate(self):
                global count_fg
                global start_game
                global check_pos
                
                if count_fg == 1:
                    #print("Taille de rota:  ", len(rota))
                    if len(rota) == 1:
                        if pos[2] == 0 or pos[2] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]-1] == "S" or case_joueur[pos[3]][pos[2]-1] == "T" or case_joueur[pos[3]][pos[2]-1] == "P" or case_joueur[pos[3]][pos[2]] == "S" or  case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]+1] == "S" or case_joueur[pos[3]][pos[2]+1] == "T" or case_joueur[pos[3]][pos[2]+1] == "P":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos = False
                                print("enter")
                                
                            print(case_joueur[pos[3]][pos[2]-1])
                            print(case_joueur[pos[3]][pos[2]])
                            print(case_joueur[pos[3]][pos[2]+1])
                            print(check_pos)

                            if check_pos == True:
                                dessin.create_arc((pos[4]-120, pos[5]-10),(pos[4]+40,  pos[5]+10), start=0, extent=90, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-120, pos[5]+10),(pos[4]+40,  pos[5]-10), start=0, extent=-90, style=ARC, outline ='#0000FF')
                                dessin.create_line(pos[4]-40,  pos[5]-10,  pos[4]-40,  pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-20,  pos[5]-5,   pos[4]+10,  pos[5]-5, fill='#0000FF')
                                dessin.create_line(pos[4]-20,  pos[5]+5,   pos[4]+10,  pos[5]+5, fill='#0000FF')
                                dessin.create_line(pos[4]+10,  pos[5]+5,   pos[4]+20,  pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]+10,  pos[5]-5,   pos[4]+20,  pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]-20,  pos[5]-5,   pos[4]-20,  pos[5]+5, fill='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]-1] = "F"
                                case_joueur[pos[3]][pos[2]] = "F"
                                case_joueur[pos[3]][pos[2]+1] = "F"
                                count_fg = 0
                                start_game = start_game-1
                                bouton_fg_num['text'] = "0"
                                #print(case_joueur)
                                
                        
                    if len(rota) == 2:
                        if pos[3] == 0 or pos[3] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]-1][pos[2]] == "P" or case_joueur[pos[3]-1][pos[2]] == "T" or case_joueur[pos[3]-1][pos[2]] == "S" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]+1][pos[2]] == "P" or case_joueur[pos[3]+1][pos[2]] == "T" or case_joueur[pos[3]+1][pos[2]] == "S":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_arc((pos[4]-10, pos[5]-120),(pos[4]+10,pos[5]+40), start=180, extent=90, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]+10, pos[5]-120),(pos[4]-10,pos[5]+40), start=0, extent=-90, style=ARC, outline ='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]-40,   pos[4]+10,pos[5]-40, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]-20,   pos[4]-5, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+5,  pos[5]-20,   pos[4]+5, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+5,  pos[5]+10,   pos[4],   pos[5]+20, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+10,   pos[4],   pos[5]+20, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]-20,   pos[4]+5, pos[5]-20, fill='#0000FF')
                                
                                case_joueur[pos[3]-1][pos[2]] = "F"
                                case_joueur[pos[3]][pos[2]] = "F"
                                case_joueur[pos[3]+1][pos[2]] = "F"
                                count_fg = 0
                                start_game = start_game-1
                                bouton_fg_num['text'] = "0"
                                #print(case_joueur)
                        
                    if len(rota) == 3:
                        if pos[2] == 0 or pos[2] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]-1] == "P" or case_joueur[pos[3]][pos[2]-1] == "T" or case_joueur[pos[3]][pos[2]-1] == "S" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]][pos[2]+1] == "P" or case_joueur[pos[3]][pos[2]+1] == "T" or case_joueur[pos[3]][pos[2]+1] == "S":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_arc((pos[4]-40,  pos[5]-10),(pos[4]+120, pos[5]+10), start=180, extent=90, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-40,  pos[5]+10),(pos[4]+120, pos[5]-10), start=180, extent=-90, style=ARC, outline ='#0000FF')
                                dessin.create_line(pos[4]+40,  pos[5]-10,  pos[4]+40,  pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4],     pos[5]-5,   pos[4]+30,  pos[5]-5, fill='#0000FF')
                                dessin.create_line(pos[4],     pos[5]+5,   pos[4]+30,  pos[5]+5, fill='#0000FF')
                                dessin.create_line(pos[4],     pos[5]+5,   pos[4]-10,  pos[5], fill='#0000FF')
                                dessin.create_line(pos[4],     pos[5]-5,   pos[4]-10,  pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]+30,  pos[5]-5,   pos[4]+30,  pos[5]+5, fill='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]-1] = "F"
                                case_joueur[pos[3]][pos[2]] = "F"
                                case_joueur[pos[3]][pos[2]+1] = "F"
                                count_fg = 0
                                start_game = start_game-1
                                bouton_fg_num['text'] = "0"
                                #print(case_joueur)
                            
                    if len(rota) == 4:
                        if pos[3] == 0 or pos[3] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]-1][pos[2]] == "P" or case_joueur[pos[3]-1][pos[2]] == "T" or case_joueur[pos[3]-1][pos[2]] == "S" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "T" or case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]+1][pos[2]] == "P" or case_joueur[pos[3]+1][pos[2]] == "T" or case_joueur[pos[3]+1][pos[2]] == "S":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_arc((pos[4]-10, pos[5]-38),(pos[4]+10,pos[5]+122), start=90, extent=90, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]+10, pos[5]-38),(pos[4]-10,pos[5]+122), start=180, extent=-180, style=ARC, outline ='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]+42,  pos[4]+10,pos[5]+42, fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+2,   pos[4]-5, pos[5]+32, fill='#0000FF')
                                dessin.create_line(pos[4]+5,  pos[5]+2,   pos[4]+5, pos[5]+32, fill='#0000FF')
                                dessin.create_line(pos[4]+5,  pos[5]+2,   pos[4],   pos[5]-8,  fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+2,   pos[4],   pos[5]-8,  fill='#0000FF')
                                dessin.create_line(pos[4]-5,  pos[5]+32,  pos[4]+5, pos[5]+32, fill='#0000FF')
                                
                                case_joueur[pos[3]-1][pos[2]] = "F"
                                case_joueur[pos[3]][pos[2]] = "F"
                                case_joueur[pos[3]+1][pos[2]] = "F"
                                count_fg = 0
                                start_game = start_game-1
                                bouton_fg_num['text'] = "0"
                                #print(case_joueur)
                                
                else:
                    messagebox.showerror("Erreur !","Vous avez déjà placé ce Bateau.")
                    pass
            
            def build_Torpilleur(self):
                global count_tp
                global start_game
                global check_pos
                
                if count_tp == 1:
                    #print("Taille de rota:  ", len(rota))
                    if len(rota) == 1:
                        if pos[2] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]+1] == "S" or  case_joueur[pos[3]][pos[2]+1] == "F" or case_joueur[pos[3]][pos[2]+1] == "P":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos = False

                            if check_pos == True:
                                dessin.create_line(pos[4]-12,  pos[5]-10,  pos[4]+38,  pos[5]-10, fill='#0000FF')
                                dessin.create_line(pos[4]-12,  pos[5]+10,  pos[4]+38,  pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-12,  pos[5]-10,  pos[4]-12,  pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+38,  pos[5]-10,  pos[4]+43,  pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]+38,  pos[5]+10,  pos[4]+43,  pos[5], fill='#0000FF')
                                dessin.create_arc((pos[4]-2,  pos[5]-5), (pos[4]+13,   pos[5]+5), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-2,  pos[5]-5), (pos[4]+13,   pos[5]+5), start=180, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]+18,  pos[5]-2), (pos[4]+28,  pos[5]+2), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]+18,  pos[5]-2), (pos[4]+28,  pos[5]+2), start=180, extent=180, style=ARC, outline ='#0000FF')

                                case_joueur[pos[3]][pos[2]] = "T"
                                case_joueur[pos[3]][pos[2]+1] = "T"
                                count_tp = 0
                                start_game = start_game-1
                                bouton_tp_num['text'] = "0"
                                #print(case_joueur)
                                
                        
                    if len(rota) == 2:
                        if pos[3] == 7:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]+1][pos[2]] == "P" or case_joueur[pos[3]+1][pos[2]] == "F" or case_joueur[pos[3]+1][pos[2]] == "S":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-10,  pos[5]-10,  pos[4]-10,  pos[5]+40, fill='#0000FF')
                                dessin.create_line(pos[4]+10,  pos[5]-10,  pos[4]+10,  pos[5]+40, fill='#0000FF')
                                dessin.create_line(pos[4]-10,  pos[5]-10,  pos[4]+10,  pos[5]-10, fill='#0000FF')
                                dessin.create_line(pos[4]-10,  pos[5]+40,  pos[4],     pos[5]+45, fill='#0000FF')
                                dessin.create_line(pos[4]+10,  pos[5]+40,  pos[4],     pos[5]+45, fill='#0000FF')
                                dessin.create_arc((pos[4]-5,   pos[5]-00),(pos[4]+5,   pos[5]+15), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-5,   pos[5]),   (pos[4]+5,   pos[5]+15), start=180, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-2,   pos[5]+20),(pos[4]+2,   pos[5]+30), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-2,   pos[5]+20),(pos[4]+2,   pos[5]+30), start=180, extent=180, style=ARC, outline ='#0000FF')

                                case_joueur[pos[3]][pos[2]] = "T"
                                case_joueur[pos[3]+1][pos[2]] = "T"
                                count_tp = 0
                                start_game = start_game-1
                                bouton_tp_num['text'] = "0"
                                #print(case_joueur)
                        
                    if len(rota) == 3:
                        if pos[2] == 0:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]][pos[2]-1] == "P" or case_joueur[pos[3]][pos[2]-1] == "F" or case_joueur[pos[3]][pos[2]-1] == "S":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-38, pos[5]-10,  pos[4]+12, pos[5]-10, fill='#0000FF')
                                dessin.create_line(pos[4]-38, pos[5]+10,  pos[4]+12, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]+12, pos[5]-10,  pos[4]+12, pos[5]+10, fill='#0000FF')
                                dessin.create_line(pos[4]-38, pos[5]-10,  pos[4]-43, pos[5], fill='#0000FF')
                                dessin.create_line(pos[4]-38, pos[5]+10,  pos[4]-43, pos[5], fill='#0000FF')
                                dessin.create_arc((pos[4]-8,  pos[5]-5), (pos[4]+7,  pos[5]+5), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-8,  pos[5]-5), (pos[4]+7,  pos[5]+5), start=180, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-28, pos[5]-2), (pos[4]-18, pos[5]+2), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-28, pos[5]-2), (pos[4]-18, pos[5]+2), start=180, extent=180, style=ARC, outline ='#0000FF')
                                
                                case_joueur[pos[3]][pos[2]] = "T"
                                case_joueur[pos[3]][pos[2]-1] = "T"
                                count_tp = 0
                                start_game = start_game-1
                                bouton_tp_num['text'] = "0"
                                #print(case_joueur)
                            
                    if len(rota) == 4:
                        if pos[3] == 0:
                            messagebox.showerror("Erreur !","Le Bateau sort de la grille, repositionnez le.")
                            pass
                        else:
                            check_pos = True
                            if case_joueur[pos[3]][pos[2]] == "P" or case_joueur[pos[3]][pos[2]] == "F" or case_joueur[pos[3]][pos[2]] == "S" or case_joueur[pos[3]-1][pos[2]] == "P" or case_joueur[pos[3]-1][pos[2]] == "F" or case_joueur[pos[3]-1][pos[2]] == "S":
                                messagebox.showerror("Erreur !","Le Bateau superpose un autre Bateau, repositionnez le.")
                                check_pos  = False
                            
                            if check_pos == False:
                                pass
                            else:
                                dessin.create_line(pos[4]-10, pos[5]-37, pos[4]-10, pos[5]+13, fill='#0000FF')
                                dessin.create_line(pos[4]+10, pos[5]-37, pos[4]+10, pos[5]+13, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]+13, pos[4]+10, pos[5]+13, fill='#0000FF')
                                dessin.create_line(pos[4]-10, pos[5]-37, pos[4],    pos[5]-42, fill='#0000FF')
                                dessin.create_line(pos[4]+10, pos[5]-37, pos[4],    pos[5]-42, fill='#0000FF')
                                dessin.create_arc((pos[4]-5,  pos[5]-12),(pos[4]+5,  pos[5]+3), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-5,  pos[5]-12),(pos[4]+5,  pos[5]+3), start=180, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-2,  pos[5]-27),(pos[4]+2, pos[5]-17), start=0, extent=180, style=ARC, outline ='#0000FF')
                                dessin.create_arc((pos[4]-2,  pos[5]-27),(pos[4]+2, pos[5]-17), start=180, extent=180, style=ARC, outline ='#0000FF')

                                case_joueur[pos[3]][pos[2]] = "T"
                                case_joueur[pos[3]-1][pos[2]] = "T"
                                count_tp = 0
                                start_game = start_game-1
                                bouton_tp_num['text'] = "0"
                                #print(case_joueur)
                                
                else:
                    messagebox.showerror("Erreur !","Vous avez déjà placé ce Bateau.")
                    pass
            

                
                    

    ##----- Création des boutons -----##
    sm = Bateau(rota, pos, case_joueur, case_ordi, longeur_case_joueur, longeur_case_ordi).SousMarin()         #| Activiation des fonctions de construction

    bouton_quitter = Button(fen, text='Quitter', command = fen.destroy)                                     #| Ecriture de tous les boutons
    bouton_quitter.grid(row = 1, column = 2, sticky = E+W , padx=3, pady=3)
    
    bouton_quitter = Button(fen, text='Rejouer', command = main)
    bouton_quitter.grid(row = 1, column = 1, sticky = E+W , padx=3, pady=3)

    bouton_replay = Button(fen, text='Menu', command = menu)
    bouton_replay.grid(row = 1, column = 0, sticky = E+W , padx=3, pady=3)

    bouton_sm = Button(fen, text='Sous-Marin', command = sm.build_SousMarin)
    bouton_sm.place(x = 1100, y = 50)
    bouton_sm_num = Button(fen, text='1', state = DISABLED, width = 1)
    bouton_sm_num.place(x = 1080, y = 50)
    
    bouton_pa = Button(fen, text='Porte-Avion', command = sm.build_PorteAvion)
    bouton_pa.place(x = 1100, y = 80)
    bouton_pa_num = Button(fen, text='1', state = DISABLED, width = 1)
    bouton_pa_num.place(x = 1080, y = 80)
    
    bouton_tp = Button(fen, text='Torpilleur', command = sm.build_Torpilleur)
    bouton_tp.place(x = 1100, y = 110)
    bouton_tp_num = Button(fen, text='1', state = DISABLED, width = 1)
    bouton_tp_num.place(x = 1080, y = 110)
    
    bouton_fg = Button(fen, text='Frégate', command = sm.build_Fregate)
    bouton_fg.place(x = 1100, y = 140)
    bouton_fg_num = Button(fen, text='1', state = DISABLED, width = 1)
    bouton_fg_num.place(x = 1080, y = 140)

    ##----- Affichage de Rotation -----##
    
    bouton_rota = Button(fen, text='🢂', state = DISABLED)
    bouton_rota.place(x = 1100, y = 400)
    dessin.create_text(1070, 405, font=('Centaur', 15, "bold"), text='Sens : ', fill = "black")


    ##----- Création des binds -----##

    fen.bind('<r>',rotation)                                    #| Ecriture des évènements déclancheur des instance graphique ( autrement dit, des boutons paarce que pour jouer c'est mieux avec des boutons )
    fen.bind('<ButtonPress-1>', motion_joueur)
    fen.bind('<ButtonPress-3>', tir)



    
    fen.mainloop()
    
    
    
def menu():                             #| La fenêtre du menus
    global fen_active
    global count_sm
    
    try:
        fen_active.destroy()            #| Fenêtre active, sa desctruction et application de la nouvelle fenêtre active
    except:
        pass
    
    
    fen2 = Tk()
    fen2.title('Bataille Navale')
    fen2.iconbitmap("anchor.ico")
    
    fond = (Image.open("menu_bg3.png"))
    resized_image = fond.resize((1200,700), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    
    dessin2 = Canvas(fen2, width = 1200, height = 700)
    dessin2.grid(row = 0, column = 0, columnspan=3, padx=3, pady=3)
    dessin2.pack(fill ="both")
    dessin2.create_image(0, 0, image = new_image , anchor ="nw")
    dessin2.create_text(600, 100, font=('Centaur', 50, "bold"), text='⦇ ៙ ~ Menu ~ ៙ ⦈', fill ="blue")
    
    Button(fen2, text='Jouer', command = main).place(x = 560, y = 200)
    Button(fen2, text='Règles !', command = regle).place(x = 560, y = 250)
    Button(fen2, text='Crédits', command = credis).place(x = 560, y = 550)
    Button(fen2, text='Quitter', command = fen2.destroy).place(x = 560, y = 600)
    
    
    fen_active = fen2
    fen2.mainloop()


def credis():                           #| Fenêtre crédits
    global fen_active
    
    
    try:
        fen_active.destroy()            #| La fenêtre active 
    except:
        pass
    
    fen3 = Tk()
    fen3.title('Bataille Navale')
    fen3.iconbitmap("anchor.ico")
    
    fond = (Image.open("menu_bg3.png"))                         #| Du Tkinter
    resized_image = fond.resize((1200,700), Image.ANTIALIAS)    #| Encore du Tkinter
    new_image = ImageTk.PhotoImage(resized_image)               #| Toujours du Tkinter, comme tout ce qui est graphique en Python sans PyGame
    
    dessin3 = Canvas(fen3, width = 1200, height = 700)
    dessin3.grid(row = 0, column = 0, columnspan=3, padx=3, pady=3)
    dessin3.pack(fill ="both")
    dessin3.create_image(0, 0, image = new_image , anchor ="nw")
    dessin3.create_text(600, 100, font=('Centaur', 50, "bold"), text='⦇ ៙ ~ Crédits ~ ៙ ⦈', fill ="blue")
    dessin3.create_text(600, 350, font=('Arial', 20, "bold"), text='Projet de : Eugène Lallain et Daniel Biros', fill ="black")
    dessin3.create_text(600, 380, font=('Arial', 20, "bold"), text='Classe    : Spé.NSI - Terminale', fill ="black")
    Button(fen3, text='Retour', command = menu).place(x = 560, y = 550)
    Button(fen3, text='Quitter', command = fen3.destroy).place(x = 560, y = 600)


    fen_active = fen3
    fen3.mainloop()
    

def regle():                    #| La fenêtre des règles
    global fen_active
    
    try:
        fen_active.destroy()
    except:
        pass
    
    
    fen4 = Tk()
    fen4.title('Bataille Navale')
    fen4.iconbitmap("anchor.ico")
    
    fond = (Image.open("regle_bg.png"))
    resized_image = fond.resize((1200,700), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)
    
    dessin4 = Canvas(fen4, width = 1200, height = 700)
    dessin4.grid(row = 0, column = 0, columnspan=3, padx=3, pady=3)
    dessin4.pack(fill ="both")
    dessin4.create_image(0, 0, image = new_image , anchor ="nw")
    dessin4.create_text(600, 100, font=('Centaur', 50, "bold"), text='⦇ ៙ ~ Règles ~ ៙ ⦈', fill ="blue")
    
    
    dessin4.create_line(610, 200,  635, 225, fill='red', width = 2)
    dessin4.create_line(610, 225,  635, 200, fill='red', width = 2)
    dessin4.create_text(525, 215, font=('Centaur', 15, "bold"), text='Touché : ', fill = "black")

    dessin4.create_arc((610, 250 ),(635, 275 ),width = 2, start=0, extent=180,style=ARC, outline='#0000FF')
    dessin4.create_arc((610,250 ),(635, 275 ),width = 2, start=180, extent=180,style=ARC, outline='#0000FF')
    dessin4.create_text(525, 260, font=('Centaur', 15, "bold"), text="A l'eau : " , fill = "black")

    dessin4.create_line(610, 290,  635, 315, fill='black', width = 2)
    dessin4.create_line(610, 315,  635, 290, fill='black', width = 2)
    dessin4.create_text(525, 305, font=('Centaur', 15, "bold"), text='Touché-Coulé : ', fill = "black")

    dessin4.create_text(600, 350, font=('Centaur', 15, "bold"), text="Pour placer un bateau, -click Gauche- sur la grille joueur à l'emplacement du centre du bateau, et appuyer sur le bouton du bateau choisit" , fill = "black")
    dessin4.create_text(600, 395, font=('Centaur', 15, "bold"), text="!! Attention les bateaux ne peuvent pas être déplacés une fois posés !!" , fill = "black")
    dessin4.create_text(600, 440, font=('Centaur', 15, "bold"), text="Les bateaux : Porte-Avions / Torpilleur sont placé selon leur centre arrière bas" , fill = "black")
    dessin4.create_text(600, 495, font=('Centaur', 15, "bold"), text="Pour tirer -click Droit- sur la grille ordinateur" , fill = "black")

        

    Button(fen4, text='Retour', command = menu).place(x = 560, y = 550)
    Button(fen4, text='Quitter', command = fen4.destroy).place(x = 560, y = 600)

    
    
    fen_active = fen4
    fen4.mainloop()
    
    
##----- Programme principal - Mise en fonction -----##

menu()      #| Exécution de la fenêtre menu qui est la première fenêtre du jeu est ainsi, lancement du jeu






#{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ( - ° - ) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}~#

                                ##----- Eugène -----##

                #Temps passé sur le code en 45-Tours ( 4 min ) : 1022 
                #Temps passé sur le code en heures : 68


#{~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ( - ° - ) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~}~#
