import pygame, random , easygui , time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy 

pygame.init()

#alle algemene variable
sign = 0
hoogte = 780
breete = 550
myfont = pygame.font.SysFont(None, 30)
naamfont = pygame.font.SysFont(None, 15)
beurt = 0
spelers =[ "","","",""]
worp1 = 0
worp2 = 0
grotekeuze = 1
positsies = [0,0,0,0]
info =False
klaar = False
clock = pygame.time.Clock()
gewonnen = False 
board = [[" " for x in range(3)] for y in range(3)]
SchermGrote = [breete,hoogte]
#vakkjes
vakjes = [[230,70],[302,64],[333,56],[363,62],[398,74],[423,97],[436,124],[443,154],[437,188],[416,213],[386,227],[355,233],[323,233]
,[289,233],[267,207],[230,211],[196,205],[164,205],[132,212],[100,222],[86,253],[80,283],[88,314],[115,339],[144,356],[176,359],[212,363],
[258,367],[295,369],[325,376],[359,383],[393,383],[419,387],[454,397],[481,417],[505,440],[508,472],[492,504],[466,546],[438,567],[408,595],
[371,609],[372,608],[343,599],[326,567],[315,530],[304,500],[285,471],[255,447],[222,444],[193,447],[158,470],[146,494],[138,524],[144,555],[154,585],
[185,600],[213,599],[241,590],[271,613],[266,648],[258,677],[238,700],[205,709],[170,698],[136,684],[100,667],[66,650],[41,622],[24,589],
[21,557],[33,530],[51,505],[53,477],[60,405],[60,405],[60,405],[60,405],[60,405],[60,405],[60,405]]
#defs
def put(beurt):
    if positsies[beurt]== 9 or positsies[beurt] == 20 or positsies[beurt] == 53 or positsies[beurt] == 60 or positsies[beurt] == 66:
        print ("je bent in de put")
        if positsies[beurt] ==9:
            positsies[beurt] = positsies[beurt] -5
        elif positsies[beurt] ==20:
            positsies[beurt] = positsies[beurt] -6
        elif positsies[beurt] ==53:
            positsies[beurt] = positsies[beurt] -8
        elif positsies[beurt] ==60:
            positsies[beurt] = positsies[beurt] -20
        if positsies[beurt] ==66:
            positsies[beurt] = positsies[beurt] -10
#def boterkaas en eiren
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
    (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
    (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
    (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
    (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
    (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
    (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
    (b[0][2] == l and b[1][1] == l and b[2][0] == l))

def get_text(i, j, gb, l1, l2):
    global sign
    global winaarvs
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winaar", f"{spelers[beurt]} won the match")
        winaarvs = spelers[beurt]
        return winaarvs 
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winaar", f"{uitgedagedespler} heeft gewonnen")
        winaarvs = spelers[beurt]
        return winaarvs
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Gelijkspel", "Gelijkspel")
    return winaarvs   
 
def isfree(i, j):
    return board[i][j] == " "  
                                   
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag
    
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop() 
               
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]     
                                    
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winaar", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winaar", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Gelijkspel", "Gelijkspel")
    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)      
           
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()   

def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",width=10, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)   

def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text=f"{spelers[beurt]}  : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text=f"{uitgedagedespler} : O",width=10, state=DISABLED)
    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)  

def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)
    head = Button(menu, text="---Welcome to tic-tac-toe---", activeforeground='red', activebackground="yellow", bg="red", fg="yellow", width=500, font='summer', bd=5)
    B1 = Button(menu, text="Single Player", command=wpc, activeforeground='red', activebackground="yellow", bg="red", fg="yellow", width=500, font='summer', bd=5)
    B2 = Button(menu, text="Multi Player", command=wpl, activeforeground='red', activebackground="yellow", bg="red", fg="yellow", width=500, font='summer', bd=5)
    B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red', activebackground="yellow", bg="red", fg="yellow", width=500, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()

# def startscherm
def inlogscherm():
    global startscherm , knopsluiten, knopinfo, knopstart,start_game, show_info,close,info
    info = False
    infoscherm.destroy()
    startscherm = tk.Tk()
    startscherm.geometry("500x500")
    knopstart = tk.Button(startscherm, text="Start", width=20, height=4, command=start_game).place(x= 175 , y= 125)
    knopinfo = tk.Button(startscherm, text="Spelregels", width=20, height=4, command=show_info).place(x=175, y=200)
    knopsluiten = tk.Button(startscherm, text="Afsluiten",width=20, height=4, command=close).place(x=175, y=275)
def start_game():
    global hello
    hello = True
    startscherm.destroy()
def show_info():
    global info
    info =True
    startscherm.destroy()
def close():
    startscherm.destroy()
    print("Yes")
    quit()

#het startscherm 
startscherm = tk.Tk()
startscherm.geometry("500x500")
knopstart = tk.Button(startscherm, text="Start", width=20, height=4, command=start_game).place(x= 175 , y= 125)
knopinfo = tk.Button(startscherm, text="Spelregels", width=20, height=4, command=show_info).place(x=175, y=200)
knopsluiten = tk.Button(startscherm, text="Afsluiten",width=20, height=4, command=close).place(x=175, y=275)
startscherm.mainloop()

# Als de Spelregels-knop is ingedrukt, toon het infoscherm
if info == True:
    # Maak het infoscherm aan
    infoscherm = tk.Tk()
    infoscherm.geometry("500x500")

    #een frame met een scrollbar en tekstveld
    frame = tk.Frame(infoscherm)
    frame.pack(fill=tk.BOTH, expand=1)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
    text.pack(fill=tk.BOTH, expand=1)

    text.insert(tk.END, "In 1947 is er een fransman geboren. Hij hete Régis Hauser, hij is in zijn leven heel rijk geworden. Voor zijn werk schreef hij boek een bedacht hij raadsels. Hij is 20 jaar bezig geweest om elf raadsels te verzinnen die, als je ze allemaal beantwoordt, de plek zouden geven waar hij een gouden uil heeft laten begraven. De is uil is begraven in 1993, deze uil is van massief goud en 1 miljoen euro waard. Echter is de uil tot op de dag nog niet gevonden. Régis Hauser is ondertussen overleden. Maar voordat hij is overleden vertelde hij dat er mensen heel dicht bij de oplossing zijn geweest maar dat ze 1 belangrijk ding zijn vergeten. Het verbinden van de antwoorden. \n\nDit is een echt gebeurd verhaal, wij gebruiken dit in ons spel als symbolisatie. De gouden uil zit in iedereen en staat voor je passie. Als je de juiste vragen beantwoordt en ze samenvoegt kom je er achter wat je passie is. Dit zijn de kernvragen die je tijdens het spel tegen gaat komen. Schrijf goed op wat je ontdekt en kijk wat er overeen komt. Als je naar 4 keer spelen een patroon begint te ontdekken dat zit daar misschien je gouden uil. ")
    text.insert(tk.END, "\n\nHoe win je?", ("large",))
    text.insert(tk.END, "\nDoor als eerste aan het einde van het bord te komen")
    text.insert(tk.END, "\n\nDe Tegels", ("large",))
    text.insert(tk.END, "\nEr zijn zes tegels \n   -VS tegel \n   -put tegel \n   -kernvraag tegel \n   -opdrachten tegel \n  -ontwikklings vragen tegel")
    text.insert(tk.END, "\n\nDe vs tegel", ("large",))
    text.insert(tk.END, "\nAls je op de VS tegel komt mag je 1 andere speler uidagen, klik op zijn naam. \njullie gaan nu boter,kaas en eirenen spelen. Er openend een scherm. De winnaar mag nog een keer gooien. Je beurt afgelopen")
    text.insert(tk.END, "\n\nDe put tegel", ("large",))
    text.insert(tk.END, "\nAls je op de put tegel komt moet je de put in, de volgende ronde begin je een aantal stappen terug.\nDit kan ook met de passief speler gebreuren")
    text.insert(tk.END, "\n\n Kernvraag tegel", ("large",))
    text.insert(tk.END, "\nAls je op de kernvraag tegel komt dan krijg je een kernvraag.\nDit is een heel moeilijk vraag en je moet deze zo goed mogelijk beandwoorden.\n Alsdat is gelukt dan is de volgde, het doel hier van is dat als je aan het eind van het spel je andwoorden in ziet je een patroon ziet")
    text.insert(tk.END, "\n\nDe opdracht tegel", ("large",))
    text.insert(tk.END, "\nDeze is nog niet af")
    text.insert(tk.END, "\n\nDe ontwikelingsvraag tegel", ("large",))
    text.insert(tk.END, "\nJe krijgt 1 vraag te zien. Deze moet je zo eerlijk mogelijk beandwoorden. Het doel hier van is dat je een partoon begint te herken")
    text.insert(tk.END, "\n\nActieve en passiefe spelers", ("large",))
    text.insert(tk.END, "\nEr is een actieve en een passief speler. De actieve speler gooit en voert een opdracht uit. De passieve speler loop alleen de 2e dobbelsteen.\n Hij voert de opdracht niet uit behalven asl hij op de put komt. Dan voert hij hem wel uit.")
    text.tag_configure("large", font=("Arial", 24))
    text.configure(state=tk.DISABLED)

    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)


    #een knop om terug te gaan naar het inlogscherm
    knopsluiteninfo = tk.Button(infoscherm, text="Terug", width=20, height=4, command=lambda: (inlogscherm(), infoscherm.destroy())).place(x=170, y=420)

    # Start de hoofdlus van het infoscherm
    infoscherm.mainloop()

#spelscherm
pygame.display.set_caption("De gouden Uil ")
scherm = pygame.display.set_mode(SchermGrote) 
bord = pygame.image.load("bord.png")
bord = pygame.transform.scale(bord, (550,778))

#Ontwikelingsvragen: Dit is een lijst van ontwikelings vragen.
ontwikelingsvragen =["Welke vakken vond/vind je leuk op de middelbare school? En waarom?","Bij welke activiteit(en) voel je de meeste voldoening in de tijd die je eraan besteed? En waarom?",
"Welke studie(s) zou je willen doen of heb je gedaan? En waarom lijkt/leek je deze studie op het eerste gezicht interessant?","Welke werkzaamheden zet jij het allerliefst bovenaan op je to-do lijst? En waarom?",
"Als je in een winkel staat met tijdschriften; naar welk tijdschrift gaat je oog het eerste naartoe en waarom? ","Wat zijn onderwerpen waar je veel over weet of veel over wilt weten en waarom? ",
"Wat vind je leuk om te doen (waar word je blij, enthousiast en gelukkig van) en waarom? (bijv.: bouwen, creëren, schrijven, werken met kinderen, koken, op het podium staan etc.) ",
"Van welke activiteit krijg je enorm veel energie en waarom? Of ook wel: Wat voelt niet eens als werk en waarom? (bijv: “Ik voel altijd veel energie als ik …….En al helemaal als ik dat combineer met …”)",
"Bij welke activiteit(en) voel je de meeste voldoening in de tijd die je eraan besteed? En waarom?","Wat wilde je vroeger worden? En wat leek je daar zou leuk aan? ",
"Waar ga jij van glunderen? En waarom?","Wat zou je doen als je nu 20 miljoen had?  En waarom?","Benoem in 30 seconden zoveel mogelijk elementen waar een ideale kantoorruimte aan moet voldoen. ",
"Vertel de anderen hoe je ideale dag zou zijn (van opstaan tot aan naar bed gaan). Welke activiteiten zitten daar allemaal in? En waarom is dat je ideale dag?","Als je een dier zou zijn, welke zou je zijn en waarom? ",
"Iemand vraagt wie je bent en waar je goed in ben. Wat zou je zeggen? En waarom? ","Je mag twee dingen noemen waardoor anderen zouden snappen in welke werk je goed bent. Welke dingen zou je noemen? En waarom? ",
"Stel dat je 20 miljoen aan een goed doel zou mogen besteden, waar zou je het aan besteden en waarom?","Als je (opnieuw) zou mogen kiezen voor een studie, welke studie zou je  dan kiezen? En waarom?","Welke mensen inspireren je? En wat exact inspireert je aan ze? ",
"Stel je hebt een half jaar helemaal niets gedaan. Wat zou je dan als eerste weer doen om je nuttig te voelen?","Wat is het laatste dat je gedaan hebt waar je trots op bent? ",
"Welke banen hebben anderen waarvan je zou willen dat jij ze had? En waarom trekt juist dat je zo aan?","Vraag aan een medespeler:  Wat denk jij dat mijn grootste sterktes, krachten en/of talenten zijn? En zou je kunnen uitleggen waarom je dat vindt?(Als je elkaar echt niet kent beantwoord hem zelf) ",
"Waar ben je beter in dan de meeste mensen? ","Bepaal met de groep wie het meeste invloed heeft op het dynamiek van het spel en waarom.",
"Je bent uitgekozen om naar een  compleet nieuwe planeet te gaan. Er schijnt daar een nieuwe beschaving te zijn. Welke 2 tot 3 dingen zou je hun willen overbrengen?",
"Tegen wie kijk je erg op? En wat herken je van jezelf daarin?","Vraag aan een medespeler voor welke hulp diegene jou zou bellen? (Als je elkaar echt niet kent, beantwoord hem zelf)",
"Vraag aan een medespeler: Als ik leidinggevende was, waar of in welke afdeling zou ik dat dan zijn? (Als je elkaar echt niet kent beantwoord hem zelf)","Welk compliment zou jij krijgen op het afscheid van je opleiding of je werk? En waarom?","Welk beroep zou jij meer over willen weten? ","Neem een bekend persoon in gedachten die een toffe baan heeft. Laat je medespeler raden wie het is (je mag alles gebruiken behalve de daadwerkelijke naam te noemen)",
"In welk vak zou je andere mensen les willen geven? En waarom?","Vertel één ding waar je als je tijd hebt graag iets aan wilt veranderen.","Wie ben jij vroeger als kind geweest? Omschrijf eens een paar kenmerken van jou als kind. ",
"Stel dat je met de kennis van nu met terugwerkende kracht één moment in je leven mocht kiezen waarop je een andere keuze zou kunnen maken, waar zou je dan voor hebben gekozen? En waarom? ","Stel dat geld, kennis of opleiding geen enkele belemmering zou zijn (alles is mogelijk), en je mag jouw eigen werk kiezen, wat zou je dan kiezen? En waarom juist dat?",
"Welke bedrijven, welke mensen of welke instanties zou je graag op één of andere manier willen ondersteunen? (Bijv. onterecht veroordeelde gevangenen, kinderen met een beperking, werklozen, carrière vrouwen, moeders, studenten, echtparen, bedrijven die op het randje van faillissement staan, etc.)",
"Als je een boek zou schrijven wat over hoe de wereld gelezen zou worden en wat gegarandeerd een bestseller zou zijn, wat zou de titel van dat boek dan zijn?","Stel dat er over 10 jaar een artikel in een tijdschrift wordt uitgebracht over wat je hebt bereikt en wat voor bijzondere verandering je teweeg hebt gebracht. Wat is dan de headline van dit artikel?",
"Vertel over de eigenschap of talent waarmee je in de toekomst succes gaat behalen.","Waar ben je over drie jaar?(Leg het uit in zoveel mogelijk zintuigen; Wat zie je? Wat voel je? Wat ruik je? Wat hoor je?)",
"Wat wil je dat mensen over je zeggen op je begrafenis over de prestaties die je hebt geleverd en de dingen die je hebt bereikt?","Je krijgt geld voor een eigen zaak, wat zou je doen?",
"Benoem iets waar je wat aan wilt veranderen en vertel hoe je dat gaat doen.","Noem een probleem dat je graag zou willen oplossen.","Benoem een kwaliteit die jij bezit","Wat fascineert jou? ","Waar geloof je heilig in? ","Deel iets waar je trots op bent"]
#kernvragen: Dit is een lijst met 11 kernvragen
kernvragen =["Met alle kennis die je nu hebt; waar zou je anderen vanaf morgen al mee kunnen helpen?","Als je kijkt naar je huidige werkzaamheden; wat mis je daaraan? En hoe zou je daar op een andere manier tóch invulling aan kunnen geven?",
"Noem eens op welke mensen of organisaties jij goed zou kunnen helpen en waarom?","Welk stemmetje gaat er nog in je hoofd om waardoor je nog niet voor je eigen pad durft te kiezen? (En welke andere stem kun je daarvoor in de plaats zetten?)",
"Als je kijkt naar jouw kwaliteiten; welke rol of functie zou jou op het lijf geschreven staan?","Als je op je 90e op een schommelstoel zit en je kijkt terug op je leven; wat hoop je dan dat er is gebeurt waardoor jij vol trots kunt terugkijken op het verschil dat jij hebt gemaakt voor anderen?",
"Wat zijn 3 randvoorwaarden die voor jou ontzettend belangrijk zijn om jouw werk helemaal naar jouw zin te maken? (denk aan zelf bepalen welke tijden ik werk, fysiek met klanten kunnen afspreken, remote kunnnen werken, etc.)",
"Welke uitdaging heb jij overwonnen of welke ervaring heb jij meegemaakt waar jij nu anderen mee zou kunnen helpen?","Er zijn altijd 100 redenen waarom je iets nu nog kan doen. Noem eens één reden waarom het nu WEL het juiste moment is om te doen wat je graag wilt?",
"Wie zou jou kunnen helpen om je droom waarheid te maken? En waarom die persoon?","Welke opoffering moet je doen (of wat moet je loslaten) om de weg in te gaan waar je uiteindelijk veel blijer, energieker en voldaner van wordt?"]
#Opslaan van de andwoorden zodat de spelers aan het eind van het spel een overzicht kunnen krijgen
Andwoordopslaan = [["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"]]
AndwoordOpslaanKernvraag = [["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"]]

#Om de spelers namen krijgen
for i in spelers:
    spelers[beurt] = easygui.enterbox(f"Geef de naam van speler {beurt}")
    beurt = beurt + 1
beurt = 0

#De game loop
while not klaar:
    clock.tick(30)
    scherm.fill((255,255,255))
    bordrect = bord.get_rect(width=5000, height=1000)
    scherm.blit(bord, bordrect)

    #pion1 
    speler_x0 = vakjes[positsies[0]][0]-5
    speler_y0 = vakjes[positsies[0]][1]-5   
    kleur_0 = (0,255,0)
    speler1 = pygame.draw.circle(scherm, kleur_0, (speler_x0, speler_y0), 20)
    spelernaamrender0 = naamfont.render(spelers[0], 1, (0,0,0))
    scherm.blit(spelernaamrender0, (speler_x0-5, speler_y0)) 
    
    #pion2
    speler_x1 = vakjes[positsies[1]][0]+5
    speler_y1 = vakjes[positsies[1]][1]-5  
    kleur_1 = (0,0,255)
    speler2 = pygame.draw.circle(scherm, kleur_1, (speler_x1, speler_y1), 20)
    spelernaamrender1 = naamfont.render(spelers[1], 1, (0,0,0))
    scherm.blit(spelernaamrender1, (speler_x1-5, speler_y1))
    
    #pion3
    speler_x2 = vakjes[positsies[2]][0]-5
    speler_y2 = vakjes[positsies[2]][1]+5   
    kleur_2 = (255,255,0) 
    speler3 = pygame.draw.circle(scherm, kleur_2, (speler_x2, speler_y2), 20)
    spelernaamrender2 = naamfont.render(spelers[2], 1, (0,0,0))
    scherm.blit(spelernaamrender2, (speler_x2-5, speler_y2))
    
    #pion4
    speler_x3 = vakjes[positsies[3]][0]+5
    speler_y3 = vakjes[positsies[3]][1]+5  
    kleur_3 = (0,255,255)
    speler4 = pygame.draw.circle(scherm, kleur_3, (speler_x3, speler_y3), 20)
    spelernaamrender3 = naamfont.render(spelers[3], 1, (0,0,0))
    scherm.blit(spelernaamrender3, (speler_x3-5, speler_y3))


    for event in pygame.event.get():
        #Om het scherm mooi af te sluiten
        if event.type == pygame.QUIT:
            klaar = True
        #Om de game echt te kunnen spelen
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #De dobbelstenen
                worp1 = random.randint(1,6)
                worp2 = random.randint(1,6)
                positsies[beurt] += worp1 + worp2
                tekst = (f"dobbelsteen 2 gooide {worp2}")
                label = myfont.render(tekst, 1, (0,0,0))
                scherm.blit(label, (302,315))

                tekst1 = (f"dobbelsteen 1 gooide {worp1}")
                label = myfont.render(tekst1, 1, (0,0,0))
                scherm.blit(label, (302,295))
                
                

                #Om het spel iets sneller te laten gaan neemt ook het persoon recht van de actieve speler stappen. Wel alleen van de 2e dobeelsteen
                if beurt == 0:
                    positsies[3] += worp2
                elif beurt == 1:
                    positsies[0] += worp2
                elif beurt == 2:
                    positsies[1] += worp2
                elif beurt == 3:
                    positsies[2] += worp2
                
                speler1 = pygame.draw.circle(scherm, kleur_0, (speler_x0, speler_y0), 20)
                spelernaamrender0 = naamfont.render(spelers[0], 1, (0,0,0))
                scherm.blit(spelernaamrender0, (speler_x0-5, speler_y0))
                
                speler2 = pygame.draw.circle(scherm, kleur_1, (speler_x1, speler_y1), 20)
                spelernaamrender1 = naamfont.render(spelers[1], 1, (0,0,0))
                scherm.blit(spelernaamrender1, (speler_x1-5, speler_y1))
                
                speler3 = pygame.draw.circle(scherm, kleur_2, (speler_x2, speler_y2), 20)
                spelernaamrender2 = naamfont.render(spelers[2], 1, (0,0,0))
                scherm.blit(spelernaamrender2, (speler_x2-5, speler_y2))
                
                speler4 = pygame.draw.circle(scherm, kleur_3, (speler_x3, speler_y3), 20)
                spelernaamrender3 = naamfont.render(spelers[3], 1, (0,0,0))
                scherm.blit(spelernaamrender3, (speler_x3-5, speler_y3))
                pygame.display.flip()
                
                

                #ontwikelingskaart: Als je op het rode vakje komt dan pak je een ontwikelingskaart.Per speler wordt elk andwoordt opgeslagen
                if positsies[beurt] == 1 or positsies[beurt] == 3 or positsies[beurt] == 5 or positsies[beurt] == 8 or positsies[beurt] == 10 or positsies[beurt] == 12 or positsies[beurt] == 17 or positsies[beurt] == 21 or positsies[beurt] == 23 or positsies[beurt] == 24 or positsies[beurt] == 29 or positsies[beurt] == 32 or positsies[beurt] == 34 or positsies[beurt] == 36 or positsies[beurt] == 39 or positsies[beurt] == 42 or positsies[beurt] == 44 or positsies[beurt] == 48 or positsies[beurt] == 50 or positsies[beurt] == 56 or positsies[beurt] == 59 or positsies[beurt] == 63 or positsies[beurt] == 65 or positsies[beurt] == 71:
                    for i in range(0,12):
                        row = beurt
                        col = i
                        lengte = len(Andwoordopslaan[row][col])
                        if lengte == 1: 
                            Andwoordopslaan[row][col] = easygui.enterbox(random.sample(ontwikelingsvragen,grotekeuze)[0], f"Ontwikelingsvraag voor {spelers[beurt]}" )
                            break

                #Kern vraag        
                elif positsies[beurt]== 4 or positsies[beurt]== 7 or positsies[beurt]== 13 or positsies[beurt]== 16 or positsies[beurt]== 19 or positsies[beurt]== 22 or positsies[beurt]== 26 or positsies[beurt]== 28 or positsies[beurt]== 33 or positsies[beurt]== 37 or positsies[beurt]== 40 or positsies[beurt]== 43 or positsies[beurt]== 45 or positsies[beurt]== 49 or positsies[beurt]== 51 or positsies[beurt]== 54 or positsies[beurt]== 57 or positsies[beurt]== 61 or positsies[beurt]== 64 or positsies[beurt]== 67 or positsies[beurt]== 70 or positsies[beurt]== 72:
                    print("Pak een kernvraag") 
                    for k in range(0,11):
                        row2 = beurt
                        col2 = k
                        lengte2 = len(AndwoordOpslaanKernvraag[row2][col2])
                        if lengte2 == 1: 
                            AndwoordOpslaanKernvraag[row2][col2] = easygui.enterbox(random.sample(kernvragen,grotekeuze)[0], f"Kernvraag voor {spelers[beurt]}" )
                            break

                #VS tegel
                elif positsies[beurt] == 14 or positsies[beurt] == 27 or positsies[beurt] == 46 or positsies[beurt] == 48:
                    choices = [f'{spelers[0]}', f'{spelers[1]}', f'{spelers[2]}',f'{spelers[3]}']
                    choices.remove(f"{spelers[beurt]}")
                    selected_option = easygui.choicebox(title='kies de actieve speler', msg= f'{spelers[beurt]} mag iemand uitdagen', choices=choices)
                    uitgedagedespler = selected_option
                    if __name__ == '__main__':
                        play()
                    
                    #beloning uit delen
                    if winaarvs == spelers[beurt]:
                        worp3 = random.randint(1,6)
                        positsies[beurt] += worp3
                        print("De active sperler wint")
                    elif winaarvs == uitgedagedespler:
                        worp3 = random.randint(1,6)
                        print("De ander speler wint")
                        selected_option += worp3            
               
                #Bepalen over er iemand heeft gewonnen
                elif positsies[beurt] >= 73:
                    positsies[beurt] = 73
                    Eindscherm = tk.Tk()
                    Eindscherm.geometry("500x500")
                    winaarknop = tk.Button(Eindscherm, text=f"De winnaar is {spelers[beurt]}", width=80, height=16, command=close)
                    winaarknop.place(x=175, y=275)
                    gewonnen = True
                    # Create the main window
                    root = tk.Tk()
                    root.geometry("800x600")  # Set the size of the window to 800x600 pixels
                    root.title("My GUI")

                    # Create a notebook widget with 4 tabs
                    notebook = ttk.Notebook(root)
                    tab1 = tk.Frame(notebook)
                    tab2 = tk.Frame(notebook)
                    tab3 = tk.Frame(notebook)
                    tab4 = tk.Frame(notebook)
                    notebook.add(tab1, text="Page 1")
                    notebook.add(tab2, text="Page 2")
                    notebook.add(tab3, text="Page 3")
                    notebook.add(tab4, text="Page 4")
                    notebook.pack(fill="both", expand=True)

                    # Add widgets to the tabs
                    tk.Label(tab1, text="This is page 1").pack(pady=10)
                    tk.Label(tab2, text="This is page 2").pack(pady=10)
                    tk.Label(tab3, text="This is page 3").pack(pady=10)
                    tk.Label(tab4, text="This is page 4").pack(pady=10)

                    # Start the GUI event loop
                    root.mainloop()

                #put-tegel. Als de actieve speler hier op komt dan gaat hij achter uit
                elif positsies[beurt]== 9 or positsies[beurt] == 20 or positsies[beurt] == 53 or positsies[beurt] == 60 or positsies[beurt] == 66:
                    put(beurt)
               #opdracht kaarten
                elif positsies[beurt] == 2 or positsies[beurt] == 6 or positsies[beurt] == 11 or positsies[beurt] == 15 or positsies[beurt] == 18 or positsies[beurt] == 24 or positsies[beurt] == 30 or positsies[beurt] == 35 or positsies[beurt] == 38 or positsies[beurt] == 41 or positsies[beurt] == 47 or positsies[beurt] == 52 or positsies[beurt] == 55 or positsies[beurt] == 58 or positsies[beurt] == 62 or positsies[beurt] == 69:
                    print("pak een opdracht kaart")
                    #maak een pup up melding met een random kaart waar ze 
                    #iets kunnen in vullen wat wordt opgeslagen en aan het eind wordt gedeeld

                #De brug
                elif positsies[beurt] == 31:
                    Brug = naamfont.render(f"{spelers[beurt]} komt op 31 en neemt de brug", 1, (0,0,0))
                    scherm.blit(Brug, (302,295))
                    pygame.display.flip()
                    time.sleep(3)
                    positsies[beurt] = 45
                
                #put-tegel passiefe speler. Als de pasiefe speler op de put komt moet diet ook uit gevoerd worden.  
                if beurt == 0:
                    put(3)
                elif beurt == 1:
                    put(0)
                elif beurt ==2:
                    put(1)
                elif beurt == 3:
                    put(2)
                 
                #Om er voor te zorgen dat de volgende speler aan de beurt is
                if beurt == 0:
                    beurt = 1 
                elif beurt == 1:
                    beurt = 2
                elif beurt == 2:
                    beurt = 3
                elif beurt == 3:
                    beurt = 0 
            
            #Om er voor te zorgen dat de spelers op elk moment opnieuw kunnen beginnen
            elif event.key == pygame.K_BACKSPACE:
                positsies = [0,0,0,0]
                beurt = 0
            if gewonnen == True:
                klaar = True
                print("het werkt")
                #Maak een popup medling met dat de game klaar is, zeg wie heeft gewonnen, wil je opnieuw
                #geef van ideereen de andwoorde weer en de vragen. 
            
    pygame.display.flip()

pygame.display.flip()
pygame.quit()