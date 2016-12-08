# nginx-docker


volledige installatie guide van begin tot eind tot sylius draait.

- nieuwe map voor je project 
- twee mapjes maken een voor nginx een voor postgres.
	- hierin maak je twee Dockerfiles
	- zorg ervoor dat docker de meeste commando’s (eigenlijk alle commando’s kan uitvoeren specificeer die in de Dockerfiles! 
- vervolgens maak je een docker-compose.yml file
	- hierin staan de images die je gebruikt
	- poorten die open worden gezet
	- mappen die je wil delen tussen de host en client
	- er kan nog veel meer check https://docs.docker.com/compose/compose-file/
- wanneer de docker-compose ook geschreven is kun je de terminal openen
- zorg ervoor dat docker werkt.. (typ docker en enter)
- docker-compose up (bij de eerste keer gaat docker dan de images bouwen.)

- Het is niet erg om een container of image opnieuw op te moeten bouwen zolang je Dockerfile maar compleet is. 

Nadat Docker de images en containers heeft gecreëerd zal er een melding komen met build succesfully of een foutmelding.. 
docker ps -a dit geeft aan of er containers zijn gemaakt en hun status en ports. 
docker images geeft alle images weer (dus het platform waar containers op worden gebouwd)
docker-compose start (Wanneer de containers nog niet waren gestart)
Docker geeft een melding als de containers zijn gestart..

- docker inspect containernaam hier kan je zien of de container draait en welke poort en ip die gebruikt. dit is nodig voor de het parameter bestand wat je later moet maken. 
om in je container te komen kun je het volgende typen
- docker exec -it containernaam bash (wanneer de container al draait)
    	Dit moet ook in een Dockerfile of composefile kunnen maar dan moet ik meer onderzoek doen..
    	- Sylius installeren
    	- Gebruik Composer of GitHub.. even kijken wat werkt..
- composer create-project -s beta sylius/sylius-standard projectnaam
    	- Laat Composer z’n werk doen tot dat hij vraagt om een aantal dingen. dit worden je installatie parameters zorg 	ervoor dat deze kloppen met de gegevens die je hebt.
- cd projectnaam (ga in de juist aangemaakte map)
- npm install (wanneer npm niet werkt apt-get install npm(moet in je dockerfile!))
- npm run gulp     
- php bin/console sylius:install 
	- In theorie zou Sylius nu moeten installeren zo niet kijk wat de error is en naar de requirements..
	- Eventueel tijdzone aanpassen: nano /etc/php/7.0/php.ini 
	- Zoek naar timezone en uncomment die met timezone = Europe/Amsterdam
	- Herhaal vorige stap (sylius install)
- Sylius gaat nu installeren duurt een tijdje maar zolang die stappen aan blijft geven gaat het goed zo niet google op de foutmelding..
- Wanneer sylius is geinstalleerd, open je webbrowser en ga naar de poort en adres (localhost:8080 bijv)
	- 502 bad gateway check je nginx config. zorg ervoor dat het project in /usr/share/nginx/html/projectnaam staat of in html zelf..
	- In je /etc/nginx/conf.d/default.conf (daar ergens) check of je de juist socket hebt  
	fastcgi_pass unix:/run/php/php7.0-fpm.sock;	
	geldt ook voor de php fpm config (google it)
	https://www.nginx.com/resources/wiki/start/topics/recipes/symfony/ 
	- /etc/nginx/nginx.conf check of de user www-data is
	- service nginx reload  
  	- service php7.0-fpm restart 
	- Krijg je nog foutmeldingen (permission denied) zorg dan de gebruiker in de config klopt dat zou www-data moeten 	  zijn en die heeft ook de permissie nodig voor de project mappen.
        om dit te bekijken en veranderen gebruik je ls -ld in de map van het project daar moet user www data staan en group         www data staat het er niet,
	chown -R gebruiker:groep map 
- als het goed is zou nu alles moeten werken zo niet check of alle mappen zijn overgedragen naar de andere user.. zie hierboven.
