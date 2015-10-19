def anti_vocal(texto):
    r=len(texto)
    cnt=0
    cadena=""
    while cnt < r:
        if texto[cnt] not in "aeiouAEIOU":
            cadena+=texto[cnt]
        cnt+=1
    return cadena

print anti_vocal("Hello")