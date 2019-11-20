def displayPathtoPrincess(n,grid):
    p=[]
    m=[]
    for i in range(n):
        for j in range(n):
            if grid[i][j]=='p':
                p=[i,j]
            if grid[i][j]=='m':
                m=[i,j]
    if(m[0]<p[0]):
        moves=p[0]-m[0]
        for i in range(moves):
            print("DOWN")
    elif(m[0]>p[0]):
        moves=m[0]-p[0]
        for i in range(moves):
            print("UP")
    if(m[1]<p[1]):
        moves=p[1]-m[1]
        for i in range(moves):
            print("RIGHT")
    elif(m[1]>p[1]):
        moves=m[1]-p[1]
        for i in range(moves):
            print("LEFT")
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(list(input().strip()))

displayPathtoPrincess(m,grid)

