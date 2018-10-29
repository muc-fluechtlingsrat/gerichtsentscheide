# -*- coding: cp1252 -*-
import fileLib

def explode(sourceString, searchString):
    sourceString = fileLib.strip(sourceString,"\n")
    liste = []
    string1 = ""
    string2 = ""
    for i in sourceString:
        if len(string2) == len(searchString):
            string1 += string2[0]
            string2 = string2[1:]
        string2 += i
        if string2 == searchString:
            liste.append(string1)
            string1 = ""
            string2 = ""
    if string1 != "" or string2 != "":
        liste.append(string1+string2)
    return liste

def read(fileName):
    liste = []
    f = open(fileName,"r")
    for line in f:
        line1 = explode(line, ",")
        try:
            line[11]
        except IndexError:
            continue
        try:
            int(line1[1])
        except ValueError:
            continue
        line2 = [line1[0]]
        for i in range(1, len(line1)):
            try:
                line2.append(int(line1[i]))
            except ValueError:
                if line1[i] != "":
                    if line1[i][0] == '"': line2.append(line1[i])
                    elif line1[i][-2:] == '%"':
                        line2[-1] += "," + line1[i]
                else: line2.append("")
        liste.append(line2)
    f.close()
    return liste

liste1 = read("2017_berufungen.csv")
liste2 = read("2017_klagen.csv")
liste3 = read("2017_revisionen.csv")
liste = []
f = open("2017_gesamteZahlen.csv","w")
f.write("Erst- und Folgeanträge\n")
f.write(";Berufungen;Gerichtsentscheidungen\n")
f.write(";;gesamt;Asyl Art.16a GG u. Fam.Asyl;(GFK) Flüchtlingsschutz;Subsidiärer Schutz;Abschiebungsverbot;Ablehnungen")
f.write(";sonst. Verfahrenserledigungen (z. B. Rücknahmen)\n")
for i in liste2:
    liste4 = i
    for j in liste1:
        if j[0] == i[0]:
            for k in range(1,len(j)):
                if type(j[k]) == int:
                    liste4[k] += j[k]
            break
    for j in liste3:
        if j[0] == i[0]:
            for k in range(1,len(j)):
                if type(j[k]) == int:
                    liste4[k] += j[k]
            break
    liste.append(liste4)
for i in liste1:
    liste4 = i
    inListe = False
    for j in liste2:
        if j[0] == i[0]:
            inListe = True
            break
    if inListe: continue
    for j in liste3:
        if j[0] == i[0]:
            for k in range(1,len(j)):
                if type(j[k]) == int:
                    liste4[k] += j[k]
            break
    liste.append(liste4)
for i in liste3:
    inListe = False
    for j in liste1:
        if j[0] == i[0]:
            inListe = True
            break
    if inListe: continue
    for j in liste2:
        if j[0] == i[0]:
            inListe = True
            break
    if inListe: continue
    liste.append(liste4)
for i in liste:
    for j in i:
        if type(j) == int:
            f.write(str(j)+";")
            continue
        if j[-2:] != '%"' and  j!= "":
            f.write(str(j)+";")
    f.write("\n")
f.close()
