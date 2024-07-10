# 5373번 큐빙

import sys
input = sys.stdin.readline

# 위 : 흰 / 아래 : 노 / 앞 : 빨 / 뒷 : 오렌지 / 왼 : 초 / 오 : 파

def rotate_face(face, direction):
    if direction == "+":
        return [list(row) for row in zip(*face[::-1])]
    else:
        return [list(row) for row in zip(*face)][::-1]

def cubing(d, w):
    global cube
    if d == 'U':
        cube[0] = rotate_face(cube[0], w)
        tmp = cube[2][0]
        if w == "+":
            cube[2][0] = cube[5][0]
            cube[5][0] = cube[3][0]
            cube[3][0] = cube[4][0]
            cube[4][0] = tmp
        else:
            cube[2][0] = cube[4][0]
            cube[4][0] = cube[3][0]
            cube[3][0] = cube[5][0]
            cube[5][0] = tmp
    elif d == 'D':
        cube[1] = rotate_face(cube[1], w)
        tmp = cube[2][2]
        if w == "+":
            cube[2][2] = cube[4][2]
            cube[4][2] = cube[3][2]
            cube[3][2] = cube[5][2]
            cube[5][2] = tmp
        else:
            cube[2][2] = cube[5][2]
            cube[5][2] = cube[3][2]
            cube[3][2] = cube[4][2]
            cube[4][2] = tmp
    elif d == 'F':
        cube[2] = rotate_face(cube[2], w)
        tmp = [cube[0][2][i] for i in range(3)]
        if w == "+":
            for i in range(3):
                cube[0][2][i] = cube[4][2-i][2]
                cube[4][2-i][2] = cube[1][0][2-i]
                cube[1][0][2-i] = cube[5][i][0]
                cube[5][i][0] = tmp[i]
        else:
            for i in range(3):
                cube[0][2][i] = cube[5][i][0]
                cube[5][i][0] = cube[1][0][2-i]
                cube[1][0][2-i] = cube[4][2-i][2]
                cube[4][2-i][2] = tmp[i]
    elif d == 'B':
        cube[3] = rotate_face(cube[3], w)
        tmp = [cube[0][0][i] for i in range(3)]
        if w == "+":
            for i in range(3):
                cube[0][0][i] = cube[5][i][2]
                cube[5][i][2] = cube[1][2][2-i]
                cube[1][2][2-i] = cube[4][2-i][0]
                cube[4][2-i][0] = tmp[i]
        else:
            for i in range(3):
                cube[0][0][i] = cube[4][2-i][0]
                cube[4][2-i][0] = cube[1][2][2-i]
                cube[1][2][2-i] = cube[5][i][2]
                cube[5][i][2] = tmp[i]
    elif d == 'L':
        cube[4] = rotate_face(cube[4], w)
        tmp = [cube[0][i][0] for i in range(3)]
        if w == "+":
            for i in range(3):
                cube[0][i][0] = cube[3][2-i][2]
                cube[3][2-i][2] = cube[1][i][0]
                cube[1][i][0] = cube[2][i][0]
                cube[2][i][0] = tmp[i]
        else:
            for i in range(3):
                cube[0][i][0] = cube[2][i][0]
                cube[2][i][0] = cube[1][i][0]
                cube[1][i][0] = cube[3][2-i][2]
                cube[3][2-i][2] = tmp[i]
    elif d == 'R':
        cube[5] = rotate_face(cube[5], w)
        tmp = [cube[0][i][2] for i in range(3)]
        if w == "+":
            for i in range(3):
                cube[0][i][2] = cube[2][i][2]
                cube[2][i][2] = cube[1][i][2]
                cube[1][i][2] = cube[3][2-i][0]
                cube[3][2-i][0] = tmp[i]
        else:
            for i in range(3):
                cube[0][i][2] = cube[3][2-i][0]
                cube[3][2-i][0] = cube[1][i][2]
                cube[1][i][2] = cube[2][i][2]
                cube[2][i][2] = tmp[i]

# 위 : 흰 / 아래 : 노 / 앞 : 빨 / 뒷 : 오렌지 / 왼 : 초 / 오 : 파
T = int(input())
for _ in range(T):
    cube = [[['w', 'w', 'w'] for _ in range(3)],
            [['y', 'y', 'y'] for _ in range(3)],
            [['r', 'r', 'r'] for _ in range(3)],
            [['o', 'o', 'o'] for _ in range(3)],
            [['g', 'g', 'g'] for _ in range(3)],
            [['b', 'b', 'b'] for _ in range(3)]]
    n = int(input())
    order = list(input().strip().split())
    for o in order:
        cubing(o[0], o[1])

    for i in range(3):
        print(''.join(cube[0][i]))