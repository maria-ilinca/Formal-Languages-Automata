import re
inf = open("info.txt", 'r', encoding="utf-8") # de aici preia datele
lista_descriere = []
x = 0
i = 0
ex = True
while ex:
    s1 = inf.readline()
    if (not s1):
        ex = False
        break
    s2 = inf.readline()
    lista_descriere.append((s1, s2))
    i += 1
# ----------------------------------------------------------------------------------

print("se ruleaza")
f = open("date.txt", "w", encoding="utf-8") # aici scrie datele

f.write("\n1.Tari:")
# germania = 0
germania = bulgaria = franta = italia = anglia = danemarca = belgia = olanda = spania = grecia = 0
for element in lista_descriere:
    if re.findall('(?i)germania', element[0]) or re.findall('(?i)germania', element[1]):
        germania += 1
    if re.findall('(?i)bulgaria', element[0]) or re.findall('(?i)bulgaria', element[1]):
        bulgaria += 1
    if re.findall('(?i)franta|fran.a|franța', element[0]) or re.findall('(?i)franta|franța|fran.a', element[1]):
        franta += 1
    if re.findall('(?i)italia', element[0]) or re.findall('(?i)italia', element[1]):
        italia += 1
    if re.findall('(?i)anglia', element[0]) or re.findall('(?i)anglia', element[1]):
        anglia += 1
    if re.findall('(?i)danemarca', element[0]) or re.findall('(?i)danemarca', element[1]):
        danemarca += 1
    if re.findall('(?i)belgia', element[0]) or re.findall('(?i)belgia', element[1]):
        belgia += 1
    if re.findall('(?i)olanda', element[0]) or re.findall('(?i)olanda', element[1]):
        olanda += 1
    if re.findall('(?i)spania', element[0]) or re.findall('(?i)spania', element[1]):
        spania += 1
    if re.findall('(?i)grecia', element[0]) or re.findall('(?i)grecia', element[1]):
        grecia += 1

if germania:
    f.write(f"\nGermania: {str(germania)}")
if belgia:
    f.write(f"\nBelgia: {str(belgia)}")
if bulgaria:
    f.write(f"\nBulgaria: {str(bulgaria)}")
if franta:
    f.write(f"\nFranta: {str(franta)}")
if italia:
    f.write(f"\nItalia: {str(italia)}")
if anglia:
    f.write(f"\nAnglia: {str(anglia)}")
if danemarca:
    f.write(f"\nDanemarca: {str(danemarca)}")
if olanda:
    f.write(f"\nOlanda: {str(olanda)}")
if spania:
    f.write(f"\nSpania: {str(spania)}")
if grecia:
    f.write(f"\nGrecia: {str(grecia)}")

f.write("\n---------------------------")
f.write("\n2.Nivel studii:")

necalificat = calificat = student = absolvent = 0
# incepator

for element in lista_descriere:
    if re.findall('(?i)necalifica[tț]|incepator|.ncep.tor', element[0]) or re.findall(
            '(?i)necalifica[tț]|incepator|.ncep.tor', element[1]):
        necalificat += 1

    if re.findall('(?i)\scalifica[tț][a-z]*', element[0]) or re.findall('(?i)\scalifica[tț][a-z]*',
                                                                        element[1]):  # ca sa nu ia din ne-calificat
        calificat += 1

    if re.findall('(?i)studen[tț][a-z]*', element[0]) or re.findall('(?i)studen[tț][a-z]*', element[1]):
        student += 1

    if re.findall('(?i)absolven[tț][a-z]*', element[0]) or re.findall('(?i)absolven[tț][a-z]*', element[1]):
        absolvent += 1

if necalificat:
    f.write(f"\nNecalificat:{necalificat}")
if calificat:
    f.write(f"\nCalificat:{calificat}")
if student:
    f.write(f"\nStudent:{student}")
if absolvent:
    f.write(f"\nAbsolvent:{absolvent}")

f.write("\n---------------------------")
f.write("\n3.Profesie:")

profesii = []
contor = []

for element in lista_descriere:
    # angajeaza
    if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajeaza )\s*[a-zA-Z]+', element[1]))

    # angajeaza ceva1 si ceva2
    # regex pt ceva2:
    pattern = re.compile('angajeaza\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    # ceva1/ceva2
    pattern = re.compile('angajeaza\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

    # angajam
    if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajam )\s*[a-zA-Z]+', element[1]))

    pattern = re.compile('angajam\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    pattern = re.compile('angajam\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

    # angajez
    if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?<=angajez )\s*[a-zA-Z]+', element[1]))

    pattern = re.compile('angajez\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    pattern = re.compile('angajez\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

    # cauta
    if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[0]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[1]) not in profesii:
            profesii.append(re.findall('(?i)(?:(?<=caut )|(?<=caut[aă] )|(?<=c[aă]ut[aă]m ))\s*[a-zA-Z]+', element[1]))

    if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+',
                      element[0]) not in profesii:
            profesii.append(
                re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[0]))
    if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+',
                      element[1]) not in profesii:
            profesii.append(
                re.findall('(?i)(?:(?<=caut aj )|(?<=caut[aă] aj )|(?<=c[aă]ut[aă]m aj ))\s*[a-zA-Z]+', element[1]))

    if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+', element[0]):
        if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+',
                      element[0]) not in profesii:
            profesii.append(
                re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+',
                           element[0]))
    if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+', element[1]):
        if re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+',
                      element[1]) not in profesii:
            profesii.append(
                re.findall('(?i)(?:(?<=caut ajutor )|(?<=caut[aă] ajutor )|(?<=c[aă]ut[aă]m ajutor ))\s*[a-zA-Z]+',
                           element[1]))

    pattern = re.compile('cauta\s+[a-zA-Z]+\s+si\s+([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))
    pattern = re.compile('cauta\s+[a-zA-Z]+\s*[/,]\s*([a-zA-Z]+)', re.I)
    if re.findall(pattern, element[0]):
        if re.findall(pattern, element[0]) not in profesii:
            profesii.append(re.findall(pattern, element[0]))
    if re.findall(pattern, element[1]):
        if re.findall(pattern, element[1]) not in profesii:
            profesii.append(re.findall(pattern, element[1]))

# varianita cu aj/ajutor si la regexurile de mai sus
# sau (|) in expresiile cu compile in lookbehind

f.write(str(profesii))

# contorizare profesii


f.write("\n---------------------------")
f.write("\n4.Tip contract:")

determinata = nedeterminata = colaborare = internship = 0

for element in lista_descriere:
    if re.findall('(?i)nedeterminat[aă]', element[0]) or re.findall('(?i)nedeterminat[aă]', element[1]):
        nedeterminata += 1

    if re.findall('(?i)\sdeterminat[aă]', element[0]) or re.findall('(?i)\sdeterminat[aă]', element[1]):
        determinata += 1

    if re.findall('(?i)colaborare', element[0]) or re.findall('(?i)colaborare', element[1]):
        colaborare += 1

    if re.findall('(?i)internship', element[0]) or re.findall('(?i)internship', element[1]):
        internship += 1

f.write(f"\nPerioada nedeterminata:{nedeterminata}")
f.write(f"\nPerioada determinata: {determinata}")
f.write(f"\nColaborare: {colaborare}")
f.write(f"\nInternship: {internship}")

f.write("\n---------------------------")
f.write("\n5.Program:")

full_time = part_time = flexibil = peste = 0

for element in lista_descriere:
    if re.findall('(?i)full time|fulltime|full_time|full-time|8\s*h|8\s*ore', element[0]) or re.findall(
            '(?i)full time|fulltime|full_time|full-time|8\s*h|8\s*ore', element[1]):
        full_time += 1

    if re.findall('(?i)part time|part_time|part-time|parttime|4\s*h|4\s*ore', element[0]) or re.findall(
            '(?i)part time|part_time|part-time|parttime|4\s*h|4\s*ore', element[1]):
        part_time += 1

    if re.findall('(?i)flexibil', element[0]) or re.findall('(?i)flexibil', element[1]):
        flexibil += 1

    if re.findall('(?i)9\s*h|9\s*ore|[0-8]{2}\s*h|[0-8]{2}\s*ore', element[0]) or re.findall(
            '(?i)9\s*h|9\s*ore|[0-8]{2}\s*h|[0-8]{2}\s*ore', element[1]):
        peste += 1

f.write(f"\nFull-time: {full_time}")
f.write(f"\nPart-time: {part_time}")
f.write(f"\nFlexibil: {flexibil}")
f.write(f"\n>8h: {peste}")
# sys.stdout.flush()


f.write("\n---------------------------")
f.write("\n6.Categorii permis:")

catA = catB = catC = catD = catCE = catBE = catDE = 0
# f.write(lista_descriere)
for element in lista_descriere:
    if re.findall('(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Aa]+\s+', element[0]) or re.findall(
            '(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Aa]+\s+', element[1]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Aa]+\s+',
        element[0]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Aa]+\s+',
        element[1]):
        catA += 1
    if re.findall('(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Bb]+\s+', element[0]) or re.findall(
            '(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Bb]+\s+', element[1]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Bb]+\s+',
        element[0]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Bb]+\s+',
        element[1]):
        catB += 1
    if re.findall('(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Dd]+\s+', element[0]) or re.findall(
            '(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Dd]+\s+', element[1]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Dd]+\s+',
        element[0]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Dd]+\s+',
        element[1]):
        catD += 1
    if re.findall('(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Cc]+\s+', element[0]) or re.findall(
            '(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+[Cc]+\s+', element[1]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Cc]+\s+',
        element[0]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+[Cc]+\s+',
        element[1]):
        catC += 1
    if re.findall('(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+,*(?:ce|C E|c.e)+',
                  element[0]) or re.findall(
        '(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+(?:ce|c.e)+', element[1]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+(?:ce|c.e)+',
        element[0]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+(?:ce|c.e)+',
        element[1]):
        catCE += 1
    if re.findall('(?i)(?:categoria|cat|permis|permsi|conducere|cat\.|condus|carnet)\s+,*(?:be|b.e)+',
                  element[0]) or re.findall(
        '(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+(?:be|b-e)+', element[1]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+(?:be|b.e)+',
        element[0]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+(?:be|b.e)+',
        element[1]):
        catBE += 1
    if re.findall('(?i)(?:categoria|cat|permis|permsi|conducere|cat\.|condus|carnet)\s+,*(?:de|d.e)+',
                  element[0]) or re.findall(
        '(?i)(?:categoria|cat|permis|permsi|conducere|condus|carnet)\s+(?:de|d-e)+', element[1]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+(?:de|d.e)+',
        element[0]) or re.findall(
        '(?i)(?:(?<=categoria)|(?<=cat)|(?<=permis)|(?<=conducere)|(?<=condus)|(?<=carnet))\s+[a-zA-Z]*\,*\s+(?:de|d.e)+',
        element[1]):
        catDE += 1

# f.write(f"\ncatA:{catA}")
# f.write(f"\ncatB:{catB}")
# f.write(f"\ncatBE:{catBE}")
# f.write(f"\ncatC:{catC}")
# f.write(f"\ncatCE:{catCE}")
# f.write(f"\ncatD:{catD}")
f.write(f"\ncatA:{catA}")
f.write(f"\ncatB:{catB}")
f.write(f"\ncatBE:{catBE}")
f.write(f"\ncatC:{catC}")
f.write(f"\ncatCE:{catCE}")
f.write(f"\ncatD:{catD}")




f.write("\n---------------------------")
f.write("\n7.Limbi straine:")


engleza = franceza = germana = spaniola = portugheza = chineza = araba = ucraineana = rusa = japoneza = coreeana = olandeza = 0

for element in lista_descriere:
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(engleza)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(engleza)+', element[1]):
        engleza += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(franceza)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(franceza)+', element[1]):
        franceza += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(germana)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(germana)+', element[1]):
        germana += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(spaniola)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(spaniola)+', element[1]):
        spaniola += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(portugheza)+',
                  element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(protugheza)+', element[1]):
        portugheza += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(chineza)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(chineza)+', element[1]):
        chineza += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(?:ucraineana|ucrainieana|ucrainiana)+',
                  element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(?:ucraineana|ucrainieana|ucrainiana)+',
            element[1]):
        ucraineana += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(rusa)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(rusa)+', element[1]):
        rusa += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(japoneza)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(japoneza)+', element[1]):
        japoneza += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(coreeana)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(coreeana)+', element[1]):
        coreeana += 1
    if re.findall('(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(olandeza)+', element[0]) or re.findall(
            '(?i)(?<=limba)\s+[a-zA-Z]*(?:\s+sau\s+|\s+si\s+|\/[a-zA-Z]*)*(olandeza)+', element[1]):
        olandeza += 1

f.write(f"\nengleza:{engleza}")
f.write(f"\nfranceza:{franceza}")
f.write(f"\ngermana:{germana}")
f.write(f"\nspaniola:{spaniola}")
f.write(f"\nportugheza:{portugheza}")
f.write(f"\nchineza:{chineza}")
f.write(f"\naraba:{araba}")
f.write(f"\nucraineana:{ucraineana}")
f.write(f"\nrusa:{rusa}")
f.write(f"\njaponeza:{japoneza}")
f.write(f"\ncoreeana:{coreeana}")
f.write(f"\nolandeza:{olandeza}")

f.write(f"\n--------------------------")
f.write(f"\n8.Nivelul de experienta:")
fara_experienta=entry_level=mid_level=senior_level=manager=0
for element in lista_descriere:
    if re.findall('(?i)experienta', element[0]) or re.findall('(?i)experienta', element[1]):
        fara_experienta+=1
    if re.findall('(?i)Entry', element[0]) or re.findall('(?i)Entry', element[1]):
        entry_level+=1
    if re.findall('(?i)Mid', element[0]) or re.findall('(?i)Mid', element[1]):
        mid_level+=1
    if re.findall('(?i)Senior', element[0]) or re.findall('(?i)Senior', element[1]):
        senior_level+=1
    if re.findall('(?i)Manager/Executiv', element[0]) or re.findall('(?i)Manager/Executiv', element[1]):
        manager+=1
f.write(f"\nFara experienta: ",{fara_experienta})
f.write(f"\nEntry level: ",{entry_level})
f.write(f"\nMid level: ",{mid_level})
f.write(f"\nSenior level: ",{senior_level})
f.write(f"\nManager/Executiv: ",{manager})

f.write(f"\n--------------------------")
f.write(f"\n9.Salariul:")

peste_6000=peste_4000=peste_2000=0

for element in lista_descriere:
    if re.findall('(?i)de la\s+[6-9]+[0-9]+[0-5]+[0-9]', element[0]) or re.findall('(?i)de la\s+[6-9]+[0-9]+[0-5]+[0-9]', element[1]):
        peste_6000+=1
    elif re.findall('(?i)de la\s+[4-6]+[0-9]+[0-5]+[0-9]', element[0]) or re.findall('(?i)de la\s+[4-6]+[0-9]+[0-5]+[0-9]', element[1]):
        peste_4000+=1
    elif re.findall('(?i)de la\s+[2-4]+[0-9]+[0-5]+[0-9]', element[0]) or re.findall('(?i)de la\s+[2-4]+[0-9]+[0-5]+[0-9]', element[1]):
        peste_2000 += 1
f.write(f"\nAu salariul peste 6000",{peste_6000})
f.write(f"\nAu salariul peste 4000",{peste_4000})
f.write(f"\nAu salariul peste 2000",{peste_2000})

f.write(f"\n---------------------------")
f.write(f"\n10.Orasul:")
Bucuresti=[]
Iasi=[]
Constanta=[]
for element in lista_descriere:
    if re.findall('(?i)in+Bucuresti', element[0]) or re.findall('(?i)Bucuresti', element[1]):
        Bucuresti.append(re.findall(pattern,re.compile('in+Bucuresti', re.I),element[0]))
    if re.findall('(?i)in+Iasi', element[0]) or re.findall('(?i)Iasi', element[1]):
        Iasi.append(re.findall(pattern,re.compile('in+Iasi', re.I),element[0]))
    if re.findall('(?i)in+Constanta', element[0]) or re.findall('(?i)in+Constanta', element[1]):
       Constanta.append(re.findall(pattern,re.compile('in+Constanta', re.I),element[0]))

f.write(f"\nLocuri de munca in Bucuresti:", {Bucuresti})
f.write(f"\nLocuri de munca in Iasi:", {Iasi})
f.write(f"\nLocuri de munca in Constanta:", {Constanta})

# f.write(lista_descriere)
