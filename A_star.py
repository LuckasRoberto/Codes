import numpy as np

class Node():
    """Nodos para os Grafos do A* """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Retorna um array de tuples, representando o caminho do inicio do labirinto ate o objetivo"""

    # Cria os Nodos de Inicio e Fim
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Cria a lista aberta e a lista fechada
    open_list = []
    closed_list = []

    # Adiciona o Nodo inicial
    open_list.append(start_node)

    # Loop até o encontrar o fim
    while len(open_list) > 0:

        # Obtem o Nodo atual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Retira da lista aberta e adiciona na lista fechada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Encontra o objetivo
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Faz o Backtracking até o nodo inicial

        # Cria o Filho
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Vizinhos/direções

            # Obtém o nodo da posição atual
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Ctz que está no range de possibilidades
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Ctz que é um caminho possivel de se fazer
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Cria novo Nodo
            new_node = Node(current_node, node_position)

            # Coloca no array do filho
            children.append(new_node)

        # Loop pelo Filho
        for child in children:

            # Filho está na lista fechada
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Cria o valor das variaveis f, g e h 
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **2) + ((child.position[1] - end_node.position[1]) **2)
            child.f = child.g + child.h

            # Filho na lista Aberta
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Adiciona Filho na lista aberta
            open_list.append(child)


def main():

    maze = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    start = (0, 0)
    end = (4, 1)

    path = astar(maze, start, end)

    print(path)
    print()

    print("Movimentos:")
    print()
    for i in range(0, len(path)):

        if path[i] == end:
            break

        elif path[i][0] + 1 == path[i+1][0]:
            print("down")

        elif path[i][0] - 1 == path[i+1][0]:
            print("up")

        elif path[i][1] + 1 == path[i+1][1]:
            print("right")

        elif path[i][1] - 1 == path[i+1][1]:
            print("left")

        else:
            print("yyy")

    print()
    print(np.matrix(maze))


if __name__ == '__main__':
    main()