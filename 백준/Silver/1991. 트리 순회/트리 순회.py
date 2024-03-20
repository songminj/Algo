import sys
input = sys.stdin.readline

# n 받기
n = int(input())

# tree 만들어주기
tree = [[] for _ in range(n+1)]
translate = {chr(64+i) : i for i in range(1, 27)}
# '.'은 None으로 바꿔준다.
translate['.'] = None

for _ in range(n):
    node, *child = input().split()
    tree[translate[node]] += child
# 전위순회
def preorder(v):
    if translate[v] == None:
        return
    print(v, end='')
    preorder(tree[translate[v]][0])
    preorder(tree[translate[v]][1])

def inorder(v):
    if translate[v] == None:
        return
    inorder(tree[translate[v]][0])
    print(v, end='')
    inorder(tree[translate[v]][1])

def postorder(v):
    if translate[v] == None:
        return
    postorder(tree[translate[v]][0])
    postorder(tree[translate[v]][1])
    print(v, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')