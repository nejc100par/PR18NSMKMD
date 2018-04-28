import codecs

loob={5501:"AJDOVŠČINA",
5502:"BREŽICE",
5503:"CELJE",
5504:"CERKNICA",
5505:"ČRNOMELJ",
5506:"DOMŽALE",
5507:"DRAVOGRAD",
5508:"GORNJA RADGONA",
5509:"GROSUPLJE",
5510:"HRASTNIK",
5511:"IDRIJA",
5512:"ILIRSKA BISTRICA",
5513:"IZOLA",
5514:"JESENICE",
5515:"KAMNIK",
5516:"KOČEVJE",
5517:"KOPER",
5518:"KRANJ",
5519:"KRŠKO",
5520:"LAŠKO",
5521:"LENART",
5522:"LENDAVA",
5523:"LITIJA",
5524:"LJUBLJANA BEŽIGRAD",
5525:"LJUBLJANA CENTER",
5526:"LJUBLJANA MOSTE POLJE",
5527:"LJUBLJANA ŠIŠKA",
5528:"LJUBLJANA VIČ RUDNIK",
5529:"LJUTOMER",
5530:"LOGATEC",
5534:"METLIKA",
5535:"MOZIRJE",
5536:"MURSKA SOBOTA",
5537:"NOVA GORICA",
5538:"NOVO MESTO",
5539:"ORMOŽ",
5540:"PIRAN",
5541:"POSTOJNA",
5542:"PTUJ",
5543:"RADLJE OB DRAVI",
5544:"RADOVLJICA",
5545:"RAVNE NA KOROŠKEM",
5546:"RIBNICA",
5547:"SEVNICA",
5548:"SEŽANA",
5549:"SLOVENJ GRADEC",
5550:"SLOVENSKA BISTRICA",
5551:"SLOVENSKE KONJICE",
5552:"ŠENTJUR PRI CELJU",
5553:"ŠKOFJA LOKA",
5554:"ŠMARJE PRI JELŠAH",
5555:"TOLMIN",
5556:"TRBOVLJE",
5557:"TREBNJE",
5558:"TRŽIČ",
5559:"VELENJE",
5560:"VRHNIKA",
5561:"ZAGORJE OB SAVI",
5562:"ŽALEC",
5564:"MARIBOR",
5565:"PESNICA",
5568:"RUŠE",
5598:"MNZ",
5599:"NEZNANA OBČ",
9999: "NEZNANA OBČ"}

prpo={
"B":"BREZ POŠKODBE",
"H":"HUDA TELESNA POŠKODBA",
"L":"LAŽJA TELESNA POŠKODBA",
"P":"SLED POŠKODBE",
"S":"SMRT",
"U":"BREZ POŠKODBE - UZ"
}


prvu={
"AV":"VOZNIK AVTOBUSA",
"DS":"VOZNIK DELOVNEGA STROJA",
"KM":"VOZNIK KOLESA Z MOTORJEM",
"KO":"KOLESAR",
"KR":"X-KRŠITELJ - JRM",
"KV":"VOZNIK KOMBINIRANEGA VOZILA",
"MK":"VOZNIK MOTORNEGA KOLESA",
"MO":"VOZNIK MOPEDA",
"OA":"VOZNIK OSEBNEGA AVTOMOBILA",
"OD":"ODGOVORNA OSEBA",
"OS":"OSTALO",
"PE":"PEŠEC",
"PO":"PRAVNA OSEBA",
"PT":"POTNIK",
"SM":"SKRBNIK MLADOLETNIKA",
"SV":"VOZNIK SPECIALNEGA VOZILA",
"TR":"VOZNIK TRAKTORJA",
"TV":"VOZNIK TOVORNEGA VOZILA",
"LK":"VOZNIK LAHKEGA ŠTIRIKOLESA",
"TK":"VOZNIK TRIKOLESA",
"SK":"VOZNIK ŠTIRIKOLESA"
}

lodz={1:"BOSNA IN HERCEGOVINA",
2:"ČRNA GORA",
3:"HRVAŠKA",
4:"MAKEDONIJA",
5:"SLOVENIJA",
6:"SRBIJA",
8:"KOSOVO",
101:"ALBANIJA",
102:"BOLGARIJA",
104:"MADŽARSKA",
106:"POLJSKA",
107:"ROMUNIJA",
111:"BELORUSIJA",
112:"UKRAJINA",
113:"LITVA",
114:"LATVIJA",
115:"ESTONIJA",
116:"RUSKA FEDERACIJA",
117:"REPUBLIKA MOLDAVIJA",
118:"ARMENIJA",
119:"GRUZIJA",
120:"AZERBAJDŽAN",
121:"KAZAHSTAN",
122:"KIRGIZISTAN",
123:"UZBEKISTAN",
124:"TADŽIKISTAN",
125:"TURKMENISTAN",
130:"ČEŠKA REPUBLIKA",
131:"SLOVAŠKA",
175:"MAYOTTE",
201:"ANDORA",
202:"AVSTRIJA",
203:"BELGIJA",
204:"DANSKA",
205:"FINSKA",
206:"FRANCIJA",
207:"GRČIJA",
208:"NIZOZEMSKA",
209:"IRSKA",
210:"ISLANDIJA",
211:"ITALIJA",
212:"LIHTENŠTAJN",
213:"LUKSEMBURG",
214:"MONAKO",
215:"NEMČIJA",
216:"NORVEŠKA",
217:"PORTUGALSKA",
218:"SAN MARINO",
219:"ŠPANIJA",
220:"ŠVICA",
221:"ŠVEDSKA",
222:"SVETI SEDEŽ  VATIKANSKA MESTNA DRŽAVA",
223:"ZDRUŽENO KRALJESTVO  VELIKA BRITANIJA",
224:"MALTA",
225:"GIBRALTAR",
226:"FERSKI OTOKI",
232:"ERITREJA",
239:"JUŽNA GEORGIJA IN OTOKI JUŽNI SANDWICH",
240:"MALTEŠKI VITEŠKI RED",
301:"AFGANISTAN",
302:"BAHRAJN",
303:"MJANMAR  BURMA",
304:"BUTAN",
305:"ŠRI LANKA",
306:"FILIPINI",
307:"HONKONG",
308:"INDIJA",
309:"INDONEZIJA",
310:"IRAK",
311:"IRAN",
312:"IZRAEL",
313:"JAPONSKA",
314:"JEMEN",
315:"JORDANIJA",
316:"JEMEN NDR  JUŽNI JEMEN",
317:"ZDRUŽENI ARABSKI EMIRATI",
318:"KAMBODŽA",
319:"KITAJSKA",
320:"CIPER",
321:"KOREJA, REPUBLIKA",
322:"KOREJA, DEMOKRATIČNA LJUDSKA REPUBLIKA",
323:"KUVAJT",
324:"LAOS",
325:"LIBANON",
326:"MALEZIJA",
327:"MONGOLIJA",
328:"OMAN",
329:"NEPAL",
330:"PAKISTAN",
331:"SAUDOVA ARABIJA",
332:"SINGAPUR",
333:"SIRSKA ARABSKA REPUBLIKA",
334:"TAJVAN, PROVINCA KITAJSKE",
336:"TURČIJA",
337:"VIETNAM",
339:"PALESTINSKO OBMOČJE, ZASEDENO",
340:"SULTANAT BRUNEJ",
341:"KATAR",
342:"MACAU",
343:"MALDIVI",
344:"TAJSKA",
346:"TIMOR-LESTE",
347:"BANGLADEŠ",
348:"PAPUA NOVA GVINEJA",
350:"AVSTRALIJA",
351:"NOVA ZELANDIJA",
352:"SAMOA",
353:"FIDŽI",
354:"NAURU",
355:"SALOMONOVI OTOKI",
356:"TONGA",
357:"TUVALU",
358:"KIRIBATI",
359:"BOŽIČNI OTOK",
360:"VANUATU",
361:"AMERIŠKA SAMOA",
363:"GUAM",
364:"COOKOVI OTOKI",
365:"MIDWAYSKI OTOKI",
366:"NIUE",
367:"NOVA KALEDONIJA",
368:"NORFOLŠKI OTOKI",
371:"TOKELAU",
372:"FRANCOSKA POLINEZIJA",
376:"KOKOSOVI OTOKI",
401:"ALŽIRIJA",
402:"ANGOLA",
403:"BURUNDI",
404:"SREDNJEAFRIŠKA REPUBLIKA",
405:"ČAD",
406:"BENIN",
407:"ETIOPIJA",
408:"GABON",
409:"GAMBIJA",
410:"GANA",
411:"GVINEJA",
413:"ZIMBAVBE",
414:"JUŽNA AFRIKA",
415:"KAMERUN",
416:"KENIJA",
417:"KONGO",
418:"LESOTO",
419:"LIBERIJA",
420:"LIBIJSKA ARABSKA DŽAMAHIRIJA",
421:"MADAGASKAR",
422:"MALAVI",
423:"MALI",
424:"MAROKO",
425:"MAVRETANIJA",
426:"MOZAMBIK",
427:"NIGER",
428:"NIGERIJA",
429:"SLONOKOŠČENA OBALA",
430:"RUANDA",
431:"SENEGAL",
432:"SIERRA LEONE",
433:"SOMALIJA",
434:"SUDAN",
435:"TANZANIJA",
436:"TOGO",
437:"TUNIZIJA",
438:"EGIPT",
439:"UGANDA",
440:"ZAMBIJA",
441:"DŽIBUTI",
442:"GVINEJA BISSAU",
443:"BOCVANA",
444:"EKVATORIALNA GVINEJA",
445:"MAURITIUS",
446:"NAMIBIJA",
447:"SVAZI",
448:"KONGO ZAIRE, DEMOKRATIČNA REPUBLIKA",
449:"KAPVERDSKI OTOKI",
450:"SAO TOME IN PRINCIPE",
451:"KOMORI",
452:"SEJŠELI",
453:"ZAHODNA SAHARA",
454:"REUNION",
455:"SAINT (SVETA) HELENA",
498:"MOLDAVIJA",
501:"KANADA",
502:"ZDRUŽENE DRŽAVE",
503:"ANTIGVA IN BARBUDA",
504:"BELIZE",
505:"ANGVILA",
506:"BERMUDI",
507:"DEVIŠKI OTOKI (BRITANSKI)",
508:"DEVIŠKI OTOKI (ZDA)",
509:"GUADELOUPE",
510:"GRENLANDIJA",
511:"KAJMANSKI OTOKI",
512:"MARTINIK",
516:"NIZOZEMSKI ANTILI",
517:"SVETI KITTS IN NEVIS",
601:"DOMINIKANSKA REPUBLIKA",
602:"GVATEMALA",
603:"HAITI",
604:"HONDURAS",
605:"JAMAJKA",
606:"KOSTARIKA",
607:"KUBA",
608:"MEHIKA",
609:"NIKARAGVA",
610:"PANAMA",
611:"PORTORIKO",
612:"SALVADOR",
613:"TRINIDAD IN TOBAGO",
614:"BAHAMI",
615:"BARBADOS",
616:"GRENADA",
617:"DOMINIKA",
618:"SAINT (SVETA) LUCIJA",
619:"SAINT VINCENT IN GRENADINE",
620:"ARGENTINA",
621:"BOLIVIJA",
622:"BRAZILIJA",
623:"ČILE",
624:"EKVADOR",
625:"GVAJANA",
626:"KOLUMBIJA",
627:"PARAGVAJ",
628:"PERU",
629:"URUGVAJ",
630:"VENEZUELA",
631:"SURINAM",
632:"FRANCOSKA GVAJANA",
633:"FALKLANDSKI OTOKI MALVINI",
700:"BREZ DRŽAVLJANSTVA",
701:"ANTARKTIKA",
702:"ARUBA",
703:"BRITANSKO OZEMLJE INDIJKEGA OCEANA",
704:"BURKINA FASO",
705:"BOUVETOV OTOK",
707:"FRANCOSKO JUŽNO OZEMLJE",
708:"HEARDOV OTOK IN MCDONALDOVI OTOKI",
709:"JOHNSTON",
711:"MONTSERRAT",
712:"NEVTRALNA ZONA",
713:"PITCAIRN",
714:"SVALBARD IN JAN MAYEN",
715:"CURACAO",
716:"SINT MAARTEN",
717:"JERSEY",
718:"GUERNSEY",
719:"SAINT MARTIN",
720:"SAINT PIERRE AND MIQUELON",
721:"SAINT BARTHELEMY",
722:"WALIS IN FUTUNA",
723:"OTOK MAN",
724:"PALAU",
725:"MARSHALLOVI OTOKI",
726:"MIKRONEZIJA",
727:"SEVERNI MARIANSKI OTOKI",
728:"ZUNANJI OTOKI - UNITED STATES",
729:"ALANDSKO OTOČJE",
730:"TURKS IN CAICOS OTOKI",
996:"UNMIK - SAMO ZA POTNE LISTE",
997:"IZMIŠLJENA DRŽAVA",
998:"ZDRUŽENI NARODI",
999:"NEZNANO"}






kaj={
    "1":"POVZROČITELJ",
    "0":"UDELEŽENEC"
}
spol={
    "1":"MOŠKI",
    "2":"ŽENSKI",
    "0":""
}

pas={
    "1":"DA",
    "0":"NE",
    "2":"DA",
    "*":""
}





f = codecs.open("PNO04.txt", encoding='cp852')
i = open("pnose2004.csv","w")

i.write("FIOStevilkaZadeve$Povzrocitelj$Starost$Spol$UEStalnegaPrebivalisca$Drzavljanstvo$PoskodbaUdelezenca$VrstaUdelezenca$UporabaVarnostnegaPasu$VozniskiStazVLetih$VozniskiStazVMesecih$VrednostAlkotesta$VrednostStrokovnegaPregleda\n")

for vrsta in f:
    print(vrsta)

    tab = vrsta.split("$")


    if 1<len(vrsta):
        FIOStevilkaZadeve = tab[0].strip()
        Povzrocitelj = kaj[tab[1].strip()] if tab[1].strip()!="" else ""
        Starost = tab[2].strip() if tab[2].strip()!="" else ""
        Spol = spol[tab[3].strip()] if tab[3].strip()!="" else ""
        UEStalnegaPrebivalisca = loob[int(tab[4].strip())] if tab[4].strip() !="" else ""
        Drzavljanstvo = lodz[int(tab[5].strip())] if tab[5].strip()!="" and int(tab[5]) in lodz  else ""
        PoskodbaUdelezenca = prpo[tab[6].strip()] if tab[6].strip()!="" else ""
        VrstaUdelezenca = prvu[tab[7].strip()] if tab[7].strip()!="" else ""
        UporabaVarnostnegaPasu = pas[tab[8].strip()] if tab[8].strip()!="" else ""
        VozniskiStazVLetih = tab[9].strip() if tab[9].strip()!="" else "0"
        VozniskiStazVMesecih = tab[10].strip() if  tab[10].strip()!="" else "0"
        VrednostAlkotesta = tab[11].strip() if tab[11].strip()!="" else "0"
        VrednostStrokovnegaPregleda = tab[12].strip() if tab[12].strip()!="" else "0"

        #print(FIOStevilkaZadeve+"$"+Povzrocitelj+"$"+Starost+"$"+Spol+"$"+UEStalnegaPrebivalisca+"$"+Drzavljanstvo+"$"+PoskodbaUdelezenca+"$"+VrstaUdelezenca+"$"+UporabaVarnostnegaPasu+"$"+VozniskiStazVLetih+"$"+VozniskiStazVMesecih+"$"+VrednostAlkotesta+"$"+VrednostStrokovnegaPregleda)
        i.write(FIOStevilkaZadeve+"$"+Povzrocitelj+"$"+Starost+"$"+Spol+"$"+UEStalnegaPrebivalisca+"$"+Drzavljanstvo+"$"+PoskodbaUdelezenca+"$"+VrstaUdelezenca+"$"+UporabaVarnostnegaPasu+"$"+VozniskiStazVLetih+"$"+VozniskiStazVMesecih+"$"+VrednostAlkotesta+"$"+VrednostStrokovnegaPregleda+"\n")
i.close()