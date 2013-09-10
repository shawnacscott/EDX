def laceStrings(s1, s2):
    indice = 0
    emptyStr = ''
    while len(s1) >= (indice + 1) and len(s2) >= (indice + 1):
        emptyStr = emptyStr + s1[indice] + s2[indice]
        indice += 1
    emptyStr = emptyStr + s1[indice:] + s2[indice:]
    return emptyStr
        
        
