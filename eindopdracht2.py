print("Er is een oorlog uitgebroken in jou land en er word heftig gevochten in jou woon plaats. Jij  en je familie moet en vluchten. Jullie plan is om naar nederland te gaan, maar daar voor moeten jullie nog wel heel wat kilometer maken en langs streng bewapende grensen gaan.")

def  een():
    print('hoe ga je vluchten?')
    print('/n')
    print('A:jullie gaan met de bus?')
    print('B:jullie gaan te voet')
    antwoord = input(': ')
    if antwoord == "a":
        drie()
    elif antwoord == "b":
        twee()
    else: 
        print("Voer een geldig antwoord in. A/B")


def  twee():
    print('\n')
    print('het is niet overal vijlig in het land omdat het leger op zoek is naar mensen die vluchten. Jij en je familie moeten beslissen waar jullie gaan slapen')
    print('\n')
    print('A: in een tent')
    print('B: in een hostel')
    antwoord = input(': ')
    if antwoord == "a":
        drie()
    elif antwoord == "b":
        drie()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  drie():
    print('\n')
    print(' Jij en je famielie moeten nog best een stuk af leggen maar helaas rijden er geen bussen meer dus moeten jullie lopen. Naar een dag of twee komt er een busje langs en vraagt of jullie een lift nodig hebben. Jullie weten niet of het vijlig is maar zijn wel al kapot van het lopen.')
    print('/n')
    print("gaan jullie met heb busje mee")
    print('A:ja wenem het ricico')
    print('B:nee we lopen verder')
    antwoord = input(':')
    if antwoord == "a":
        vijf()
    elif antwoord == "b":
        vier()
    else: 
        print("Voer een geldig antwoord in. A/B")


def  vier():
    print('\n')
    print('het is niet overal vijlig in het land omdat het leger op zoek is naar mensen die vluchten. Jij en je familie moeten beslissen waar jullie gaan slapen ')
    print('A: in een tent')
    print('B: in een hostel')
    antwoord = input(': ')
    if antwoord == "a":
        print("jullie zijn gaan slapen in een tent. Omdat het een redelijk onveilig gebied is het er de hele tijd minimaal 1 persoon de wacht. Gelukkig het de nacht goed verlopen en is er niks gebeurt, nu kunnen jullie weer verder met de tocht richting de grens ")
    elif antwoord == "b":
        print("jullie zijn gaan slapen in een hostel waar jullie gerust konen slapen, nu zijn jullie goed uitgerus en kunnen jullie weer verder naar de grens")
    else: 
        print("Voer een geldig antwoord in. A/B")

def  vijf():
    print('\n')
    print('jij en je familie worden afgezet door de bestuurden van het busje, bij een dorpje dicht in de buurt van de grens. Het is van af hier nog maar vier uur lopen.')
    print('\n')
    print("julie komen aan bij de eerte grens post. Er staan heel veel bewaker en lange rijen. jullie kunnen er voor kiezen om te gaan wachten in de rij en mischien niet door gelaten te worden of jullie gaan proberen mee te rijden in een vracht wagen ")
    print("\n")
    print("wat gaan jullie kiezen")
    print('A:in de rij wachten en mischien niet door gelaten te worden')
    print('B:mee rijden in een vracht wagen')
    antwoord = input(': ')
    if antwoord == "a":
        zeven()
    elif antwoord == "b":
        zes()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  zes():
    print('\n')
    print('na een tijdje rond vragen is het jullie gelukt om een lift te krijgen. Jullie stappen in de laad ruimte van een varachwagen en rijden de grens over zonder moeite.')
    print('na twee uur rijden word de vracht wagen gestopt en horen jullie stemmen. Als de deuren open gedaan worden zien jullie twee agenten staan. ')
    print("\n")
    print("wat gaan jullie doen?")
    print('A: jullie rennen weg')
    print('B: julie blijven zitten')
    antwoord = input(': ')
    if antwoord == "a":
        tien()
    elif antwoord == "b":
        tien()
    else: 
        print("Voer een geldig antwoord in. A/B")


def  zeven():
    print('\n')
    print('Jullie hebben zeker drie dagen moeten wachten en zijn nu eindelijk de grens over. ')
    print('Hoe gaan jullie verder?')
    print('A:Jullie gaan proberen een vliegtuig te nemen op het vlieg veld en een vlucht te pakken naar een veilig buur land')
    print('B:Jullie gaan probeeren verder te lopen/liften.')
    antwoord = input(': ')
    if antwoord == "a":
        negen()
    elif antwoord == "b":
        acht()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  acht():
    print('\n')
    print('jullie moeten ergens slapen.')
    print('waar gaan jullie in slapen?')
    print('A: in een tent')
    print('B:in een hostel')
    antwoord = input(': ')
    if antwoord == "a":
        negen()
    elif antwoord == "b":
        negen()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  negen():
    print('\n')
    print("na een goede nacht rust kunnen jullie weer verder")
    print("\n")
    print('jullie hebben een taxi genomen naar het vliegveld en zijn van plan een vlucht te pakken naar en veiliger gebied')
    print('welke vlucht pakken jullie ')
    print('A: de lange minder veilige vlucht')
    print('B: de korte veilige vlucht')
    antwoord = input(': ')
    if antwoord == "a":
        print("Jullie vliegtuig is door een onveilig gebied gevlogen en is neer gestort en alle passagiers zijn dood gegaan")
    elif antwoord == "b":
        veertien()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  tien():
    print('\n')
    print('een maal op het politie bureau moeten jullie een legitimatie bewijs laten zien')
    print('gaan jullie dat doen ')
    print('A: ja doet doen we')
    print('B: nee dat doen we nii')
    antwoord = input(': ')
    if antwoord == "a":
        elf()
    elif antwoord == "b":
        twaalf()
    else: 
        print("Voer een geldig antwoord in. A/B")        

def  elf():
    print('\n')
    print('jullie hebben de juiste papieren bij jullie en worden door de politie naar een treistation gebracht')
    print('')
    print('A: de lange minder veilige rit')
    print('B: de korte veilige rit')
    antwoord = input(': ')
    if antwoord == "a":
        veertien()
    elif antwoord == "b":
        veertien()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  twaalf():
    print('\n')
    print('Jullie moeten een nacht in de cel zitten en onder tussen worden jullie spullen door zocht. De volgende Ochten worden jullie wakker gemaakt en moeten jullie mee terug naar de grens.')
    print('bij de gresns aan gekomen moeten jullie toch in de rij gaan staan om binnen te komen. Na twee dagen wachten zijn jullie eindelijk binnen.')
    print("\n")
    print("hoe gaan jullie nu verder")
    print('A:Jullie gaan proberen een vliegtuig te nemen op het vlieg veld en een korte vlucht te pakken naar een veilig buur land')
    print('B:Jullie gaan probeeren verder te lopen/liften')
    antwoord = input(': ')
    if antwoord == "a":
        dertien()
    elif antwoord == "b":
        vijftien()
    else: 
        print("Voer een geldig antwoord in. A/B")


def  dertien():
    print('\n')
    print('Jullie hebben de taxi genomen naar het vliegveld en zijn van plan een vliegtuig te pakken naar een veiliger gebied')
    print('Welke vlucht pakken jullie ')
    print('A: de lange minder veilige vlucht')
    print('B: de korte veilige vlucht')
    antwoord = input(': ')
    if antwoord == "a":
        print("Jullie vliegtuig is door een onveilig gebied gevlogen en is neer gestort en alle passagiers zijn dood gegaan")
    elif antwoord == "b":
        veertien()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  veertien():
    print('\n')
    print('jullie zijn aan gekomen in duitsland. de afstand tot de nederlandse grens in niet zo ver meer.')
    print('hoe gaan jullie')
    print('A: lopen')
    print('B: liften')
    antwoord = input(': ')
    if antwoord == "a":
        zestien()
    elif antwoord == "b":
        zestien()
    else: 
        print("Voer een geldig antwoord in. A/B")


def  vijftien():
    print('\n')
    print('jullie zijn aan gekomen op een vlieg veld in de buurt van Nederland')
    print('hoe gaan jullie naar de grens?')
    print('A: weer lopen ')
    print('B: van jullie laatste geld een bus kaartje halen')
    antwoord = input(': ')
    if antwoord == "a":
        vijftien()
    elif antwoord == "b":
        zestien()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  zestien():
    print('\n')
    print('jullie zijn aan gekomen bij de nederlandse grens')
    print('wat gaan jullie doen?')
    print('A: naar het azc (asielzoekerscentrum)')
    print('B: naar Amsterdam')
    antwoord = input(': ')
    if antwoord == "a":
        zeventien()
    elif antwoord == "b":
        print("jullie zijn naar Amsterdam gegaan en zijn nu opzoek naar woon plaats. Zo dra jullie aan komen zien jullie hoe groot en hoe druk de stad is. als jullie in de nacht rond lopen over de dam worden jullie berooft door een groep jongeren en jullie zij alles kwijt geraakt.  Helaas is jullie reis voor niks geweest")
    else: 
        print("Voer een geldig antwoord in. A/B")

def  zeventien():
    print('\n')
    print('jij en je familie zijn naar het azc gegaan om rustig te wennen aan Nederland en hoe alles hier werkt. Jullie gaan nu een beetje het leven proberen op te pakken en naar school te gaan en te werken ')
    print('\n')
    print('na twee maanden willen jullie best een eigen huis krijgen, er is genoeg gespaart voor een klein huisje.')
    print ("waar willen jullie gaan wonen?")
    print('A: in Amsterdam')
    print('B: in een dorpje op het platte land')
    antwoord = input(': ')
    if antwoord == "a":
        achtien()
    elif antwoord == "b":
        achtien()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  achtien():
    print('\n')
    print('jullie wonen nu in een mooi huis')
    print('jij kan weer je opleiding oppakken of gaan werken')
    print("wat goe je doen")
    print('A: naar school/opleiding')
    print('B: je gaat ergens werken')
    antwoord = input(': ')
    if antwoord == "a":
        negentien()
    elif antwoord == "b":
        twintig()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  negentien():
    print('\n')
    print('je hebt het leuk op je school en er word aan je gevraagt of je mee naar de stad gaat om te chillen')
    print('ga je mee?')
    print('A: ja')
    print('B: nee')
    antwoord = input(': ')
    if antwoord == "a":
        ()
    elif antwoord == "b":
        ()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  twintig():
    print('\n')
    print("je hebt een leuke baan kunnen vinden en hebt leuke colega's")
    print('ze vragen je mee naar een borrel ga je mee?')
    print('A: ja ')
    print('B: nee')
    antwoord = input(': ')
    if antwoord == "a":
        eenentwintig()
    elif antwoord == "b":
        eenentwintig()
    else: 
        print("Voer een geldig antwoord in. A/B")

def  eenentwintig():
    print('\n')
    print('na dat jullie twee jaar in nederland hebben gewoond hebben is jullie land eidelijk klaar met het voeren van een oorlog. jullie hebben een mooilijke keuzen te maken')
    print('\n')
    print("")
    print('A: blijven jullie in nedeland')
    print('B: gaan jullie terug naar jullie oude woongebied')
    antwoord = input(': ')
    if antwoord == "a":
        print(" De familie is in Nederland geblevevn en hebben een gelukkig leven kunnen hebben .")
    elif antwoord == "b":
        print("de famlilie is terug gegaan en hebben een heel gelukkig leven kunnen hebben")
    else: 
        print("Voer een geldig antwoord in. A/B")







een()





