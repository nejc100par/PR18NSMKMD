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
5599:"NEZNANA OBČ"}

prpo={
"B":"BREZ POŠKODBE",
"H":"HUDA TELESNA POŠKODBA",
"L":"LAŽJA TELESNA POŠKODBA",
"P":"SLED POŠKODBE",
"S":"SMRT",
}

lovc={
"H":"HITRA CESTA",
"L":"LOKALNA CESTA",
"N":"NASELJE Z ULIČNIM SISTEMOM",
"T":"TURISTIČNA CESTA",
"V":"NASELJE BREZ ULIČNEGA SISTEMA",
"0":"AVTOCESTA",
"1":"GLAVNA CESTA I. REDA",
"2":"GLAVNA CESTA II. REDA",
"3":"REGIONALNA CESTA I. REDA",
"4":"REGIONALNA CESTA II. REDA",
"5":"REGIONALNA CESTA III. REDA",

"A":"AVTOCESTA",
"M":"GLAVNA CESTA",
"R":"REGIONALNA CESTA",
}




prkd={
"Ž":"ŽELEZNIŠKI PREHOD",
"A":"AVTOBUSNA POSTAJA",
"C":"CESTA",
"E":"ŽELEZNIŠKO POSTAJALIŠČE",
"K":"KOLESAR. ST. ALI PLOČNIK",
"M":"KROŽNO KRIŽIŠČE",
"N":"NARAVNO OKOLJE",
"O":"NARAVOVARSTVENO OBMOČJE",
"P":"PARKIRNI PROSTOR",
"R":"KRIŽIŠČE",
"V":"VLAK",
"Z":"PREHOD ZA PEŠCE",
}

prvz={
"CE":"NEPRAVILNOSTI NA CESTI",
"HI":"NEPRILAGOJENA HITROST",
"NP":"NEPRAVILNOSTI PEŠCA",
"OS":"OSTALO",
"PD":"NEUPOŠTEVANJE PRAVIL O PREDNOSTI",
"PR":"NEPRAVILNO PREHITEVANJE",
"PV":"PREMIKI Z VOZILOM",
"SV":"NEPRAVILNA STRAN / SMER VOŽNJE",
"TO":"NEPRAVILNOSTI NA TOVORU",
"VO":"NEPRAVILNOSTI NA VOZILU",
"VR":"NEUSTREZNA VARNOSTNA RAZDALJA",
}

prtn={
"ČT":"ČELNO TRČENJE",
"BT":"BOČNO TRČENJE",
"NT":"NALETNO TRČENJE",
"OP":"OPLAŽENJE",
"OS":"OSTALO",
"PP":"POVOŽENJE PEŠCA",
"PR":"PREVRNITEV VOZILA",
"PZ":"POVOŽENJE ŽIVALI",
"TO":"TRČENJE V OBJEKT",
"TV":"TRČENJE V STOJEČE / PARKIRANO VOZILO",
}

prvr={
"D":"DEŽEVNO",
"J":"JASNO",
"M":"MEGLA",
"N":"NEZNANO",
"O":"OBLAČNO",
"S":"SNEG",
"T":"TOČA",
"V":"VETER",
}

prsp={
"E":"NEZNANO",
"G":"GOST",
"N":"NORMALEN",
"R":"REDEK",
"Z":"ZASTOJI",
}

prpv={
"BL":"BLATNO",
"MO":"MOKRO",
"OS":"OSTALO",
"PN":"POLEDENELO - NEPOSIPANO",
"PP":"POLEDENELO - POSIPANO",
"SL":"SNEŽENO - PLUŽENO",
"SN":"SNEŽENO - NEPLUŽENO",
"SP":"SPOLZKO",
"SU":"SUHO",
}

prsv={
"AH":"HRAPAV  ASFALT / BETON",
"AN":"NERAVEN ASFALT / BETON",
"AZ":"ZGLAJEN ASFALT / BETON",
"MA":"MAKADAM",
"OS":"OSTALO",
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
}

aja={
    "D":"NASELJE",
    "N":"CESTA"
}






f = codecs.open("pn00.txt", encoding='cp852')
i = open("pn2000.csv","w")

i.write("FIOStevilkaZadeve$KlasifikacijaNesrece$UpravnaEnotaStoritve$DatumPN$UraPN$VNaselju$Lokacija$VrstaCesteNaselja$SifraCesteNaselja$TekstCesteNaselja$SifraOdsekaUlice$TekstOdsekaUlice$StacionazaDogodka$OpisKraja$VzrokNesrece$TipNesrece$VremenskeOkoliscine$StanjePrometa$StanjeVozisca$VrstaVozisca$GeoKoordinataX$GeoKoordinataY\n")

for vrsta in f:
    print(vrsta)
    if 1<len(vrsta):
        FIOStevilkaZadeve = vrsta[0:9].strip()
        KlasifikacijaNesrece = prpo[vrsta[9].strip()] if vrsta[9].strip()!="" else "?"
        UpravnaEnotaStoritve = loob[int(vrsta[10:14].strip())] if vrsta[10:14].strip()!="" else "?"
        DatumPN = vrsta[14:24].strip() if vrsta[14:24].strip()!="" else "?"
        UraPN = vrsta[24:26].strip() if vrsta[24:26].strip() !="" else "?"
        VNaselju = vrsta[29].strip() if vrsta[29].strip()!="" else "?"
        Lokacija = aja[VNaselju] if VNaselju!="" else "?"
        VrstaCesteNaselja = lovc[vrsta[30]] if vrsta[30].strip()!="" else "?"
        SifraCesteNaselja = vrsta[31:36].strip() if vrsta[31:36].strip()!="" else "?"
        TekstCesteNaselja = vrsta[36:61].strip() if vrsta[36:61].strip()!="" else "?"
        SifraOdsekaUlice = vrsta[61:66].strip() if vrsta[61:66].strip()!="" else "?"
        TekstOdsekaUlice = vrsta[66:91].strip() if vrsta[66:91].strip()!="" else "?"
        StacionazaDogodka = vrsta[91:95].strip() if vrsta[91:95].strip()!="" else "?"
        OpisKraja = prkd[vrsta[95].strip()] if vrsta[95].strip()!="" else "?"
        VzrokNesrece = prvz[vrsta[96:98].strip()] if vrsta[96:98].strip()!="" else "?"
        TipNesrece = prtn[vrsta[98:100].strip()] if vrsta[98:100].strip()!="" else "?"
        VremenskeOkoliscine = prvr[vrsta[100].strip()] if vrsta[100].strip()!="" else "?"
        StanjePrometa=prsp[vrsta[101].strip()] if vrsta[101].strip()!="" else "?"
        StanjeVozisca=prsv[vrsta[102:104].strip()] if vrsta[102:104].strip()!="" else "?"
        VrstaVozisca=prpv[vrsta[104:106].strip()] if vrsta[104:106].strip()!="" else "?"
        GeoKoordinataX="0"
        GeoKoordinataY="0"
        i.write(""+FIOStevilkaZadeve+"$"+KlasifikacijaNesrece +"$"+UpravnaEnotaStoritve +"$"+DatumPN +"$"+UraPN +"$"+VNaselju +"$"+Lokacija+"$"+VrstaCesteNaselja +"$"+SifraCesteNaselja +"$"+TekstCesteNaselja +"$"+SifraOdsekaUlice +"$"+TekstOdsekaUlice +"$"+StacionazaDogodka +"$"+OpisKraja +"$"+VzrokNesrece +"$"+TipNesrece +"$"+VremenskeOkoliscine +"$"+StanjePrometa +"$"+VrstaVozisca +"$"+StanjeVozisca +"$"+GeoKoordinataX +"$"+GeoKoordinataY+"\n")
i.close()