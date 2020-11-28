# Dino AI Game

## Inleiding

Dit project heeft als doel de dinosaurus game van Chrome namaken en een Genetic Algorithm te schrijven dat de optimale parameters kan zoeken om het spel te spelen.

## Structuur van het project

 - **DinoAI**: Dit is de root folder. Alle projectfiles zitten hierin.
    - **main.py**: Dit bestand is een oude versie. Dit bevat het dinospel dat gespeeld kan worden door de speler. Dit was een poc voor de game.
    - **gamain.py**: Dit bestand is de nieuwe versie en bevat de game speelbaar door een genetic algorithm.
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
        
## Opmerkingen

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