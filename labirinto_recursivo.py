import numpy as np

#Estrutura Principal do Labirinto
grid = [[1, 1, 0, 1, 0, 2],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 0]]
        
#Algoritmo Recursivo de explorar o Labirinto
def recursive_walk(x, y):
    if grid[x][y] == 2:
        print ("Encontrado em:", x, y)
        return True
    
    elif grid[x][y] == 1:
        print ("Parede em:", x, y)
        return False

    elif grid[x][y] == 3:
        print ("Visitado em:", x, y)
        return False
    
    print ("Visitando em:", x, y)

    # marca como visitado
    grid[x][y] = 3

    # explora os vizinhos no sentido horario, começando pela direita
    if ((x < len(grid)-1 and recursive_walk(x+1, y))
        or (y > 0 and recursive_walk(x, y-1))
        or (x > 0 and recursive_walk(x-1, y))
        or (y < len(grid)-1 and recursive_walk(x, y+1))):
    		return True

    return False

recursive_walk(5, 0)

print()
print("Da uma olhada no labirinto")
print(np.matrix(grid))