

diccionario={'SB': 'B', 'HH': 'P', 'VF': 'N', 'BS': 'S', 'NC': 'C', 'BF': 'H', 'BN': 'H', 'SP': 'H', 'BK': 'H', 'FF': 'N', 'VN': 'B', 'FN': 'C', 'FS': 'S', 'PP': 'F', 'ON': 'H', 'FV': 'F', 'KO': 'F', 'PK': 'H', 'VB': 'S', 'HS': 'B', 'NV': 'O', 'PN': 'S', 'VH': 'B', 'OS': 'P', 'BP': 'H', 'OV': 'B', 'HK': 'S', 'NN': 'K', 'SV': 'C', 'PB': 'F', 'SK': 'F', 'FB': 'S', 'NB': 'K', 'HF': 'P', 'FK': 'K', 'KV': 'P', 'PV': 'F', 'BC': 'S', 'FO': 'N', 'HC': 'F', 'CP': 'B', 'KK': 'F', 'PC': 'S', 'HN': 'O', 'SH': 'H', 'CK': 'P', 'CO': 'F', 'HP': 'K', 'PS': 'C', 'KP': 'F', 'OF': 'K', 'KS': 'F', 'NO': 'V', 'CB': 'K', 'NF': 'N', 'SF': 'F', 'SC': 'P', 'FC': 'V', 'BV': 'B', 'SS': 'O', 'KC': 'K', 'FH': 'C', 'OP': 'C', 'CF': 'K', 'VO': 'V', 'VK': 'H', 'KH': 'O', 'NP': 'V', 'NH': 'O', 'NS': 'V', 'BH': 'C', 'CH': 'S', 'CC': 'F', 'CS': 'P', 'SN': 'F', 'BO': 'S', 'NK': 'S', 'OO': 'P', 'VV': 'F', 'FP': 'V', 'OK': 'C', 'SO': 'H', 'KN': 'P', 'HO': 'O', 'PO': 'H', 'VS': 'N', 'PF': 'N', 'CV': 'F', 'BB': 'H', 'VC': 'H', 'HV': 'B', 'CN': 'S', 'OH': 'K', 'KF': 'K', 'HB': 'S', 'OC': 'H', 'KB': 'P', 'OB': 'C', 'VP': 'C', 'PH': 'K'}

inicio='SCVHKHVSHPVCNBKBPVHV'

pares = {}

for x in diccionario.keys():
    pares[x]=0
    
vacio=pares.copy()

for i in range(len(inicio)-1):
    pares[inicio[i:i+2]]+=1


for step in range(40):
    pares2 = vacio.copy()
    
    for par in pares:
        a=par[0]
        b=par[1]
        c=diccionario[par]
        pares2[a+c] += pares[par]
        pares2[c+b] += pares[par]
    
    pares = pares2.copy()


keys=pares.keys()

letras=set("".join(keys))

diccLetras={}

for x in letras:
    diccLetras[x]=0

for x in letras:
    for y in keys:
        if x ==y[0]:
            diccLetras[x]+=pares[y]

diccLetras[inicio[-1]]+=1
            

print(max(diccLetras.values())-min(diccLetras.values()))