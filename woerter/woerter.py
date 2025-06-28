import random as r
import time

woerter = {
    'der' : ['pass','eingang', 'roman','platz','bauerhof','durchschnitt','saal','nebel','fuehrerschein'
    ,'kunde','reparatur','husten','konzern','sessel','stadtrand','staub','direktor','buergersteig','tod','wal'
    ,'lachs','ingwer','essig','stoff','speichel','aufenthalt','seitensprung','becher','dienst','nacken','bruch'
    ,'duft','knochen','ofen','neid','instinkt','deich','segen','scherz','geist','laerm','auftrag','anteil'
    ,'hai','stil','weizen','ausweis','dom','umschlag','tacker','adler','faden','sitz','drache','krebs','knast'
    ,'aberglaube','satz','ast','zeuge','guertel','leichnam','blumenstrauss','baunstamm','aermel','ritter','welpe'
    ,'wischmopp','Film','monat','kurs','plan','park','test','vogel','grund','experte','typ','käse','preis','tag'
    ,'dialog','prozess','market','sport','balkon','bus','eingang','eintritt','automat','name','fuß','ball'
    ,'fehler','friseur','ort','job','baum','joghurt','koffer','kuechen','Koch','apfel','schrank','liter'
    ,'wunsch','meter','pfeffer','reis','rücken','stress','stock','tee','teller','zucker','punkt','zwiling'
    ,'Laden','wind','atem','zirkus','zahn','faktor','motor','korb','notfall','schnee','laptop','computer'
    ,'raum','erfolg','regen','spiegel','tunnel','schmetterling','freund','gorilla','weg','Ballon','zylinder'
    ,'hut','comic','trend','zoo','Vulkan','radiergummi','ring','eimer','artikel','berg','bahnhof','zug'
    ,'Frühling','körper','kopf','besen','nachbar','schritt','Dialekt','Krimi','anzug','bart','stein','tropfen'
    ,'strand','sand','text','frieden','krieg','teil','arm','Kommentar','schock','satz','mund','nagel'
    ,'tisch','apparat','mond','rabatt','verkehr','club','stuhl','bleistift','fluss','komm','kopfschmerz'
    ,'wettbewerb','bauch','traum','kaffee','morgen','abend','grad','salat','müll','Bildschirm','aufzug','stau'
    ,'fisch','ring','stern','knopf','himmel','wind','teppich','löfel','hals','ellbogen','honig','finger'
    ,'wagen','wald','flur','donner','blitz','osten','boden','unterricht','fuchs','löwe','affe'],

    'das' : ['foto','bild','ziel','lebensmittel','loch','stueck','museum','buegeleisen','ergebnis','feld'
    ,'gewitter','rind','fett','getreid','gleis','gehalt','waschbecken','gedicht','ereignis','mitglied','seil'
    ,'gebirge','mehl','zitat','netz','stipendium','heim','pflaster','besteck','pech','schach','geheimnis','raetsel'
    ,'erdgeschoss','gift','rad','stadion','zelt','schwert','testament','fell','haeschen','Ende','finale','album'
    ,'ticket','fest','viertel','festival','konzert','dokument','experiment','magazin','jahr','top','bild'
    ,'foto','duell','niveau','match','hoch','angebot','aspirin','schwimmbad','bett','regal','spiel','essen'
    ,'Cafe','datum','diktat','ding','paar','fieber','formular','Gramm','gepäck','kilo','menü','ohr','auge'
    ,'papier','radio','salz','pferd','schaf','schiff','sofa','taxi','wort','team','tennis','telefon','wunder'
    ,'zertifikat','papier','bein','zeugnis','restaurant','video','interview','glas','zeichnen','Alter','phänomen'
    ,'teleskop','gel','puzzle','ketschup','institut','tuch','projekt','programm','Parfüm','dorf','hobby','theater'
    ,'Gebäude','organ','hotel','blut','dach','bier','problem','klavier','land','gespräch','schloss','lebewesen'
    ,'intersse','kleid','haus','büro','geld','feuer','herz','radio','selber','brot','dorf','wasser','eis'
    ,'fleisch','haar','gehirn','insekt','meer','licht','rezept','gericht','holz','messer','gesicht','plastic'
    ,'leder','metall','gras','klima','produkt','kapitel','kostüm','geschenk','kamel','ei','atom'],

    'die' : ['birne', 'lampe', 'anlage','bettdecke','wange','herkunft','wimpern','frucht','furcht','feige','sahne'
    ,'pfanne','konditorei','ampel','insel','aussicht','grenze','ameise','muecke','schildkroete','kuechenschabe'
    ,'schuerze','drogorie','traube','agentur','schublade','gebuehr','druese','kueste','bohne','matratze','armut'
    ,'presse','laune','flut','ausrede','eifersucht','halskette','seite','gerste','ernte','grippe','flaeche','mandel'
    ,'klingel','ecke','dichte','pistole','handschellen','geldboerse','kneipe','waffe','schicht','feuerwehr','faust'
    ,'wurzel','mappe','zutaten','hoehle','rasse','person','zeit','woche','tasse','Region','mail','musik','city'
    ,'Wahl','post','kasse','luft','villa','konferenz','saison','sprache','regel','ecke','banana','birne'
    ,'dauer','soße','disko','dusche','Karte','nummer','Gitarre','hand','krawatte','küche'
    ,'Mitte','oper','puppe','sauna','schokolade','temperatur','tour','kantine','zigarette','szene','stadt','blume'
    ,'Kamera','Nase','Möbel','generation','tomate','flasche','palme','vase','erde','mango','Wunde','perücke','lust','echse'
    ,'sache','Agentur','mode','firma','feier','ferien','Mauer','Wand','ananas','limonade','Bahn'
    ,'Bibliothek','leber','serie','klasse','Tafel','Pause','adresse','wüste','burg','keramik'
    ,'zentrale','farbe','etage','orange','erdkunde','haut','maus','kunst','seele','torte','wassermelone'
    ,'erdbeere','mall','mail','nacht','zukunft','bürste','spange','wäsche','flasche','blume','tür','biene'
    ,'fleige','spinne','sonne','kosmetik','kartoffel','hose','luft','brücke','brille','treppe','bank','decke'
    ,'wand','lampe','zitrone','marmelade','zweibel','gabel','haut','brust','schulter','zunge','lunge','hüfte'
    ,'lippe','reise','apotheke','kasse','praxis','medizin','diät','angst','schuld','wolke','wüste','pflanze'
    ,'maschine','notiz','fabrik','eule','schlange','menge','seele','guerkel']
}

all_woerter = [wort for value_list in woerter.values() for wort in value_list]
random_wort = r.choice(all_woerter)
random_wort_key = None
for key, value_list in woerter.items():
    if random_wort in value_list:
        random_wort_key = key
        break
all_woerter = [wort for value_list in woerter.values() for wort in value_list]

x = len(all_woerter)
correct = 0
wrong = 0
wrong_woerter = {}
start_time = time.time()
no_woerter = 0

def game(no__woerter = x):
    global correct, wrong, wrong_woerter, start_time, no_woerter
    if not all_woerter or no_woerter == no__woerter:
        print('the woerter has finished')
        end_time = time.time()
        time_taken = end_time - start_time
        percentage = (correct / x)* 100
        print(time_taken)
        print(percentage)
        print(wrong)
        print(wrong_woerter)
    else:
        random_wort = r.choice(all_woerter)
        for key, value_list in woerter.items():
            if random_wort in value_list:
                random_wort_key = key
        all_woerter.remove(random_wort)
        artikel = ['der', 'das', 'die']
        no_woerter += 1
        print(no_woerter)
        print(random_wort)
        answer = input('please write the article:  ')
        if answer.strip() not in artikel:
            print('please enter der or das or die')
            input('please write a right article:  ')
            game()
        else:
            if answer.strip() == random_wort_key:
                print('right')
                print('')
                correct += 1
                game()
            else :
                print ('wrong, the article is' + ' : '+ str(random_wort_key))
                print('')
                wrong += 1
                wrong_woerter[random_wort_key] = random_wort
                time.sleep(1.0)
                game()
game()
