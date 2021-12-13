import numpy as np

def doblarX(matriz,c):
    matrizC=matriz[:]
    for i in range(len(matrizC)):
        for j in range(len(matrizC[0])-c):
            if matrizC[i][j]==0:
                matrizC[i][j]=matrizC[i][len(matrizC[0])-j-1]
            
    return matrizC[:,0:c]

def doblarY(matriz,c):
    matrizC=matriz[:]
    for i in range(len(matrizC)-c):
        for j in range(len(matrizC[0])):
            if matrizC[i][j]==0:
                matrizC[i][j]=matrizC[len(matrizC)-i-1][j]
    return matrizC[0:c,:]
            


lista=[[1284, 359], [47, 25], [699, 764], [55, 204], [552, 247], [731, 877], [765, 12], [619, 806], [437, 864], [1202, 152], [105, 456], [159, 165], [648, 563], [701, 143], [609, 861], [972, 414], [1195, 379], [1097, 439], [358, 95], [1126, 288], [773, 332], [863, 813], [1250, 63], [1280, 95], [1237, 672], [224, 343], [1222, 488], [748, 842], [554, 208], [1086, 215], [1136, 479], [1308, 826], [371, 367], [972, 722], [766, 719], [80, 366], [920, 22], [765, 882], [1208, 354], [994, 526], [512, 430], [1007, 507], [773, 695], [909, 672], [370, 231], [38, 812], [766, 495], [1078, 534], [633, 408], [233, 770], [251, 429], [874, 315], [649, 666], [1140, 868], [1138, 75], [808, 441], [864, 150], [1066, 814], [440, 674], [477, 238], [1290, 739], [786, 434], [263, 42], [306, 891], [1086, 652], [248, 621], [515, 387], [378, 730], [1255, 189], [769, 187], [70, 473], [408, 773], [1039, 581], [373, 312], [537, 562], [1078, 360], [1036, 775], [925, 565], [1022, 530], [132, 207], [1027, 815], [869, 7], [631, 281], [725, 404], [945, 305], [1173, 509], [678, 338], [788, 207], [447, 753], [166, 740], [745, 199], [49, 383], [1151, 729], [1255, 705], [351, 507], [648, 331], [1, 208], [728, 299], [174, 479], [224, 215], [179, 372], [497, 541], [445, 84], [952, 95], [1136, 422], [1253, 341], [251, 877], [269, 150], [227, 154], [597, 341], [72, 343], [657, 656], [900, 473], [117, 562], [990, 474], [1096, 326], [524, 147], [1228, 473], [990, 420], [360, 434], [493, 47], [582, 299], [843, 266], [1220, 850], [370, 103], [176, 26], [1192, 430], [890, 252], [1235, 809], [1220, 318], [666, 332], [711, 481], [1083, 154], [825, 2], [365, 305], [566, 854], [1278, 658], [213, 887], [26, 7], [766, 399], [448, 47], [892, 549], [349, 38], [605, 168], [303, 42], [592, 114], [433, 219], [7, 560], [10, 526], [227, 614], [186, 836], [323, 109], [32, 658], [1061, 802], [544, 271], [289, 589], [227, 280], [713, 553], [997, 574], [577, 221], [502, 696], [497, 801], [431, 486], [42, 250], [68, 866], [1290, 372], [736, 773], [676, 3], [1208, 663], [1004, 891], [202, 775], [1116, 655], [1057, 670], [840, 16], [160, 320], [172, 371], [480, 32], [666, 441], [83, 880], [100, 816], [813, 821], [1265, 868], [976, 420], [372, 822], [1284, 7], [110, 495], [348, 451], [1210, 526], [467, 852], [170, 474], [788, 339], [390, 872], [119, 703], [940, 663], [577, 764], [316, 646], [1, 460], [1027, 79], [137, 509], [565, 247], [838, 395], [321, 93], [763, 712], [268, 332], [355, 42], [217, 590], [410, 473], [213, 439], [433, 456], [733, 221], [1099, 739], [1211, 602], [221, 438], [371, 92], [579, 205], [207, 529], [487, 813], [1124, 58], [1097, 455], [213, 7], [1099, 67], [1149, 847], [208, 744], [633, 486], [1156, 813], [239, 735], [174, 78], [370, 663], [438, 348], [599, 690], [1061, 92], [987, 337], [333, 93], [1126, 291], [239, 541], [1029, 760], [1283, 637], [78, 273], [318, 186], [441, 103], [1036, 119], [1074, 793], [867, 827], [75, 17], [415, 541], [488, 154], [644, 441], [64, 91], [554, 816], [976, 474], [676, 43], [239, 353], [271, 133], [92, 842], [544, 719], [1097, 887], [157, 801], [1309, 131], [900, 421], [731, 689], [597, 822], [388, 175], [599, 637], [385, 296], [987, 785], [57, 374], [1158, 889], [167, 365], [731, 205], [316, 722], [830, 530], [239, 159], [905, 92], [663, 726], [927, 581], [530, 483], [107, 522], [455, 889], [1267, 316], [502, 866], [45, 26], [842, 58], [833, 238], [70, 638], [803, 36], [211, 515], [562, 52], [20, 851], [480, 332], [1148, 64], [679, 281], [1248, 200], [666, 562], [385, 744], [1093, 864], [1260, 164], [888, 364], [547, 74], [373, 582], [480, 479], [551, 486], [1021, 589], [120, 476], [467, 266], [1061, 753], [1298, 644], [728, 103], [544, 658], [561, 44], [1149, 47], [1233, 316], [1195, 827], [443, 155], [124, 35], [88, 488], [1203, 182], [1248, 305], [266, 787], [249, 589], [110, 770], [1019, 341], [565, 199], [863, 753], [1267, 255], [549, 438], [612, 616], [552, 551], [1208, 231], [577, 130], [883, 733], [43, 578], [274, 551], [766, 623], [584, 642], [1078, 812], [410, 80], [658, 68], [627, 369], [216, 236], [775, 540], [850, 239], [366, 530], [720, 803], [1252, 338], [869, 551], [830, 332], [1237, 448], [274, 882], [110, 627], [60, 130], [698, 26], [758, 23], [213, 791], [92, 52], [808, 812], [445, 114], [50, 400], [758, 540], [62, 200], [1066, 473], [683, 628], [1097, 103], [448, 418], [1247, 68], [770, 789], [816, 154], [1089, 456], [817, 47], [502, 562], [927, 294], [1267, 764], [1275, 33], [338, 172], [541, 187], [383, 600], [539, 155], [30, 799], [749, 850], [981, 847], [1077, 770], [808, 5], [609, 420], [354, 175], [383, 742], [950, 434], [535, 703], [1036, 12], [415, 353], [264, 332], [594, 588], [184, 288], [415, 735], [1086, 231], [1241, 490], [961, 38], [974, 156], [758, 354], [591, 826], [1222, 406], [574, 366], [502, 620], [1211, 733], [927, 742], [38, 530], [864, 430], [644, 696], [564, 402], [577, 578], [415, 93], [612, 644], [955, 852], [1044, 130], [864, 296], [1248, 835], [763, 522], [1248, 694], [1124, 836], [410, 814], [622, 882], [662, 563], [119, 191], [769, 775], [90, 318], [895, 541], [579, 877], [822, 154], [686, 351], [349, 856], [473, 133], [390, 22], [90, 850], [418, 148], [666, 696], [1136, 368], [701, 644], [510, 843], [1099, 379], [733, 764], [825, 450], [427, 733], [730, 376], [883, 280], [877, 456], [867, 67], [217, 752], [830, 252], [146, 147], [1034, 46], [714, 338], [619, 444], [771, 620], [724, 866], [403, 429], [57, 822], [27, 369], [1039, 152], [1129, 133], [1195, 739], [959, 507], [207, 753], [764, 294], [564, 598], [837, 740], [1257, 304], [661, 271], [1208, 652], [160, 574], [1083, 609], [1029, 565], [274, 119], [609, 644], [443, 827], [1011, 42], [211, 739], [580, 518], [895, 801], [401, 672], [815, 165], [502, 396], [624, 351], [445, 536], [842, 338], [766, 658], [1123, 266], [401, 670], [113, 119], [1036, 460], [85, 589], [661, 623], [60, 175], [249, 802], [1097, 791], [45, 537], [224, 802], [89, 647], [236, 793], [726, 256], [211, 67], [80, 528], [1283, 705], [537, 332], [338, 816], [385, 150], [221, 456], [227, 609], [400, 299], [248, 173], [502, 498], [649, 623], [1303, 560], [592, 332], [316, 248], [1086, 92], [117, 114], [622, 658], [136, 63], [748, 52], [907, 465], [1230, 773], [579, 689], [274, 460], [107, 182], [1077, 124], [1237, 446], [355, 852], [174, 422], [691, 603], [1283, 369], [653, 656], [109, 640], [433, 675], [873, 30], [1225, 589], [698, 616], [522, 207], [540, 789], [488, 546], [1186, 343], [102, 231], [169, 373], [354, 719], [907, 429], [217, 864], [249, 354], [713, 822], [1059, 429], [1293, 56], [488, 98], [1208, 204], [60, 63], [637, 56], [448, 847], [1236, 152], [1161, 880], [1267, 130], [545, 12], [584, 252], [1191, 533], [919, 516], [268, 338], [410, 30], [274, 12], [418, 549], [634, 43], [1044, 175], [544, 399], [383, 294], [1193, 88], [212, 553], [527, 677], [224, 679], [937, 312], [1066, 25], [427, 280], [1300, 780], [895, 735], [254, 595], [706, 282], [441, 392], [813, 73], [700, 72], [415, 159], [1171, 628], [644, 889], [900, 80], [209, 114], [837, 133], [537, 695], [716, 271], [822, 740], [1143, 365], [599, 413], [115, 379], [1158, 476], [769, 119], [373, 196], [60, 287], [1022, 364], [877, 219], [1265, 250], [1, 763], [910, 595], [937, 751], [35, 33], [1066, 421], [26, 359], [825, 521], [1033, 231], [880, 802], [49, 831], [830, 642], [75, 809], [80, 773], [1178, 351], [142, 464], [1300, 114], [2, 68], [70, 256], [354, 215], [813, 801], [867, 739], [266, 287], [480, 562], [371, 815], [1241, 852], [539, 620], [524, 434], [1111, 5], [85, 305], [174, 32], [800, 395], [1046, 562], [1134, 418], [1136, 78], [93, 850], [107, 372], [416, 152], [925, 329], [194, 787], [1250, 130], [705, 511], [657, 238], [1225, 876], [274, 775], [1129, 761], [574, 773], [1242, 28], [937, 143], [32, 236], [758, 551], [564, 850], [174, 368], [1220, 150], [1101, 114], [843, 8], [594, 306], [545, 814], [118, 38], [160, 740], [1241, 42], [378, 220], [994, 646], [698, 278], [73, 446], [552, 343], [925, 296], [174, 498], [1089, 438], [855, 668], [609, 117], [544, 627], [1265, 26], [1099, 515], [100, 368], [611, 130], [23, 556], [1056, 708], [1250, 831], [570, 497], [544, 684], [682, 887], [1027, 527], [43, 130], [731, 533], [1200, 627], [248, 684], [62, 305], [740, 497], [1092, 315], [1240, 638], [1086, 343], [701, 582], [989, 93], [830, 396], [124, 411], [186, 338], [1071, 353], [1158, 722], [284, 663], [758, 343], [152, 190], [7, 334], [266, 607], [706, 494], [691, 88], [1261, 63], [766, 175], [610, 72], [373, 329], [1263, 25], [174, 480], [666, 364], [446, 744], [1211, 161], [581, 222], [790, 600], [93, 178], [1141, 373], [120, 215], [93, 322], [597, 789], [744, 854], [1010, 311], [761, 149], [1019, 441], [224, 231], [900, 30], [472, 499], [706, 730], [480, 172], [688, 658], [371, 540], [174, 396], [825, 444], [830, 172]]

doblar=[["x",655],["y",447],["x",327],["y",223],["x",163],["y",111],["x",81],["y",55],["x",40],["y",27],["y",27],["y",13],["y",6]]

matriz=np.zeros((895,1311))
for x in lista:
        matriz[x[1]][x[0]]=1


def part1():
    
    matriz2=(doblarX(matriz,655)) 
    
    
    total=0
    for x in matriz2:
        total+=list(x).count(1)
        
    print(total)

def part2():
    
    matriz1=matriz[:]
    matriz2=[]
    
    
    for i in range(13):
        matriz2=matriz1
        matriz1=[]

        if doblar[i][0]=="x":
            matriz1=doblarX(matriz2,doblar[i][1])
        else:
            matriz1=doblarY(matriz2,doblar[i][1])
            
    for x in matriz1:
        for y in x:
            if y==1:
                print("x",end="")
            else:
                print(" ",end="")
        print("")
        
            
    

part2()


            



    