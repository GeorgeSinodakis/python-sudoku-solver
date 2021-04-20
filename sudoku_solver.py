import numpy

a = [[0,2,6,0,0,0,3,7,8],
     [0,5,8,6,3,7,4,0,0],
     [0,4,7,0,0,0,5,6,1],
     [0,0,0,7,2,0,9,0,0],
     [0,0,0,3,0,8,2,5,0],
     [8,0,2,0,0,0,0,1,0],
     [4,6,9,5,0,1,0,0,0],
     [0,0,1,9,0,0,7,4,0],
     [0,3,0,0,4,0,0,9,0]]

def possible(number, y, x):
    """τσέκαρε αν υπάρχει ο αριθμός στην γραμμή ή στην στήλη ή στο τετράγωνο"""

    global a
    for i in range(9):
        if a[y][i] == number:
            return False

    for i in range(9):
        if a[i][x] == number:
            return False

    y0 = (y//3)*3
    x0 = (x//3)*3

    for grammes in range(0,3):
        for stiles in range(0,3):
            if a[y0+grammes][x0+stiles] == number:
                return False

    return True

solved = False

def solve():

    global a,solved
    for grammes in range(9):
        for stiles in range(9):
            if a[grammes][stiles] == 0:
                for n in range(1,10):
                    if possible(n, grammes, stiles):
                        a[grammes][stiles] = n
                        solve()
                        if not solved:
                            a[grammes][stiles] = 0
                return
    solved = True


solve()
print(numpy.matrix(a))
input()
