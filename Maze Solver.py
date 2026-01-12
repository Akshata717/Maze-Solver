import random 

def maze(): 
  rows = 9
  cols = 9
  cap = (0.2*rows*cols)

  array = []
  for i in range(9):
    x = []
    for j in range(9):
      x.append('0')
    array.append(x)

# start and end points 
  array[0][0] = 'S'
  array[7][4] = 'E'

  count = 0

  while (cap>count):
    x1 = random.randint(0, 8)
    y1 = random.randint(0, 8)

    if (array[x1][y1] == '0'):
      array[x1][y1] = 'X'
      count +=1

  return array 





# solves the maze 
def solver(array):
    rows = 9
    cols = 9
    visits = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(False)
        visits.append(row)


    
    visits[0][0] = True 
    path = []
    previous = {
        
    }
    path.append((0,0  ))

    while len(path) > 0:
        #print(len(path))
        pos = path.pop(0)
      
        newrow = pos[0]
        newcol = pos[1]


# directions 
        dir = [(1,0), (0,1), (0,-1), (-1,0)]
        for d in dir:
            x = newrow + d[0]
            y = newcol + d[1]

            if (0 <= x < 9) and (0 <= y < 9):
                if (array[x][y] != 'X') and ( not visits[x][y]):
                 
                 
                    visits[x][y] = True
                    path.append((x, y))
                    
                    previous[x, y] = (newrow, newcol)
        if array[newrow][newcol] == 'E':
            #noloop
            break

    for i in range(rows):
        for j in range(cols):
            if array[i][j] == 'E':
                cur = (i,j)
                
 

 
    while cur in previous:
        (i,j) = cur
        if array[i][j] == '0':
            array[i][j] = str("*")
        cur = previous[cur]


     


  
  

tester = maze()

print()
print()
solver(tester)

for row in tester:
  for x in row:
      print(x, end = " ")
  print()

    

      