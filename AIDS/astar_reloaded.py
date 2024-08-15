import time

start_time = time.localtime()


initialstate = [[1, 3, 4], [8, 6, 2], [7, 0, 5]]
finalstate = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

inputkarnahai = int(
    input("Its the hardest problem. \nDo you want to give Custom input? 0/1: ")
)

if inputkarnahai == 1:
    for i in range(1, 10):
        placeposi = int(input(f"Enter Position of {i}: "))
        initialstate[placeposi // 3][placeposi % 3] = i

    for i in range(1, 10):
        placeposi = int(input(f"Enter Final Position of {i}: "))
        finalstate[placeposi // 3][placeposi % 3] = i


def printstate(matrix: list):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print("\n")


print("Initial State:")
printstate(initialstate)
print("Final State:")
printstate(finalstate)


def h(starting_node):
    # Manhattan distance heuristic
    h_val = 0
    for i in range(3):
        for j in range(3):
            value = starting_node[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                h_val += abs(i - target_x) + abs(j - target_y)
    return h_val


def f(starting_node, starting_node_g):
    # f(n) = g(n) + h(n)
    return starting_node_g + h(starting_node)


open_list = []  # priority queue (min-heap)
closed_list = []  # visited states (set)


def childgeneration(initialstate):
    children = []
    sx, sy = 0, 0

    def movesup(x, y):
        return x - 1, y

    def movesdown(x, y):
        return x + 1, y

    def movesleft(x, y):
        return x, y - 1

    def movesright(x, y):
        return x, y + 1

    def validmove(fn):
        nx, ny = fn(sx, sy)
        if 0 <= nx < 3 and 0 <= ny < 3:
            return True
        return False

    def movespace(state, newx, newy):
        new_state = [row[:] for row in state]
        tobemoved = new_state[newx][newy]
        new_state[newx][newy] = 0
        new_state[sx][sy] = tobemoved
        return new_state

    spaceshift = [movesup, movesdown, movesleft, movesright]

    # find space
    for x in range(3):
        for y in range(3):
            if initialstate[x][y] == 0:
                sx, sy = x, y
                break

    # find possible children
    for move_fn in spaceshift:
        if validmove(move_fn):
            new_state = movespace(initialstate, *move_fn(sx, sy))
            if new_state not in closed_list:
                children.append(new_state)

    return children


def chooseleast():
    min_f = float("inf")
    min_index = -1

    for idx, state in enumerate(open_list):
        f_val = f(state, len(closed_list))
        if f_val < min_f:
            min_f = f_val
            min_index = idx

    return min_index


def process():
    g = 0
    open_list.append(initialstate)

    while len(open_list) > 0:
        idx = chooseleast()
        current_state = open_list[idx]
        g += 1
        if current_state == finalstate:
            print("Solution Found!")
            print(f"Step {g} - ")
            printstate(current_state)
            print("Total Steps", g)
            return True

        print(f"Step {g} - ")
        printstate(open_list.pop(idx))
        closed_list.append(current_state)

        for child in childgeneration(current_state):
            if child not in closed_list and child not in open_list:
                open_list.append(child)

    print("No solution found.")
    return False


process()

end_time = time.localtime()
print("Time_Taken:", end_time - start_time)
