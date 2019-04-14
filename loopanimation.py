import pygame
import pickle
import sys
from numpy import *
from pygame.locals import *
from pygame.color import *
import pickle 
from numpy import * #modulo de matematica
import matplotlib.pyplot as plt #modulo para plotar graficos
from numba import njit #modulo para acelerar a velocidade das contas
import time as timehandler # modulo para dar as horas
t = timehandler.localtime()  # objeto de tempo
h = t.tm_hour #hora atual
m = t.tm_min #minuto atual
s = t.tm_sec #segundo atual
print(str(h) + ":" + str(m)+":"+str(s)) #cria identificador da simulacao utilizando o tempo atual
#Arquivo de saida dos dados
saidanome = str(h) + "-"+str(m)+"-"+str(s)+"-loopsimulation.iypt" #cria um nome pro arquivo utilizando o identificador. O arquivo tem formato .iypt
#Variaveis iniciais
#TODOS OS VALORES EM SI
dt = 0.000001 #tamanho do dt
t = 0
alpha = pi/2
theta = pi - alpha
alphaponto = 0
thetaponto = 0
thetadoispontos = 0
m = 0.034 #massa
M = 0.253 #massa maior
l = 1.0 #tamanho inicial do fio exposto do lado da massa menor
lponto = 0
ldoispontos = 0
h = 0 #medida da poiscao do massa maior, assumindo que a posicao inicial como referencial zero
hponto = 0
hdoispontos = 0
g = 9.72 #gravidade local
r = 0.008 #raio da barra
mi = 0.18 # coeficiente de atrito
#Texto com os valores utilizados na configuracao da simulacao. Serve para referencias futuras
configtext = "dt = " + str(dt) + "\nalpha = " + str(alpha) + "\nm = " + str(m) + "\nM = " + str(M) + "\nl = " + str(l) + "\ng = " + str(g)
configtext += "\nr = " + str(r) + "\nmi = " + str(mi)
#valores padrao inicialmente para as aceleracoes
alphadoispontos = 0
thetadoispontos = 0
ldoispontos = 0
hdoispontos = 0
#Lista onde os dados vão ser armazenados
tdata = []
ldata = []
hdata = []
alphadata = []
thetadata = []
alphapontodata = []
alphadoispontosdata = []
#fase1 -> comeco do fenomeno
#@njit(debug=True,fastmath = True,parallel=True)
def fase1():
    #chama as variaveis que ficarao global ao programa
    global dt,t,alpha,alphaponto,alphadoispontos,theta,thetaponto,thetadoispontos,m,M,l,lponto,ldoispontos,h,hponto,hdoispontos,g,r,mi,T1,T2
    # Cálculo das equações de segunda ordem, elas servem de base para a resolucao
    alphadoispontos = (-g*sin(alpha) - 2 * lponto * alphaponto)/l
    T2 = (g*(1+cos(alpha))+ (alphaponto**2)*l - alphadoispontos*r)/((exp(mi*theta)/m)+(1/M))
    T1 = T2*exp(mi*theta)
    ldoispontos = (alphaponto**2)*l + g*cos(alpha) - (T1/m)
    hdoispontos = g - (T2/M)
    thetadoispontos = -alphadoispontos
    #Com a segunda ordem calculada analiticamente neste instante, integra-se para chegar na primeira ordem
    lponto += ldoispontos * dt
    hponto += hdoispontos * dt
    thetaponto += thetadoispontos*dt
    alphaponto += alphadoispontos*dt
    #Integra-se novamente para chegar na ordem zero (as proprias variaveis)
    l += lponto * dt
    h += hponto * dt
    alpha += alphaponto * dt
    theta += thetaponto*dt
    t += dt
    #Salva-se os dados em cada instante nas listas
    tdata.append(t)
    ldata.append(l)
    hdata.append(h)
    alphadata.append(alpha)
    thetadata.append(theta)
    alphapontodata.append(alphaponto)
    alphadoispontosdata.append(alphadoispontos)
#fase 2 -> a massa M parou e agora o sistema virou um pendulo ao redor da barra
def fase2():
    global dt,t,alphaponto,alpha,alphadoispontos,theta,thetaponto,thetadoispontos,m,M,l,lponto,ldoispontos,h,hponto,hdoispontos,g,r,mi,T1,T2
    #Variaveis de segunda ordem calculadas
    alphadoispontos = (-g*sin(alpha) - 2 * lponto * alphaponto)
    thetadoispontos = - alphadoispontos
    ldoispontos = alphadoispontos * r
    hdoispontos = 0 
    hponto = 0
    #Integracao para chegar na primeira ordem
    lponto += ldoispontos * dt
    hponto += hdoispontos * dt
    thetaponto += thetadoispontos*dt
    alphaponto += alphadoispontos*dt
    #Integracao final
    l += lponto * dt
    h += hponto * dt
    alpha += alphaponto * dt
    theta += thetaponto*dt
    t += dt
    #Salvar os dados
    tdata.append(t)
    ldata.append(l)
    hdata.append(h)
    alphadata.append(alpha)
    thetadata.append(theta)
    alphapontodata.append(alphaponto)
    alphadoispontosdata.append(alphadoispontos)
ultimot = 0
while True: #enquanto a massa de baixo estiver acelerando
    fase1()
    if t-ultimot > 0.01: #printar a cada 0.01 segundos
        print(str(t) + " " + str(l)+ "\r",end="")
        ultimot = t
    if l <= 0 or abs(hdoispontos) < 0.001: #se o l acabar ou a massa parar de acelerar
        #print(l,hdoispontos)
        print()
        print("Simulacao da Fase 1 finalizada")
        #Equação de transição -> Quando M para de cair lponto perde velocidade
        lponto=alphaponto*r
        break
while l >= 0.00001: #enquanto ainda tiver l
    fase2()
    if t-ultimot > 0.01: #printar a cada 0.01 segundos
        print(str(t) + " " + str(l)+ "\r",end="")
        ultimot = t
print()
print("Simulacao da Fase 2 finalizada")
#print(ldata)
finaldata = [tdata,ldata,hdata,alphadata,thetadata,alphapontodata,alphadoispontosdata] #dados a serem guardados
pickle.dump(finaldata,open(saidanome,"wb")) #funcao do pickle que  cria o arquivo e salva os dados
print("Arquivo de saida salvo")
configtext += "\nt = " + str(t) #texto com os valores utilizados
configname = saidanome.replace(".iypt",".log")
arquivoconfig = open(configname,"w") #salva-se o arquivo
arquivoconfig.write(configtext)
arquivoconfig.close()
print("Arquivo de log salvo")

#Animação

dt = tdata[1]-tdata[0] #calcula o dt utilizado
framerate = 30 #definicao do framerate da animacao
velocidade = 0.1 #a razao entre o tempo real e o tempo na animacao
frequencia = velocidade/framerate
quant = round(frequencia/dt,0)
def extract(quantity,lista):
    return [i for a,i in enumerate(lista) if a % quantity == 0] #extrai dados da lista no intervalo que se quer
#arquivos novos com dados apenas de cada frame (e nao todos os dados disponiveis)
newtdata = extract(quant,tdata)
newldata = extract(quant,ldata)
newhdata = extract(quant,hdata)
newalphadata = extract(quant,alphadata)
newthetadata = extract(quant,thetadata)
newalphapontodata = extract(quant,alphapontodata)
newalphadoispontosdata = extract(quant,alphadoispontosdata)
pygame.init() #inicializa o pygame
screen = pygame.display.set_mode((1000, 750)) #tamanho da tela
clock = pygame.time.Clock()
running = True
framecount = 0
limit = len(newtdata) #limite de frames
#Posicao da barra na tela
xo = 400
yo = 300
hbase = 30 #tamanho da corda h
k = 500 #escala entre pixel e metro (px/m)
def inteirar(x):
    return int(round(x,0))
while running:
    #Codigo para encerrar caso se aperte o botao de fechar a tela
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.fill((255,255,255))
    #desenhar o l, a barra fica em (xo,yo)
    t,l,h,alpha,theta = newtdata[framecount],newldata[framecount],newhdata[framecount],newalphadata[framecount],newthetadata[framecount]
    #Calculo dos dois pontos que definem uma reta
    l1 = (xo,yo)
    l2 = ((l*sin(pi-alpha))*k+xo,(-l*cos(pi-alpha)*k+yo))
    # as coordenadas devem ser inteiras
    l1 = [inteirar(i) for i in l1]
    l2 = [inteirar(i) for i in l2]
    pygame.draw.line(screen,(0,0,0),l1,l2) #desenha a linha
    #desenhar o h
    h1 = (xo,yo)
    h2 = (xo,yo+k*h)
    h1 = [inteirar(i) for i in h1]
    h2 = [inteirar(i) for i in h2]
    pygame.draw.line(screen,(0,0,0),h1,h2)
    #desenha pontos adicionais]
    pygame.draw.circle(screen,(60, 60, 60),l2,10) #m
    pygame.draw.circle(screen,(40, 40, 40),h2,20) #M
    pygame.draw.circle(screen,(20, 30, 30),(xo,yo),10) #barra
    pygame.display.flip() #atualiza o frame
    clock.tick(framerate) #mantem o programa no framerate correto
    framecount += 1
    if framecount >= limit: #encerra se tiver chegado ao final
        break
    pygame.display.flip()
pygame.quit()


#Graficos

import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(ldata,alphadata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(ldata):
        l = ldata[a]
        alpha = alphadata[a]
        #calculo das coordenadas de cada ponto geometricamente a partir de suas coordenadas polares
        y = l*sin(-(pi/2 + alpha))
        x = -l*cos(-(pi/2 + alpha))
        paresx.append(x)
        paresy.append(y)
    return paresx,paresy
parx,pary = process(ldata,alphadata)
plt.title("Curva do espaço da massa menor")
plt.ylabel("Y(m)")
plt.xlabel("X(m)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot


import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(ldata,alphadata,tdata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(ldata):
        l = ldata[a]
        alpha = alphadata[a]
        t = tdata[a]
        #calculo das coordenadas de cada ponto geometricamente a partir de suas coordenadas polares
        x = -l*cos(-(pi/2 + alpha))
        paresx.append(t)
        paresy.append(x)
    return paresx,paresy
parx,pary = process(ldata,alphadata,tdata)
plt.title("Curva da coordenada x(t)")
plt.ylabel("X(m)")
plt.xlabel("Tempo(t)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot


import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(ldata,alphadata,tdata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(ldata):
        l = ldata[a]
        alpha = alphadata[a]
        t = tdata[a]
        #calculo das coordenadas de cada ponto geometricamente a partir de suas coordenadas polares
        y = l*sin(-(pi/2 + alpha))
        paresx.append(t)
        paresy.append(y)
    return paresx,paresy
parx,pary = process(ldata,alphadata,tdata)
plt.title("Curva da coordenada y(t)")
plt.ylabel("Y(m)")
plt.xlabel("Tempo(t)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot


import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(alphadata,tdata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(alphadata):
        alpha = alphadata[a]
        t = tdata[a]
        paresx.append(t)
        paresy.append(alpha)
    return paresx,paresy
parx,pary = process(alphadata,tdata)
plt.title("Curva de alpha(t)")
plt.ylabel("alpha (°)")
plt.xlabel("t (s)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot


import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(alphapontodata,tdata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(alphapontodata):
        alphaponto = alphapontodata[a]
        t = tdata[a]
        paresx.append(t)
        paresy.append(alphaponto)
    return paresx,paresy
parx,pary = process(alphapontodata,tdata)
plt.title("Curva de alphaponto(t)")
plt.ylabel("alphaponto (m/s)")
plt.xlabel("t (s)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot


import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(alphadoispontosdata,tdata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(alphadoispontosdata):
        alphadoispontos = alphadoispontosdata[a]
        t = tdata[a]
        paresx.append(t)
        paresy.append(alphadoispontos)
    return paresx,paresy
parx,pary = process(alphadoispontosdata,tdata)
plt.title("Curva de alphadoisponto(t)")
plt.ylabel("alphadoispontos (m/s^2)")
plt.xlabel("t (s)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot


import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(ldata,tdata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(ldata):
        l = ldata[a]
        t = tdata[a]
        paresx.append(t)
        paresy.append(l)
    return paresx,paresy
parx,pary = process(ldata,tdata)
plt.title("Curva de l(t)")
plt.ylabel("l (m)")
plt.xlabel("t (s)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot



import matplotlib.pyplot as plt #biblioteca de fazer grafico
@njit(debug=True,fastmath = True) #acelera a funcao ao compila-la para codigo de maquina
def process(hdata,tdata):
    paresx = [] #coordenadas x
    paresy = [] #coordenadas y
    for a,i in enumerate(hdata):
        h = hdata[a]
        t = tdata[a]
        paresx.append(t)
        paresy.append(h)
    return paresx,paresy
parx,pary = process(hdata,tdata)
plt.title("Curva de h(t)")
plt.ylabel("h (m)")
plt.xlabel("t (s)")
plt.plot(parx,pary) #plota os pontos
plt.show() #mostra o plot numa telinha propria
plt.clf() #limpa o plot









