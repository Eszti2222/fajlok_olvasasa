import fajlkezeles
import feladatok

lista=fajlkezeles.fajlbol_olvas()

fajlkezeles.lista_letrehozasa()

fajlkezeles.szovegge_alakit(lista)

fajlkezeles.fajlba_mentes(lista)

print("1.hány negatív szám van a listában?")
db=feladatok.elso(lista)

print("2.melyik a legnagyobb szám?")
max_index=feladatok.masodik(lista)
print("3.készits új listát paros_lista néven és legyenek benne a  páros számok")
paros_lista=feladatok.harmadik(lista)
print("4.mennyi az öttel osztható számok összege?")

print("5.hányadik helyen áll a legkisebb szám?")





