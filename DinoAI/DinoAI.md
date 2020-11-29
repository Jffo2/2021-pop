# Dino AI Game

## Inleiding

Dit project heeft als doel de dinosaurus game van Chrome namaken en een Genetic Algorithm te schrijven dat de optimale parameters kan zoeken om het spel te spelen.

## Structuur van het project

 - **DinoAI**: Dit is de root folder. Alle projectfiles zitten hierin.
    - **main.py**: Dit bestand is een oude versie. Dit bevat het dinospel dat gespeeld kan worden door de speler. Dit was een poc voor de game.
    - **gamain.py**: Dit bestand is de nieuwe versie en bevat de game speelbaar door een genetic algorithm.
    - **neatmain.py**: Dit bestand is eveneens een nieuwe versie die de game bevat die speelbaar is door neat agens.
    - **config**: Het configuratiebestand voor neat.
    - **img**: Deze folder bevat alle sprites gebruikt door de game. Bron voor deze sprites: [https://github.com/chirag64/t-rex-runner-bot](https://github.com/chirag64/t-rex-runner-bot)
    - **GameObjects**: Deze folder bevat alle objecten die gebruikt worden in de game.
        - **dinosaur.py**: Dit is het dinosaurus object.
        - **aidinosaur.py**: Dit object extend het dinosaurus object en voegt enkele methodes en velden toe die GA toelaten.
        - **ground.py**: Het object voorde grond.
        - **obstacle.py**: Een obstakel zoals een cactus of een vogel.
        - **obstacle_spawner.py**: Dit is een game object dat andere game objecten kan spawnen. Dit game object spawned nieuwe obstakels.
    - **GAHelpers**: Dit zijn klassen die gebruikt worden voor het GA algoritme.
        - **dna.py**: Via de aidinosaur.py wordt dna toegevoegd aan een dino die zijn gedrag zal bepalen.
        - **aidinobehavior.py**: Deze klasse zal het gedrag van de dino bepalen op basis van zijn dna.
        - **geneticsengine.py**: Deze klasse implementeert methoden voor het GA algoritme zoals crossover tussen dinosaurussen en natuurlijke selectie, alsook ondersteuning voor generaties.

## Opmerkingen gij GA

Het nadeel aan een GA oplossing is altijd dat men kennis moet hebben over de werking van het programma.
Hier ook is de dino gedetermineerd in zijn logica. Er zijn 2 parameters die hij leest, de afstand tot het eerstkomende obstakel en de y positie van het obstakel.
Het GA trained 3 variabelen. De eerste variabele, gebaseerd op de Y waarde van het obstakel, kiest of de actie is om te springen of te crouchen.
De volgende twee variabelen zijn gebaseerd op de afstand tot het obstakel en duiden de minimum afstand tot het obstakel aan vanaf wanneer actie ondernomen wordt.
Hier valt ook onmiddelijk op dat er niet 1 "beste" dinosaurus zal zijn.
Omdat er gesproken wordt over intervallen kan er dus gerust speling zitten op het interval waarbinnen de dinosaurus springt of kruipt.
Tot slot ook nog de opmerking over waarom niet gewerkt wordt met de officiële browsergame van Google Chrome.
Na enige research blijkt dat het heel moeilijk is om een image van de game state te krijgen (de browser moet steeds open staan, het window moet steeds dezelfde grootte hebben).
Er is ook een groot snelheidsprobleem. Het nemen van screenshots van de game neemt tijd in beslag (alle pixels moeten gemapped worden), en vervolgens moeten alle objecten herkend worden.
Het doorsturen van input is ook niet gemakkelijk naar het browserwindow. Uiteindelijk is dit ook niet de scope van dit project en blijft de logica voor het algoritme volledig hetzelfde.

## Opmerkingen bij neat

Het nadeel aan neat is dat het veel moeilijker is om te trainen omdat bijna geen kennis op voorhand op het model wordt opgedrongen.
Er worden inputs in het neurale netwerk voorzien die de omgeving illustreren en er worden outputs voorzien waarmee het netwerk acties kan uitvoeren.
De AI leert op zich heel snel de mechanics van de game kennen. Vanaf generatie 24 haal ik in de meeste gevallen al een AI die op de juiste moment kan springen.
Het probleem zijn de vogels die hoog in de lucht vliegen.
Omdat deze vogels relatief sporadisch voorkomen kan de AI zich hier moeilijk aan aanpassen.
Zo leert de AI eerst om overal over te springen en pas later kan hij leren om niet tegen de hoogste vogels te springen.
Gelukkig zijn neat netwerken heel versatiel en zal de AI uiteindelijk toch tot een oplossing komen. Ook al duurt het in dit geval langer.
Uiteindelijk na 311 generaties is neat erin geslaagd een netwerk te vinden dat de game kan spelen.
De winnende dino is een dino die rechtop loopt enkel wanneer er geen obstakels zijn op het scherm.
Van zodra een obstakel op het scherm komt bukt de dino zich.
Wanneer er een obstakel komt dat laag bij de grond is springt de dino,
en wanneer het obstakel hoger is dan blijft hij gebukt.
Ondanks dat het even duurde vooraleer neat een optimale oplossing vond ben ik wel heel trots.
Het is zeer fijn om een neuro-evolutionair netwerk te zien leren.

### Uitbreidingen van het neat project

 - [ ] Het visualiseren van het geleerde netwerk van 1 van de dino's
 - [ ] Het opslaan van de winnaar
 - [ ] Het toelaten van een replay van de winnaar
 - [ ] main.py, neatmain.py en gamain.py delen heel erg veel code, dit moet beter kunnen