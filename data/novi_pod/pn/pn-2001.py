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
}
"""
"A":"AVTOCESTA",
"M":"GLAVNA CESTA",
"R":"REGIONALNA CESTA",
"""




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
"A":"ASFALT / BETON",
"M":"MAKADAM",
"O":"OSTALO",
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
nas={
    "1":"D",
    "0":"N"
}





f = codecs.open("PN04.txt")
i = open("pn2004.csv","w")

i.write("FIOStevilkaZadeve$KlasifikacijaNesrece$UpravnaEnotaStoritve$DatumPN$UraPN$VNaselju$Lokacija$VrstaCesteNaselja$SifraCesteNaselja$TekstCesteNaselja$SifraOdsekaUlice$TekstOdsekaUlice$StacionazaDogodka$OpisKraja$VzrokNesrece$TipNesrece$VremenskeOkoliscine$StanjePrometa$StanjeVozisca$VrstaVozisca$GeoKoordinataX$GeoKoordinataY\n")
for vrsta in f:
    print(vrsta)
    tab = vrsta.split("$")
    if 1<len(vrsta):
        FIOStevilkaZadeve = tab[0].strip()
        KlasifikacijaNesrece = prpo[tab[1].strip()] if tab[1].strip()!="" else "?"
        UpravnaEnotaStoritve = loob[int(tab[2].strip())] if tab[2].strip()!="" else "?"
        DatumPN = tab[3].strip() if tab[3].strip()!="" else "?"
        UraPN = tab[4].strip() if tab[4].strip() !="" else "?"
        VNaselju = nas[tab[5].strip()] if tab[5].strip()!="" else "?"
        Lokacija = aja[VNaselju] if VNaselju!="" else "?"
        VrstaCesteNaselja = lovc[tab[6]] if tab[6].strip()!="" else "?"
        SifraCesteNaselja = tab[7].strip() if tab[7].strip()!="" else "?"
        TekstCesteNaselja = tab[8].strip() if tab[8].strip()!="" else "?"
        SifraOdsekaUlice = tab[9].strip() if tab[9].strip()!="" else "?"
        TekstOdsekaUlice = tab[10].strip() if tab[10].strip()!="" else "?"
        StacionazaDogodka = tab[11].strip() if tab[11].strip()!="" else "?"
        OpisKraja = prkd[tab[12].strip()] if tab[12].strip()!="" else "?"
        VzrokNesrece = prvz[tab[13].strip()] if tab[13].strip()!="" else "?"
        TipNesrece = prtn[tab[14].strip()] if tab[14].strip()!="" else "?"
        VremenskeOkoliscine = prvr[tab[15].strip()] if tab[15].strip()!="" else "?"
        StanjePrometa=prsp[tab[16].strip()] if tab[16].strip()!="" else "?"
        StanjeVozisca=prpv[tab[17].strip()] if tab[17].strip()!="" else "?"
        VrstaVozisca=prsv[tab[18].strip()] if tab[18].strip()!="" else "?"
        GeoKoordinataX="0"
        GeoKoordinataY="0"
        i.write(""+FIOStevilkaZadeve+"$"+KlasifikacijaNesrece +"$"+UpravnaEnotaStoritve +"$"+DatumPN +"$"+UraPN +"$"+VNaselju +"$"+Lokacija+"$"+VrstaCesteNaselja +"$"+SifraCesteNaselja +"$"+TekstCesteNaselja +"$"+SifraOdsekaUlice +"$"+TekstOdsekaUlice +"$"+StacionazaDogodka +"$"+OpisKraja +"$"+VzrokNesrece +"$"+TipNesrece +"$"+VremenskeOkoliscine +"$"+StanjePrometa +"$"+StanjeVozisca +"$"+VrstaVozisca +"$"+GeoKoordinataX +"$"+GeoKoordinataY+"\n")
i.close()