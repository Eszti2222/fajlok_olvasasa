import random
def lista_letrehozasa():
    #generalj 100 véletlen egész számot[-50, 150] között
    # a függvény térjen vissza a listával
    lista=[]
    i:int=0
    while(i<100):
        vszam:int= int(random.random()*(201)-50)
        i+=1
        lista.append(vszam)
    return lista

lista=lista_letrehozasa()
print(lista)

#a listában lévő számokat fűzd össze stringgé, az elválasztó jel ";" legyen. Az utolsó után ne legyen";"
def szovegge_alakit(lista):
    szoveg:str=""
    i:int=0
    while(i<len(lista)):
        if(i<len(lista)-1):
            szoveg +=f"{lista[i]};"
        else:
            szoveg+=f"{lista[i]}"
        i+=1
    return szoveg

def fajlba_mentes(szoveg):
    fajlom = open("adatok.txt", "w", encoding='utf-8')
    fajlom.write(szoveges_lista)
    fajlom.close()

szoveges_lista=szovegge_alakit(lista)
print(szoveges_lista)
fajlba_mentes(szoveges_lista)
#Adatok beolvasása fájlból

def fajlbol_olvas():
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg_fajlbol:str=fajlom.read()
    szoveg_lista=szoveg_fajlbol.split(";")
    for i in range(0,len(szoveg_lista),1):
        szam:int= int(szoveg_lista[i].strip())
        lista.append(szam)
    print(szoveg_fajlbol)
    print(lista)
    fajlom.close()
    return lista

fajlbol_olvas()




