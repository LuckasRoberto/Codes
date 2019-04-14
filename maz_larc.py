import pygame
import time
import random

WIDTH = 500
HEIGHT = 500
FPS = 30 

#Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
VERDE = (0 , 255, 0)
CINZA = (40, 40, 40)

#PYGAME
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze")
clock = pygame.time.Clock()

#Setup
x = 0
y = 0
w = 20
grade = []
visitado = []
stack = []
solucao = {}

# Construir a Grade
def build_grade(x, y, w):
    for i in range(1,21):
        x = 20
        y = y + 20
        for j in range(1,21):
            pygame.draw.line(screen, BRANCO, [x, y], [x+w, y])
            pygame.draw.line(screen, BRANCO, [x+w, y], [x+w, y+w])
            pygame.draw.line(screen, BRANCO, [x+w, y+w], [x, y+w])
            pygame.draw.line(screen, BRANCO, [x, y+w], [x, y]) 
            grade.append((x,y))
            x = x + 20

def para_cima(x, y):
    pygame.draw.rect(screen, CINZA, (x + 1, y - w + 1, 19, 39), 0)  # Desenha um retangulo do dobro do tamnho da cell
    pygame.display.update() # animação :v
def para_baixo(x, y):
    pygame.draw.rect(screen, CINZA, (x +  1, y + 1, 19, 39), 0)
    pygame.display.update()
def para_esquerda(x, y):
    pygame.draw.rect(screen, CINZA, (x - w +1, y +1, 39, 19), 0)
    pygame.display.update()
def para_direita(x, y):
    pygame.draw.rect(screen, CINZA, (x +1, y +1, 39, 19), 0)
    pygame.display.update()

def uma_cell(x, y):
    pygame.draw.rect(screen, VERMELHO, (x +1, y +1, 18, 18), 0)    # Desenha um dos quadrados
    pygame.display.update()
  

def backtracking_cell(x, y):
    pygame.draw.rect(screen, CINZA, (x + 1, y +1, 18, 18), 0)
    pygame.display.update()


def solucao_cell(x, y):
    pygame.draw.ellipse(screen, AMARELO, (x+8, y+8, 5, 5), 0)   # Solução do labirinto
    pygame.display.update()

def solucao_cell_2(x, y):
    pygame.draw.ellipse(screen, VERDE, (x+8, y+8, 5, 5), 0)
    pygame.display.update()



def running_away(x, y):
    uma_cell(x, y)
    stack.append((x, y))
    visitado.append((x,y))
    while len(stack) > 0:
        time.sleep(.0007)
        cell = []
        if (x + w, y) not in visitado and (x + w, y) in grade:       
            cell.append("direita")                                   

        if (x - w, y) not in visitado and (x - w, y) in grade:     
            cell.append("esquerda")

        if (x , y + w) not in visitado and (x , y + w) in grade:     
            cell.append("baixo")

        if (x, y - w) not in visitado and (x , y - w) in grade:    
            cell.append("cima")


        if len(cell) > 0:                                   
            cell_chosen = (random.choice(cell))                    

            if cell_chosen == "direita":                             
                para_direita(x, y)                                   
                solucao[(x + w, y)] = x, y  
                x = x + w                                         
                visitado.append((x, y))                         
                stack.append((x, y))                           

            elif cell_chosen == "esquerda":
                para_esquerda(x, y)
                solucao[(x - w, y)] = x, y
                x = x - w
                visitado.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "baixo":
                para_baixo(x, y)
                solucao[(x , y + w)] = x, y
                y = y + w
                visitado.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "cima":
                para_cima(x, y)
                solucao[(x , y - w)] = x, y
                y = y - w
                visitado.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()                                    
            uma_cell(x, y)                                     
            time.sleep(.0007)                                       
            backtracking_cell(x, y)


def plot_caminho_de_volta(x, y):
    solucao_cell(x, y)
    while (x, y) != (400,400):
        x, y = solucao[x, y]
        solucao_cell(x, y)
        time.sleep(.01)

def plot_caminho_de_volta_2(x2, y2):
    solucao_cell_2(x2, y2)
    while (x2, y2) != (20, 20):
        x2, y2 = solucao[x2, y2]
        solucao_cell_2(x2, y2)
        time.sleep(.01)

#a = [20, 40, 80, 100, 400]
#x, y = random.choice(a), random.choice(a)
x, y = 400, 400
build_grade(40, 0, 20)
running_away(x, y)
plot_caminho_de_volta(20, 20)
x2, y2 = 20, 20
plot_caminho_de_volta_2(400, 400)


# pygame loop
running = True
while running:
    # mantem rodando na velocidade certa
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



