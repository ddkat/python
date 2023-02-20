#goal is to find difference between blood testpacks

#two blood test packs given in string form


base = """Aszpartát-aminotranszferáz (ASAT, GOT), Alaninaminotranszferáz (ALAT, GPT), Gamma-glutamiltranszferáz
(GGT), Alkalikus foszfatáz (ALP), Összes bilirubin, Laktát
dehidrogenáz (LDH), Amiláz, Karbamid, Kreatinin, Húgysav,
Glükóz (vércukor), Nátrium (Na), Kálium (K), Kalcium (Ca),
Foszfát (P), Magnézium (Mg), Vas (Fe), Transzferrin, Ferritin,
Összfehérje, Albumin, C reaktív protein (CRP), Koleszterin,
Triglicerid, LDL koleszterin, HDL koleszterin, Vérkép
automatával (kvalitatív vérképpel), Általános vizeletvizsgálat
üledékkel, TSH (Tireoidea-Stimuláló Hormon), D-vitamin
(Total 25-OH D-vitamin), Mintavételi díj"""

compare = """Aszpartát-aminotranszferáz (ASAT, GOT), Alaninaminotranszferáz (ALAT, GPT), Gamma-glutamiltranszferáz
(GGT), Alkalikus foszfatáz (ALP), Összes bilirubin, Konjugált
(direkt) bilirubin, Laktát dehidrogenáz (LDH), Kreatin-kináz
(CK), Amiláz, Karbamid, Kreatinin, Húgysav, Inzulin, Glükóz
(vércukor), Nátrium (Na), Kálium (K), Klorid (Cl), Kalcium (Ca),
Foszfát (P), Magnézium (Mg), Vas (Fe), Transzferrin, Ferritin,
Összfehérje, Albumin, C reaktív protein (CRP), Reuma faktor
(RF), Koleszterin, LDL koleszterin, HDL koleszterin, Triglicerid,
Vérkép automatával (kvalitatív vérképpel), Vörösvérsejt
süllyedés (We), Folsav, B12-vitamin, Általános vizeletvizsgálat
üledékkel, Széklet vér immunológiai kimutatása, TSH
(Tireoidea-Stimuláló Hormon), Totál tesztoszteron, D-vitamin
(Total 25-OH D-vitamin), PSA (prosztata specifikus antigén),
Mintavételi díj"""

base_list = list(base.split(','))
compare_list = list(compare.split(','))

base_final = []
compare_final = []

for item1 in base_list:
    base_final.append(" ".join(item1.split()))
    
for item2 in compare_list:  
    compare_final.append(" ".join(item2.split()))

#print(base_pack, check_pack)

dif = []

for test in compare_final:
    if test not in base_final:
        dif.append(test)    

print(', '.join(dif))