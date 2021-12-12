lista=[[5, 6, 6, 5, 1, 1, 4, 5, 5, 4], [4, 8, 8, 2, 6, 6, 5, 4, 2, 7], [6, 1, 8, 5, 5, 8, 2, 1, 1, 3], [7, 7, 6, 2, 8, 5, 2, 7, 4, 4], [7, 2, 5, 5, 6, 2, 1, 8, 4, 1], [8, 8, 4, 2, 7, 5, 3, 1, 2, 3], [8, 2, 2, 5, 3, 7, 2, 1, 7, 6], [7, 2, 1, 2, 8, 6, 5, 8, 2, 7], [7, 7, 5, 8, 7, 5, 1, 1, 5, 7], [1, 8, 2, 8, 5, 4, 4, 5, 6, 3]]

lista2=[[5, 4, 8, 3, 1, 4, 3, 2, 2, 3], [2, 7, 4, 5, 8, 5, 4, 7, 1, 1], [5, 2, 6, 4, 5, 5, 6, 1, 7, 3], [6, 1, 4, 1, 3, 3, 6, 1, 4, 6], [6, 3, 5, 7, 3, 8, 5, 4, 7, 8], [4, 1, 6, 7, 5, 2, 4, 6, 4, 5], [2, 1, 7, 6, 8, 4, 1, 7, 2, 1], [6, 8, 8, 2, 8, 8, 1, 1, 3, 4], [4, 8, 4, 6, 8, 4, 8, 5, 5, 4], [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]




def parte1():
    total=0
    for step in range(100):
        brillados=[]
        for x in range(10):
                for y in range(10):
                    lista[x][y]+=1    
        
        for _ in range(100):
            for x in range(10):
                for y in range(10):
                    if lista[x][y]>=10 and ([x,y]) not in brillados:                
                        brillados.append([x,y])
                        if ([x-1,y-1]) not in brillados and x-1>-1 and y-1>-1:
                            lista[x-1][y-1]+=1 
                        if ([x-1,y]) not in brillados and x-1>-1:
                            lista[x-1][y]+=1
                        if ([x-1,y+1]) not in brillados and x-1>-1 and y+1<10:
                            lista[x-1][y+1]+=1
                        if ([x,y-1]) not in brillados and y-1>-1 :
                            lista[x][y-1]+=1
                        if ([x,y+1]) not in brillados and y+1<10:
                            lista[x][y+1]+=1
                        if ([x+1,y-1]) not in brillados  and y-1>-1 and x+1<10 :
                            lista[x+1][y-1]+=1
                        if ([x+1,y]) not in brillados and x+1<10:
                            lista[x+1][y]+=1
                        if ([x+1,y+1]) not in brillados and x+1<10 and y+1<10:
                            lista[x+1][y+1]+=1
                    
                        
        for x in brillados:
            lista[x[0]][x[1]]=0
        
        total+=len(brillados)
        
            
    print(total)


def parte2():
    
    for step in range(400):
        brillados=[]
        for x in range(10):
                for y in range(10):
                    lista[x][y]+=1    
        
        for _ in range(100):
            for x in range(10):
                for y in range(10):
                    if lista[x][y]>=10 and ([x,y]) not in brillados:                
                        brillados.append([x,y])
                        if ([x-1,y-1]) not in brillados and x-1>-1 and y-1>-1:
                            lista[x-1][y-1]+=1 
                        if ([x-1,y]) not in brillados and x-1>-1:
                            lista[x-1][y]+=1
                        if ([x-1,y+1]) not in brillados and x-1>-1 and y+1<10:
                            lista[x-1][y+1]+=1
                        if ([x,y-1]) not in brillados and y-1>-1 :
                            lista[x][y-1]+=1
                        if ([x,y+1]) not in brillados and y+1<10:
                            lista[x][y+1]+=1
                        if ([x+1,y-1]) not in brillados  and y-1>-1 and x+1<10 :
                            lista[x+1][y-1]+=1
                        if ([x+1,y]) not in brillados and x+1<10:
                            lista[x+1][y]+=1
                        if ([x+1,y+1]) not in brillados and x+1<10 and y+1<10:
                            lista[x+1][y+1]+=1
                    
                        
        for x in brillados:
            lista[x[0]][x[1]]=0
        
        if len(brillados) == 100:
            print(step+1)
            break

parte2()