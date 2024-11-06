def elso(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            db+=1
        i+=1
    print(f"{db} db negatív szám van.")
    return db

def masodik(lista):
    i:int=0
    max_index:int=0 #feltételezem, hogy a lista első eleme a legnagyobb
    while(i<len(lista)):
        if(lista[i]>lista[max_index]):
            max_index=i
        i+=1
    print(f"A legnagyobb szám a listában: {max_index}")
    return lista[max_index]

def harmadik(lista):
    #elso(lista)
    paros_lista=[]
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]>0):
            db+=1
        i+=1
    print(f"{db} db páros szám van.")
    return db
    
    