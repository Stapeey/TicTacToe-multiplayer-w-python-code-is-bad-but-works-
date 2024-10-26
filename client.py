import pygame, sys, tkinter, socket, threading

response = 0
won = False
root = tkinter.Tk()
root.geometry("600x600")

def myClick():
    global ip
    global port
    global pw
    global h
    global root
    global PORT, IP, PASSWORD, HOST
    PORT = port.get()
    IP = ip.get()
    PASSWORD = pw.get()
    if h.get().upper() == 'host'.upper():
        HOST = True
    else:
        HOST = False
    root.destroy()

tkinter.Label(root,text="IP",width=300).pack()
ip = tkinter.Entry(root, width=50)
ip.pack()
tkinter.Label(root,text="", height=3).pack()
tkinter.Label(root,text="PORT",width=300).pack()
port = tkinter.Entry(root, width=50)
port.pack()
tkinter.Label(root,text="", height=3).pack()
tkinter.Label(root,text="password",width=300).pack()
pw = tkinter.Entry(root, width=50)
pw.pack()
tkinter.Label(root,text="", height=3).pack()
tkinter.Label(root,text="Host vagy Join",width=300).pack()
h = tkinter.Entry(root, width=50)
h.pack()
mehet = tkinter.Button(root, text="MEHET!", command=myClick, width=70, height=30).pack()
root.mainloop()
connected = False
'''IP = '192.168.0.184'
PORT = 5555
HOST = True'''
        
def respond(csatl,h):
    global response
    if not won: 
        response = csatl.recv(1024).decode('utf-8')
        response = [int(i) for i in response.split()]
            

def game(csatl,h):
    global game_turn
    global move
    global response
    global kereszt_list
    global kor_list
    global turn
    global negyzet_list
    global kor
    global kereszt
    global font1
    global score1
    global score2
    global pont1
    global pont2
    global drawn
    global winner
    global clicked
    global delay
    Realresponse = 0
    pont1 = "0"; pont2 = "0"
    pygame.init()
    def win():
        global text
        global textRect
        global winner
        pygame.draw.rect(screen, (0,255,255), pygame.Rect(border-10, border-10, 2*(area+grid)+area+20, 2*(area+grid)+area+20))
        font = pygame.font.Font('freesansbold.ttf', 70)
        text = font.render(f'{winner} nyerte a kört!', True, (0,255,0), (0,125,255))
        textRect = text.get_rect()
        textRect.center = (width //2, height // 4)
        screen.blit(text, textRect)

    def draw():
        global text
        global textRect
        global winner
        pygame.draw.rect(screen, (0,255,255), pygame.Rect(border-10, border-10, 2*(area+grid)+area+20, 2*(area+grid)+area+20))
        font = pygame.font.Font('freesansbold.ttf', 70)
        text = font.render('Döntetlen a kör!', True, (0,255,0), (0,125,255))
        textRect = text.get_rect()
        textRect.center = (width //2, height // 4)
        screen.blit(text, textRect)


    def restart():
        global game_turn
        global HOST
        global kereszt_list
        global kor_list
        global turn
        global negyzet_list
        global kor
        global kereszt
        global font1
        global score1
        global score2
        global pont1
        global pont2
        global drawn
        global delay
        if HOST:
            game_turn = True
            turn = "kor"
        else:
            game_turn = False
            turn = "kereszt"
            responder = threading.Thread(target=respond, args=(csatl,10))
            responder.start()
        delay = False
        font1 = pygame.font.Font('freesansbold.ttf', 40)

        drawn = False
        screen.fill((0,255,255))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(border,border,width-2*border,height-2*border))
        negyzet_list = []
        for j in range(3):
            for i in range(3):
                pygame.draw.rect(screen, (0,255,255), pygame.Rect(border+i*(area+grid), border+j*(area+grid),area,area))
                negyzet_list.append(pygame.Rect(border+i*(area+grid), border+j*(area+grid),area,area))
        kereszt = pygame.image.load("X.png")
        kereszt = pygame.transform.scale(kereszt,(area,area))
        kereszt_list = []
        kor = pygame.image.load("C.png")
        kor = pygame.transform.scale(kor,(area,area))
        kor_list = []
        score1= font1.render(pont1, True, (255,0,0), (0,255,255))
        score2= font1.render(pont2, True, (255,0,0), (0,255,255))
        screen.blit(score1, textRect3)
        screen.blit(score2, textRect4)
        screen.blit(player1, textRect1)
        screen.blit(player2, textRect2)

    def suck(lista):
        mama = []
        mama = [i[0:2] for i in lista]
        if [100,100] in mama:
            if [320, 320] in mama:
                if [540, 540] in mama:
                    pygame.draw.line(screen, (0,0,0),(border,border),(border+2*(area+grid)+area, border+2*(area+grid)+area), 10)
                    return True
        if [100,540] in mama:
            #ezt a szart nem érzékeli vmiért
            #az elifet kicseréltem és most jó wtf
            if [320, 320] in mama:
                if [540, 100] in mama:
                    pygame.draw.line(screen, (0,0,0),(border, border+2*(area+grid)+area),(border+2*(area+grid)+area,border), 10)
                    return True

    def keresztbe_van_e(lista):
        new_list = []
        for i in lista:
            new_list.append(i[1])
        a = 0; b = 0; c = 0
        for j in new_list:
            if j == 100:
                a += 1
            elif j == 320:
                b += 1
            else:
                c += 1
        if a >= 3:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(border+grid/4, border+0*area+area/2-grid/4, 3*area+2*grid-grid/2, grid/2))
            return True
        elif b >= 3:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(border+grid/4, border+1*(area+grid)+area/2-grid/4, 3*area+2*grid-grid/2, grid/2))
            return True
        elif c >= 3:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(border+grid/4, border+2*(area+grid)+area/2-grid/4, 3*area+2*grid-grid/2, grid/2))
            return True

    def fuggolegesbe_van_e(lista):
        new_list = []
        for i in lista:
            new_list.append(i[0])
        a = 0; b = 0; c = 0
        for j in new_list:
            if j == 100:
                a += 1
            elif j == 320:
                b += 1
            else:
                c += 1
        if a >= 3:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(border+0*area+area/2-grid/4, border+grid/4, grid/2, 3*area+2*grid-grid/2))
            return True
        elif b >= 3:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(border+1*(area+grid)+area/2-grid/4, border+grid/4, grid/2, 3*area+2*grid-grid/2))
            return True
        elif c >= 3:
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(border+2*(area+grid)+area/2-grid/4, border+grid/4, grid/2, 3*area+2*grid-grid/2))
            return True

    border = 100
    grid = 20
    area = 200
    width, height = 2*border+2*grid+3*area, 2*border+2*grid+3*area
    size = (width,height)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    won = False
    a = 0
    next = False
    b = 0

    font1 = pygame.font.Font('freesansbold.ttf', 40)
    pont1 = "0"; pont2 = "0"
    score1= font1.render(pont1, True, (255,0,0), (0,255,255))
    score2= font1.render(pont2, True, (255,0,0), (0,255,255))
    textRect3 = score1.get_rect()
    textRect3.topright = (width, grid+45)
    textRect4 = score2.get_rect()
    textRect4 = (0,grid+45)
    player1= font1.render('Circle Guy', True, (255,0,0), (0,255,255))
    textRect1 = player1.get_rect()
    textRect1.topright = (width, grid)
    player2= font1.render('Cross Guy', True, (255,0,0), (0,255,255))
    textRect2 = player2.get_rect()
    textRect2 = (0,grid)
    clicked = False
    restart()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
        if won:
            a += 1
            if a >= 50:
                next = True
                a = 0
                won = False
                if drawn:
                    drawn = False
                    draw()
                else:
                    win()
        if next:
            b += 1
            if b == 100:
                b = 0
                next = False
                restart()
        if clicked:
            a+=1
            if a == 25:
                a = 0
                clicked = False
        #nem kell külön listener mert másik jön akkro
        #+ legyen a click check előtt egy ha my turn és ott a listening + draw
        #+ elejeére if len negyzetlist == 9 akkor delay és akkor 100%, h nem fog fuck upolni a socket
        if negyzet_list == []:
            game_turn = True
        if len(negyzet_list) == 9 and not delay:
            clicked = True
            delay = True
        if not won and not next:
            if not game_turn:
                if response != 0:
                    for i in negyzet_list:
                        if i[0:] == response:
                            response = 0
                            game_turn = True
                            if HOST:
                                screen.blit(kereszt, i[0:2])
                                negyzet_list.remove(i)
                                kereszt_list.append(i)
                            if not HOST:
                                screen.blit(kor, i[0:2])
                                negyzet_list.remove(i)
                                kor_list.append(i)
                            if keresztbe_van_e(kor_list):
                                pont1 = int(pont1)+1
                                pont1 = str(pont1)
                                score1= font1.render(pont1, True, (255,0,0), (0,255,255))
                                screen.blit(score1, textRect3)
                                winner = "Circle Guy"
                                won = True
                                clicked = True
                            elif fuggolegesbe_van_e(kor_list):
                                pont1 = int(pont1)+1
                                pont1 = str(pont1)
                                score1= font1.render(pont1, True, (255,0,0), (0,255,255))
                                screen.blit(score1, textRect3)
                                winner = "Circle Guy"
                                won = True
                                clicked = True
                            elif negyzet_list == []:
                                drawn = True
                                won = True
                                clicked = True
                            elif keresztbe_van_e(kereszt_list):
                                pont2 = int(pont2)+1
                                pont2 = str(pont2)
                                score2= font1.render(pont2, True, (255,0,0), (0,255,255))
                                screen.blit(score2, textRect4)
                                winner = "Cross Guy"
                                won = True
                                clicked = True
                            elif fuggolegesbe_van_e(kereszt_list):
                                pont2 = int(pont2)+1
                                pont2 = str(pont2)
                                score2= font1.render(pont2, True, (255,0,0), (0,255,255))
                                screen.blit(score2, textRect4)
                                winner = "Cross Guy"
                                won = True
                                clicked = True
                            elif suck(kereszt_list):
                                pont2 = int(pont2)+1
                                pont2 = str(pont2)
                                score2= font1.render(pont2, True, (255,0,0), (0,255,255))
                                screen.blit(score2, textRect4)
                                winner = "Cross Guy"
                                won = True
                                clicked = True
                            elif suck(kor_list):
                                pont1 = int(pont1)+1
                                pont1 = str(pont1)
                                score1= font1.render(pont1, True, (255,0,0), (0,255,255))
                                screen.blit(score1, textRect3)
                                winner = "Circle Guy"
                                won = True
                                clicked = True

                            #ez pedig egy threadbe ami returnöl 
                            #márcsak ha 9 azt kell megodlani
                else:
                    pygame.event.pump()
                    clicked = True
            if not clicked:
                if pygame.mouse.get_pressed()[0]:
                    clicked = True
                    mousepos_whenclicking = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],1,1)
                    for i in negyzet_list:
                        if mousepos_whenclicking in i:
                            move = " ".join([str(j) for j in i[0:]])
                            game_turn = False
                            if turn == "kor":
                                screen.blit(kor, i[0:2])
                                kor_list.append(i)
                                negyzet_list.remove(i)
                            elif turn == "kereszt":
                                screen.blit(kereszt, i[0:2])
                                negyzet_list.remove(i)
                                kereszt_list.append(i)
                            if keresztbe_van_e(kor_list):
                                csatl.send(move.encode('utf-8'))
                                pont1 = int(pont1)+1
                                pont1 = str(pont1)
                                score1= font1.render(pont1, True, (255,0,0), (0,255,255))
                                screen.blit(score1, textRect3)
                                winner = "Circle Guy"
                                won = True
                                clicked = False
                            elif fuggolegesbe_van_e(kor_list):
                                csatl.send(move.encode('utf-8'))
                                pont1 = int(pont1)+1
                                pont1 = str(pont1)
                                score1= font1.render(pont1, True, (255,0,0), (0,255,255))
                                screen.blit(score1, textRect3)
                                winner = "Circle Guy"
                                won = True
                                clicked = False
                            elif suck(kor_list):
                                csatl.send(move.encode('utf-8'))
                                pont1 = int(pont1)+1
                                pont1 = str(pont1)
                                score1= font1.render(pont1, True, (255,0,0), (0,255,255))
                                screen.blit(score1, textRect3)
                                winner = "Circle Guy"
                                won = True
                                clicked = False
                            elif negyzet_list == []:
                                csatl.send(move.encode('utf-8'))
                                drawn = True
                                won = True
                                clicked = False
                            elif keresztbe_van_e(kereszt_list):
                                csatl.send(move.encode('utf-8'))
                                pont2 = int(pont2)+1
                                pont2 = str(pont2)
                                score2= font1.render(pont2, True, (255,0,0), (0,255,255))
                                screen.blit(score2, textRect4)
                                winner = "Cross Guy"
                                won = True
                                clicked = False
                            elif fuggolegesbe_van_e(kereszt_list):
                                csatl.send(move.encode('utf-8'))
                                pont2 = int(pont2)+1
                                pont2 = str(pont2)
                                score2= font1.render(pont2, True, (255,0,0), (0,255,255))
                                screen.blit(score2, textRect4)
                                winner = "Cross Guy"
                                won = True
                                clicked = False
                            elif suck(kereszt_list):
                                csatl.send(move.encode('utf-8'))
                                pont2 = int(pont2)+1
                                pont2 = str(pont2)
                                score2= font1.render(pont2, True, (255,0,0), (0,255,255))
                                screen.blit(score2, textRect4)
                                winner = "Cross Guy"
                                won = True
                                clicked = False
                            else:
                                responder = threading.Thread(target=respond, args=(csatl,10))
                                responder.start()
                                csatl.send(move.encode('utf-8'))
        pygame.display.flip()
        clock.tick(60)

if HOST:
    del tkinter
    game_turn = True
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, int(PORT)))
    server.listen(1)
    while not connected:
        conn, addr = server.accept()
        if conn:
            connected = False
            games = threading.Thread(target=game, args=(conn,10))
            games.start()
else:
    del tkinter
    game_turn = False
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, int(PORT)))
    games = threading.Thread(target=game, args=(client,10))
    responder = threading.Thread(target=respond, args=(client,10))
    games.start()
    responder.start()