# Comparateur de contrats 
## Mars Manon M1 DENG 
### Objectif du projet 

        J’ai choisi de travailler sur le projet numéro 3 qui est un comparateur de contrats avec alertes. C’est-à-dire qu’il s’agit d’un outil qui reçoit deux fichiers textes et qui est capable de relever les différences entre les deux versions. Ces différences peuvent être par exemple : une date, une condition ou une clause. Une fois les différences relevées, l’outil est capable d’évaluer voire de classer l’importance des changements. Nous notons que les différences ne doivent pas uniquement être basées sur la forme mais également sur le fond et sens des mots. Certaines clauses qui ont qui ont été modifiées peuvent être considérées comme abusives ou illégales, dans ces cas, l’outil doit être en capacité de le signaler de manière claire. 

### Fonctionnalités attendues 

        Les fonctionnalités attendues sont les suivantes : 
        - Pouvoir déposer ses deux documents de manière pratique (drag and drop par exemple) 
        - Alerte sur les données modifiées 
        - Mise en avant claire de clauses abusives ou illégales 
        - Classement de l'importance des modifications de la plus à la moins "grave"

### Fonctionnalités supplémentaires si le temps le permet 

        - Éventuellement une possibilité d'accepter ou de refuser les changements 
        - Éventuellement une proposition de mail à envoyer à la personne responsable de l'édition du contrat suivant l'acceptation ou le refus des changements  

### Scope négatif 

        Nous ne pensons pas réaliser l’outil pour des documents formatés différemment, les deux versions seront similaires. Nous ne relèverons pas les différences non significatives comme les fautes de frappe. 

### Choix techniques 
        Au niveau des choix techniques, nous allons choisir de réaliser l’interface pour l’utilisateur en HTML/CSS et éventuellement JS si besoin car cela m’apparait comme le plus simple pour réaliser un front end. Le back end sera réalisé en Python (Flask) car Python est un langage très flexible et qui comporte une grande quantité de librairies, notamment des librairies d’océrisation qui pourront sûrement s’avérer pratiques. Nous utiliserons sûrement un appel à une api d’IA générative. 

### Contraintes techniques 

        Le comportement asynchrone de Flask peut éventuellement poser problème. Il faudra trouver une manière de contourner cette contrainte. 


### Difficultés anticipées 

        Je pense que la difficulté principale va résider dans la réalisation de prompts de qualité qui vont éviter que les IA génératives ne partent trop loin ou ne produisent des codes trop complexes que nous ne comprendrions pas et que nous n’arriverons pas à maintenir correctement. Ensuite, je pense que la liaison front/back va peut-être me poser problème car je n’ai jamais réalisé un « vrai » backend en python. Également, je n’ai jamais réalisé de projet impliquant l’appel à une API externe, donc je pense que je passerai beaucoup de temps à comprendre comment cela fonctionne. 

### Lien GitHub 

        https://github.com/ManonMars12/M1_PROJET_AI_GATEWAY 


