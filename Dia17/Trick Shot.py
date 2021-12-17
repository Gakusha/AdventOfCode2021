xmax=259
xmin=235

ymax=-62
ymin=-118


maximos=[]

for vxI in range(-100,300): #valores arbitarios hasta que la plataforma me acepto la respuesta
    for vyI in range(-200,1000):
        
        x=0
        y=0
        vx=vxI
        vy=vyI
        hmax=0
        cumplido=False
        
        while x<=xmax and y>=ymin:
            
            x+=vx
            y+=vy
            
            if vx>0:
                vx-=1
                
            vy-=1
            
            
            if y>hmax:
                hmax=y
            
            if y>=ymin and y<=ymax and x>=xmin and x<=xmax:
                cumplido=True
        
        if cumplido:
            maximos.append(hmax)
        
            
print(max(maximos))

print(len(maximos))
                