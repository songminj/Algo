import sys

m = int(sys.stdin.readline())
st = set()
def set_cal(order, num):
    global st
    if order == 'add':
        st.add(num)
        return
    if order == 'remove':
        st.discard(num)
        return
    if order == 'check':
        if num in st:
            print(1)
        else:
            print(0)
        return
    if order == 'toggle':
        if num in st:
            st.remove(num)
        else:
            st.add(num)
        return
    if order == 'all':
        st = set(range(1, 21))
        return
    if order == 'empty':
        st.clear()
        return
    pass

for i in range(m):
    order, *num = map(str, sys.stdin.readline().split())
    if num :
        num = int(*num)
    # print(order, num)
    set_cal(order, num)
    # print(st)
    # print(st)
