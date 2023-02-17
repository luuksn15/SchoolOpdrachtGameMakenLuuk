import pygame, random , easygui , time, os
import tkinter as tk 
pygame.init()



#het startscherm 
info =False
klaar = False
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
    
    

startscherm = tk.Tk()
startscherm.geometry("500x500")
knopstart = tk.Button(startscherm, text="Start", width=20, height=4, command=start_game).place(x= 175 , y= 125)
knopinfo = tk.Button(startscherm, text="Spelregels", width=20, height=4, command=show_info).place(x=175, y=200)
knopsluiten = tk.Button(startscherm, text="Afsluiten",width=20, height=4, command=close).place(x=175, y=275)



# Voeg de knoppen toe aan het startscherm

# Start de hoofdlus
startscherm.mainloop()

# Als de "Spelregels"-knop is ingedrukt, toon het infoscherm
if info == True:
    # Maak het infoscherm aan
    infoscherm = tk.Tk()
    infoscherm.geometry("500x500")
    knopsluiteninfo = tk.Button(infoscherm, text="Terug", width=20, height=4, command=lambda: (inlogscherm(), infoscherm.destroy())).place(x= 170, y=420)
    # Start de hoofdlus van het infoscherm
    infoscherm.mainloop()

#titel
pygame.display.set_caption("De gouden Uil ")

#spelscherm
hoogte = 780
breete = 550
SchermGrote = [breete,hoogte]
scherm = pygame.display.set_mode(SchermGrote) 


    
#BORD AFBELDING
bord = pygame.image.load("bord.png")
bord = pygame.transform.scale(bord, (550,778))
#defs
def put():
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

myfont = pygame.font.SysFont(None, 30)
naamfont = pygame.font.SysFont(None, 15)
beurt = 0
spelers =[ "","","",""]
worp1 = 0
worp2 = 0
#Ontwikelingsvragen: Dit is een lijst van ontwikelings vragen.
ontwikelingsvragen =[["Welke vakken vond/vind je leuk op de middelbare school? En waarom?"],["Bij welke activiteit(en) voel je de meeste voldoening in de tijd die je eraan besteed? En waarom?"],
["Welke studie(s) zou je willen doen of heb je gedaan? En waarom lijkt/leek je deze studie op het eerste gezicht interessant?"],["Welke werkzaamheden zet jij het allerliefst bovenaan op je to-do lijst? En waarom?"],
["Als je in een winkel staat met tijdschriften; naar welk tijdschrift gaat je oog het eerste naartoe en waarom? "],["Wat zijn onderwerpen waar je veel over weet of veel over wilt weten en waarom? "],
["Wat vind je leuk om te doen (waar word je blij, enthousiast en gelukkig van) en waarom? (bijv.: bouwen, creëren, schrijven, werken met kinderen, koken, op het podium staan etc.) "],
["Van welke activiteit krijg je enorm veel energie en waarom? Of ook wel: Wat voelt niet eens als werk en waarom? (bijv: “Ik voel altijd veel energie als ik …….En al helemaal als ik dat combineer met …”)"],
["Bij welke activiteit(en) voel je de meeste voldoening in de tijd die je eraan besteed? En waarom?"],["Wat wilde je vroeger worden? En wat leek je daar zou leuk aan? "],
["Waar ga jij van glunderen? En waarom?"],["Wat zou je doen als je nu 20 miljoen had?  En waarom?"],["Benoem in 30 seconden zoveel mogelijk elementen waar een ideale kantoorruimte aan moet voldoen. "],
["Vertel de anderen hoe je ideale dag zou zijn (van opstaan tot aan naar bed gaan). Welke activiteiten zitten daar allemaal in? En waarom is dat je ideale dag?"],["Als je een dier zou zijn, welke zou je zijn en waarom? "],
["Iemand vraagt wie je bent en waar je goed in ben. Wat zou je zeggen? En waarom? "],["Je mag twee dingen noemen waardoor anderen zouden snappen in welke werk je goed bent. Welke dingen zou je noemen? En waarom? "],
["Stel dat je 20 miljoen aan een goed doel zou mogen besteden, waar zou je het aan besteden en waarom?"],["Als je (opnieuw) zou mogen kiezen voor een studie, welke studie zou je  dan kiezen? En waarom?"],["Welke mensen inspireren je? En wat exact inspireert je aan ze? "],
["Stel je hebt een half jaar helemaal niets gedaan. Wat zou je dan als eerste weer doen om je nuttig te voelen?"],["Wat is het laatste dat je gedaan hebt waar je trots op bent? "],
["Welke banen hebben anderen waarvan je zou willen dat jij ze had? En waarom trekt juist dat je zo aan?"],["Vraag aan een medespeler:  Wat denk jij dat mijn grootste sterktes, krachten en/of talenten zijn? En zou je kunnen uitleggen waarom je dat vindt?(Als je elkaar echt niet kent beantwoord hem zelf) "],
["Waar ben je beter in dan de meeste mensen? "],["Bepaal met de groep wie het meeste invloed heeft op het dynamiek van het spel en waarom."],
["Je bent uitgekozen om naar een  compleet nieuwe planeet te gaan. Er schijnt daar een nieuwe beschaving te zijn. Welke 2 tot 3 dingen zou je hun willen overbrengen?"],
["Tegen wie kijk je erg op? En wat herken je van jezelf daarin?"],["Vraag aan een medespeler voor welke hulp diegene jou zou bellen? (Als je elkaar echt niet kent, beantwoord hem zelf)"],
["Vraag aan een medespeler: Als ik leidinggevende was, waar of in welke afdeling zou ik dat dan zijn? (Als je elkaar echt niet kent beantwoord hem zelf)"],["Welk compliment zou jij krijgen op het afscheid van je opleiding of je werk? En waarom?"],["Welk beroep zou jij meer over willen weten? "],["Neem een bekend persoon in gedachten die een toffe baan heeft. Laat je medespeler raden wie het is (je mag alles gebruiken behalve de daadwerkelijke naam te noemen)"],
["In welk vak zou je andere mensen les willen geven? En waarom?"],["Vertel één ding waar je als je tijd hebt graag iets aan wilt veranderen."],["Wie ben jij vroeger als kind geweest? Omschrijf eens een paar kenmerken van jou als kind. "],
["Stel dat je met de kennis van nu met terugwerkende kracht één moment in je leven mocht kiezen waarop je een andere keuze zou kunnen maken, waar zou je dan voor hebben gekozen? En waarom? "],["Stel dat geld, kennis of opleiding geen enkele belemmering zou zijn (alles is mogelijk), en je mag jouw eigen werk kiezen, wat zou je dan kiezen? En waarom juist dat?"],
["Welke bedrijven, welke mensen of welke instanties zou je graag op één of andere manier willen ondersteunen? (Bijv. onterecht veroordeelde gevangenen, kinderen met een beperking, werklozen, carrière vrouwen, moeders, studenten, echtparen, bedrijven die op het randje van faillissement staan, etc.)"],
["Als je een boek zou schrijven wat over hoe de wereld gelezen zou worden en wat gegarandeerd een bestseller zou zijn, wat zou de titel van dat boek dan zijn?"],["Stel dat er over 10 jaar een artikel in een tijdschrift wordt uitgebracht over wat je hebt bereikt en wat voor bijzondere verandering je teweeg hebt gebracht. Wat is dan de headline van dit artikel?"],
["Vertel over de eigenschap of talent waarmee je in de toekomst succes gaat behalen."],["Waar ben je over drie jaar?(Leg het uit in zoveel mogelijk zintuigen; Wat zie je? Wat voel je? Wat ruik je? Wat hoor je?)"],
["Wat wil je dat mensen over je zeggen op je begrafenis over de prestaties die je hebt geleverd en de dingen die je hebt bereikt?"],["Je krijgt geld voor een eigen zaak, wat zou je doen?"],
["Benoem iets waar je wat aan wilt veranderen en vertel hoe je dat gaat doen."],["Noem een probleem dat je graag zou willen oplossen."],["Benoem een kwaliteit die jij bezit"],["Wat fascineert jou? "],["Waar geloof je heilig in? "],["Deel iets waar je trots op bent"]]
#kernvragen
kernvragen =["Met alle kennis die je nu hebt; waar zou je anderen vanaf morgen al mee kunnen helpen?","Als je kijkt naar je huidige werkzaamheden; wat mis je daaraan? En hoe zou je daar op een andere manier tóch invulling aan kunnen geven?",
"Noem eens op welke mensen of organisaties jij goed zou kunnen helpen en waarom?","Welk stemmetje gaat er nog in je hoofd om waardoor je nog niet voor je eigen pad durft te kiezen? (En welke andere stem kun je daarvoor in de plaats zetten?)",
"Als je kijkt naar jouw kwaliteiten; welke rol of functie zou jou op het lijf geschreven staan?","Als je op je 90e op een schommelstoel zit en je kijkt terug op je leven; wat hoop je dan dat er is gebeurt waardoor jij vol trots kunt terugkijken op het verschil dat jij hebt gemaakt voor anderen?",
"Wat zijn 3 randvoorwaarden die voor jou ontzettend belangrijk zijn om jouw werk helemaal naar jouw zin te maken? (denk aan zelf bepalen welke tijden ik werk, fysiek met klanten kunnen afspreken, remote kunnnen werken, etc.)",
"Welke uitdaging heb jij overwonnen of welke ervaring heb jij meegemaakt waar jij nu anderen mee zou kunnen helpen?","Er zijn altijd 100 redenen waarom je iets nu nog kan doen. Noem eens één reden waarom het nu WEL het juiste moment is om te doen wat je graag wilt?",
"Wie zou jou kunnen helpen om je droom waarheid te maken? En waarom die persoon?","Welke opoffering moet je doen (of wat moet je loslaten) om de weg in te gaan waar je uiteindelijk veel blijer, energieker en voldaner van wordt?"]
grotekeuze = 1
#VS
VS = [f" {spelers[beurt]}, daag iemand anders uit in wie het best , \n  een olifant na kan doen",f" {spelers[beurt]}, daag iemand anders uit in wie het best , \n  onderwijz in 1 zin kan omschrijven",
f" {spelers[beurt]}, daag iemand anders uit in wie het best , \n  Donald Duck na kan doen",f" {spelers[beurt]}, daag iemand anders uit in wie het best , \n  de handstand kan",f" {spelers[beurt]}, daag iemand anders uit in wie het best , \n  kat na kan doen",f" {spelers[beurt]}, daag iemand ander uit in wie het best , \n  in 1 zin Nederland kan omschrijven",
f" {spelers[beurt]}, daag iemand ander uit in wie het best , \n  grappen kan vertelen",f" {spelers[beurt]}, daag iemand ander uit in wie het best , \n  kan zingen"]
#vakkjes
vakjes = [[230,70],[302,64],[333,56],[363,62],[398,74],[423,97],[436,124],[443,154],[437,188],[416,213],[386,227],[355,233],[323,233]
,[289,233],[267,207],[230,211],[196,205],[164,205],[132,212],[100,222],[86,253],[80,283],[88,314],[115,339],[144,356],[176,359],[212,363],
[258,367],[295,369],[325,376],[359,383],[393,383],[419,387],[454,397],[481,417],[505,440],[508,472],[492,504],[466,546],[438,567],[408,595],
[371,609],[372,608],[343,599],[326,567],[315,530],[304,500],[285,471],[255,447],[222,444],[193,447],[158,470],[146,494],[138,524],[144,555],[154,585],
[185,600],[213,599],[241,590],[271,613],[266,648],[258,677],[238,700],[205,709],[170,698],[136,684],[100,667],[66,650],[41,622],[24,589],
[21,557],[33,530],[51,505],[53,477],[60,405],[60,405],[60,405],[60,405],[60,405],[60,405],[60,405]]

#pionn positie
positsies = [0,0,0,0]
Andwoordopslaan = [["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"]]
AndwoordOpslaanKernvraag = [["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"],
["1","1", "1","1","1","1","1","1","1","1","1","1"]]
clock = pygame.time.Clock()
gewonnen = False 
#Dit doen we zodat elke speler een eigen naam heeft. 

#spelers namen krijgen
for i in spelers:
    spelers[beurt] = easygui.enterbox(f"Geef de naam van speler {beurt}")
    beurt = beurt + 1
beurt = 0

while not klaar:
    clock.tick(30)
    scherm.fill((255,255,255))
    bordrect = bord.get_rect(width=5000, height=1000)
    scherm.blit(bord, bordrect)

    #pion1 
    speler0_x = vakjes[positsies[0]][0]-5
    speler0_y = vakjes[positsies[0]][1]-5   
    kleur_0 = (0,255,0)
    pygame.draw.circle(scherm, kleur_0, (speler0_x, speler0_y), 20)
    speler0naamrender = naamfont.render(spelers[0], 1, (0,0,0))
    scherm.blit(speler0naamrender, (speler0_x-5, speler0_y)) 
    #pion2
    speler1_x = vakjes[positsies[1]][0]+5
    speler1_y = vakjes[positsies[1]][1]-5  
    kleur_1 = (0,0,255)
    pygame.draw.circle(scherm, kleur_1, (speler1_x, speler1_y), 20)
    speler1naamrender = naamfont.render(spelers[1], 1, (0,0,0))
    scherm.blit(speler1naamrender, (speler1_x-5, speler1_y))
    #pion3
    speler2_x = vakjes[positsies[2]][0]-5
    speler2_y = vakjes[positsies[2]][1]+5   
    kleur_2 = (255,255,0) 
    pygame.draw.circle(scherm, kleur_2, (speler2_x, speler2_y), 20)
    speler2naamrender = naamfont.render(spelers[2], 1, (0,0,0))
    scherm.blit(speler2naamrender, (speler2_x-5, speler2_y))
    #pion4
    speler3_x = vakjes[positsies[3]][0]+5
    speler3_y = vakjes[positsies[3]][1]+5  
    kleur_3 = (0,255,255)
    pygame.draw.circle(scherm, kleur_3, (speler3_x, speler3_y), 20)
    speler3naamrender = naamfont.render(spelers[3], 1, (0,0,0))
    scherm.blit(speler3naamrender, (speler3_x-5, speler3_y))
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            klaar = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
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
                    beurt = 3
                    positsies[beurt] += worp2
                    beurt = 0
                elif beurt == 1:
                    beurt = 0
                    positsies[beurt] += worp2
                    beurt = 1
                elif beurt == 2:
                    beurt = 1
                    positsies[beurt] += worp2
                    beurt = 2
                elif beurt == 3:
                    beurt = 2
                    positsies[beurt] += worp2
                    beurt = 3

                pygame.display.flip()
                #ontwikelingskaart: Als je op het rode vakje komt dan pak je een ontwikelingskaart.Per speler wordt elk andwoordt opgeslagen
                if positsies[beurt] == 1 or positsies[beurt] == 3 or positsies[beurt] == 5 or positsies[beurt] == 8 or positsies[beurt] == 10 or positsies[beurt] == 12 or positsies[beurt] == 17 or positsies[beurt] == 21 or positsies[beurt] == 23 or positsies[beurt] == 24 or positsies[beurt] == 29 or positsies[beurt] == 32 or positsies[beurt] == 34 or positsies[beurt] == 36 or positsies[beurt] == 39 or positsies[beurt] == 42 or positsies[beurt] == 44 or positsies[beurt] == 48 or positsies[beurt] == 50 or positsies[beurt] == 56 or positsies[beurt] == 59 or positsies[beurt] == 63 or positsies[beurt] == 65 or positsies[beurt] == 71:
                    for i in range(0,12):
                        row = beurt
                        col = i
                        lengte = len(Andwoordopslaan[row][col])
                        if lengte == 1: 
                            Andwoordopslaan[row][col] = easygui.enterbox(random.sample(ontwikelingsvragen,grotekeuze)[0][0], f"Ontwikelingsvraag voor {spelers[beurt]}" )
                            break
                        
                elif positsies[beurt]== 4 or positsies[beurt]== 7 or positsies[beurt]== 13 or positsies[beurt]== 16 or positsies[beurt]== 19 or positsies[beurt]== 22 or positsies[beurt]== 26 or positsies[beurt]== 28 or positsies[beurt]== 33 or positsies[beurt]== 37 or positsies[beurt]== 40 or positsies[beurt]== 43 or positsies[beurt]== 45 or positsies[beurt]== 49 or positsies[beurt]== 51 or positsies[beurt]== 54 or positsies[beurt]== 57 or positsies[beurt]== 61 or positsies[beurt]== 64 or positsies[beurt]== 67 or positsies[beurt]== 70 or positsies[beurt]== 72:
                    print("Pak een kernvraag") 
                    for k in range(0,11):
                        row2 = beurt
                        col2 = k
                        lengte2 = len(AndwoordOpslaanKernvraag[row2][col2])
                        if lengte2 == 1: 
                            AndwoordOpslaanKernvraag[row2][col2] = easygui.enterbox(random.sample(kernvragen,grotekeuze)[0], f"Kernvraag voor {spelers[beurt]}" )
                            break

                
                #VS maken
                elif positsies[beurt] == 14 or positsies[beurt] == 27 or positsies[beurt] == 46 or positsies[beurt] == 48:
                    choices = [f'{spelers[0]}', f'{spelers[1]}', f'{spelers[2]}',f'{spelers[3]}']
                    selected_option = easygui.choicebox(title='kies de actieve speler', msg= f'{spelers[beurt]} mag iemand uitdagen', choices=choices)
                    
                    WIDTH1, HEIGHT1 = 900, 500
                    WIN = pygame.display.set_mode((WIDTH1, HEIGHT1))
                    pygame.display.set_caption("VS")
                    WHITE = (255, 255, 255)
                    BLACK = (0, 0, 0)
                    RED = (255, 0, 0)
                    YELLOW = (255, 255, 0)

                    BORDER = pygame.Rect(WIDTH1/2-5, 0, 10, HEIGHT1)

                    # Set Bullet Sound Effects
                    BULLET_HIT_SOUND = pygame.mixer.Sound('GunHit.wav')   


                    HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
                    WINNER_FONT = pygame.font.SysFont('comicsans', 100)

                    FPS = 60
                    VEL = 5
                    BULLET_VEL = 7
                    MAX_BULLETS = 3
                    SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40


                    YELLOW_HIT = pygame.USEREVENT + 1
                    RED_HIT = pygame.USEREVENT + 2

                    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship_yellow.png"))
                    YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
                    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("spaceship_red.png"))
                    RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

                    SPACE = pygame.transform.scale(pygame.image.load(os.path.join('space.png')), (WIDTH1, HEIGHT1))


                    def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):

                        WIN.blit(SPACE, (0, 0))
                        pygame.draw.rect(WIN, BLACK, BORDER)

                        red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
                        yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
                        WIN.blit(red_health_text, (WIDTH1 - red_health_text.get_width() - 10, 10))
                        WIN.blit(yellow_health_text, (10, 10))

                        WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
                        WIN.blit(RED_SPACESHIP, (red.x, red.y))

                        for bullet in red_bullets:
                            pygame.draw.rect(WIN, RED, bullet)
                        for bullet in yellow_bullets:
                            pygame.draw.rect(WIN, YELLOW, bullet)
                        positsies[beurt] = positsies[beurt] +1
                        pygame.display.update()
                        positsies[beurt] = positsies[beurt] -1



                    def yellow_handle_movement(keys_pressed, yellow):
                        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
                            yellow.x -= VEL
                        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
                            yellow.x += VEL
                        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
                            yellow.y -= VEL
                        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT1 - 15:  # DOWN
                            yellow.y += VEL


                    def red_handle_movement(keys_pressed, red):
                        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
                            red.x -= VEL
                        if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH1:  # RIGHT
                            red.x += VEL
                        if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
                            red.y -= VEL
                        if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT1 - 15:  # DOWN
                            red.y += VEL


                    def handle_bullets(yellow_bullets, red_bullets, yellow, red):
                        for bullet in yellow_bullets:
                            bullet.x += BULLET_VEL
                            if red.colliderect(bullet):
                                pygame.event.post(pygame.event.Event(RED_HIT))
                                yellow_bullets.remove(bullet)
                            elif bullet.x > WIDTH1:
                                yellow_bullets.remove(bullet)

                        for bullet in red_bullets:
                            bullet.x -= BULLET_VEL
                            if yellow.colliderect(bullet):
                                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                                red_bullets.remove(bullet)
                            elif bullet.x < 0:
                                red_bullets.remove(bullet)


                    def draw_winner(text):
                        draw_text = WINNER_FONT.render(text, 1, WHITE)
                        WIN.blit(draw_text, (WIDTH1/2 - draw_text.get_width() /
                                2, HEIGHT1/2 - draw_text.get_height()/2))
                        positsies[beurt] = positsies[beurt] +1
                        pygame.display.update()
                        positsies[beurt] = positsies[beurt] -1
                        pygame.time.delay(5000)


                    def main():
                        red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
                        yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

                        red_bullets = []
                        yellow_bullets = []

                        red_health = 10
                        yellow_health = 10

                        clock = pygame.time.Clock()

                        run = True
                        while run:
                            clock.tick(FPS)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    run = False
                                    pygame.quit()

                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                                        yellow_bullets.append(bullet)
                                        

                                    if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                                        bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                                        red_bullets.append(bullet)
                                        

                                if event.type == RED_HIT:
                                    red_health -= 1
                                    BULLET_HIT_SOUND.play()

                                if event.type == YELLOW_HIT:
                                    yellow_health -= 1
                                    BULLET_HIT_SOUND.play()

                            winner_text = ""
                            if red_health <= 0:
                                winner_text = "Yellow Wins!"

                            if yellow_health <= 0:
                                winner_text = "Red Wins!"

                            if winner_text != "":
                                draw_winner(winner_text)
                                pygame.quit()

                            keys_pressed = pygame.key.get_pressed()
                            yellow_handle_movement(keys_pressed, yellow)
                            red_handle_movement(keys_pressed, red)

                            handle_bullets(yellow_bullets, red_bullets, yellow, red)

                            draw_window(red, yellow, red_bullets, yellow_bullets,red_health, yellow_health)

                        main()


                    if __name__ == "__main__":
                        main()
                    
                
                #winst
                elif positsies[beurt] >= 73:
                    positsies[beurt] = 73
                    print("gewonnen")
                    gewonnen = True

                #put-tegel. Als de actieve speler hier op komt dan gaat hij achter uit
                elif positsies[beurt]== 9 or positsies[beurt] == 20 or positsies[beurt] == 53 or positsies[beurt] == 60 or positsies[beurt] == 66:
                    put()
                     
               #opdracht kaarten
                elif positsies[beurt] == 2 or positsies[beurt] == 6 or positsies[beurt] == 11 or positsies[beurt] == 15 or positsies[beurt] == 18 or positsies[beurt] == 24 or positsies[beurt] == 30 or positsies[beurt] == 35 or positsies[beurt] == 38 or positsies[beurt] == 41 or positsies[beurt] == 47 or positsies[beurt] == 52 or positsies[beurt] == 55 or positsies[beurt] == 58 or positsies[beurt] == 62 or positsies[beurt] == 69:
                    print("pak een opdracht kaart")
                    #maak een pup up melding met een random kaart waar ze 
                    #iets kunnen in vullen wat wordt opgeslagen en aan het eind wordt gedeeld

                elif positsies[beurt] == 31:
                    Brug = naamfont.render(f"{spelers[beurt]} komt op 31 en neemt de brug", 1, (0,0,0))
                    scherm.blit(Brug, (326,567))
                    pygame.display.flip()
                    time.sleep(3)
                    positsies[beurt] = 45
                
                #put-tegel passiefe speler. Als de pasiefe speler op de put komt moet diet ook uit gevoerd worden.  
                if beurt == 0:
                    beurt = 3
                    put()
                    beurt = 0
                elif beurt == 1:
                    beurt = 0
                    put()
                    beurt = 1
                elif beurt ==2:
                    beurt = 1
                    put()
                    beurt = 2
                elif beurt == 3:
                    beurt = 2
                    put()
                    beurt = 3
                 

                if beurt == 0:
                    beurt = 1 
                elif beurt == 1:
                    beurt = 2
                elif beurt == 2:
                    beurt = 3
                elif beurt == 3:
                    beurt = 0 
            
            elif event.key == pygame.K_BACKSPACE:
                positsies = [0,0,0,0]
                beurt = 0
            if gewonnen == True:
                klaar = True
                print("het werkt")
                #Maak een popup medling met dat de game klaar is, zeg wie heeft gewonnen, wil je opnieuw
                #geef van ideereen de andwoorde weer. 
            
            

    pygame.display.flip()



pygame.display.flip()


pygame.quit()