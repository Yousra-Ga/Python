import matplotlib.pyplot as plt
#import nampy


notes = {}
class MyClass:
    modules = ["DAP 1 Datenstrukturen, Algorithmen und Programmierung",
            "RS Rechnerstrukturen" ,
            "HM1 Höhere Mathematik", 
            "BS Betriebssysteme" ,
            "Wrums Wahrscheinlichkeitsrechnung und math. Statistik" ,
            "Grundlagen der Elektrotechnik 1&2" , 
            "Präsentationstechnik" ,
            "DAP 2 Datenstrukturen, Algorithmen und Programmierung 2" ,
            "HM2 Höhere Mathematik 2", 
            "Rvs Rechnernetze und verteilte Systeme" ,
            "HM3 Höhere Mathematik 3" , 
            "Proseminar" ,
            "Ringvorlesung Elektrotechnik " , 
            "Physik für Elektrotechnik " ,
            "Steuerungs- und Regelungstechnik " , 
            "Praktikum Robotik " ,
            "Markt und Wettbewerb ", 
            "Marketing " ,
            "Wahlpflicht " , 
            "SWT Softwaretechnik " , 
            "SoPra Software-Praktikum ", 
            "Fachprojekt " , 
            "BA Bachelorabschlussmodul " ,
            "GTI Theoretische Informatik für Angew. Informatik ",
]
#for i in range(0,25):
for modul in MyClass.modules:

  x=input(f"did you pass {modul}? yes(y)/no")
  if x == "y":
   note = float(input('enter your Note:'))
   notes[modul] = note
  else :
   notes[modul] = 0

xwerte = list (notes.keys())
ywerte = list(notes.values())
plt.bar(xwerte, ywerte)
plt.xlabel("Modulen")
plt.ylabel("Noten")
plt.show()