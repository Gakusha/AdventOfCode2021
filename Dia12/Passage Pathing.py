
aristas= {'yb': ['start', 'rj', 'DN', 'OC', 'de', 'MU'], 
          'start': ['yb', 'VP', 'rj'], 
          'de': ['vd', 'OC', 'MU', 'rj', 'VP', 'yb'], 
          'vd': ['de', 'end', 'WK', 'DN', 'MU'], 
          'rj': ['yb', 'VP', 'de', 'DN', 'start'], 
          'VP': ['rj', 'start', 'de', 'oa'], 
          'OC': ['de', 'yb', 'end'], 
          'MU': ['de', 'vd', 'oa', 'jv', 'yb'], 
          'end': ['DN', 'vd', 'OC'], 
          'DN': ['end', 'vd', 'yb', 'rj'], 
          'WK': ['vd'], 'oa': ['MU', 'VP'], 
          'jv': ['MU']}

aristas2={'start': ['A', 'b'], 
         'A': ['start', 'c', 'b', 'end'], 
         'b': ['start', 'A', 'd', 'end'], 
         'c': ['A'], 
         'd': ['b'], 
         'end': ['A', 'b']}



def part1():

    
    def caminos(aristas, start, end, visitados):
        
        
        if start==end:
            return 1
        
        total=0
        
        for x in aristas[start]:
            if x in visitados and x==x.lower():  
                continue
            else:
                total+=caminos(aristas, x, end, visitados+[start])
              
        return total
    
    print(caminos(aristas, "start", "end",[]))
            
def part2():

    def caminos(aristas, start, end, visitados, cumplido):
        
        if start==end:
            return 1
        
        total=0
        
        for x in aristas[start]:
            if x in visitados and x==x.lower() and (cumplido==True or x in ["start","end"]):  
                continue
            else:
                if x in visitados and x==x.lower():
                    total+=caminos(aristas, x, end, visitados+[start], True)
                else:
                    total+=caminos(aristas, x, end, visitados+[start], cumplido)
        
        return total
    
    print(caminos(aristas, "start", "end",[],False))
    
part2()

#4411
#136767

