w, h = map(int, input().split())
slice_num = int(input())

ws = [0, w]
hs = [0, h]

for i in range(slice_num):
  way, num = list(map(int, input().split()))
  if way == 0 :
    hs.append(num)
  else:
    ws.append(num)
    
  hs.sort()
  ws.sort()
  hs_total = []
  ws_total = []
  for i in range(len(hs)-1):
    hs_total.append(hs[i+1]-hs[i])
  for i in range(len(ws)-1):
      ws_total.append(ws[i+1]-ws[i])

area = max(hs_total) * max(ws_total)
print(area)  