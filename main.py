rows=7
cols=7
matrica = [[0] * cols for _ in range(rows)]
for i in range (rows):
  row=[]
  for j in range(cols):
    if i % 2 == 0:
      matrica[i][j] = (j+1) % 2
    else:
       matrica[i][j] = j % 2
for r in matrica:
  print(*r)