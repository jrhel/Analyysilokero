# Analyysilokero

Analyysilokero on sovellus [kilpailevien hypoteesien analyysien](https://en.wikipedia.org/wiki/Analysis_of_competing_hypotheses) tekemiselle yhdessä ja/tai ryhmissä. Sovelluksessa käyttäjät laativat analyyseilleen hypoteesit, tallentavat löytämiään todisteita, laativat analyysejä näiden perusteella, sekä pystyvät selailemaan tallennettuja todisteita ja laadittuja analyysejä lokeroidusti. Sovellus ei opeta kilpailevien hypoteesien analyysien tekemistä, mutta sen tarkoituksena on asoiden analysoiminen järjestelmällisesti ja vähentää vinoumia lyhyesti seuraavasti:
1) Muodosta kysymys;
2) Aseta toisiaan poissulkevia hypoteesejä jotka itsessään vastaisivat kysymykseen niin että yhdessä ne kattavat kaikki mahdollisuudet;
3) Etsi jokaiselle hypoteesille todisteida jotka ovat ristiriidassa tämän kanssa, sekä kaikenlaista muuta asiaan littyvää tietoa;
4) Muodosta Hypoteeseistä ja todisteista taulukko, johon jompikumpi tulee pystyriville ja toinen vaakariville;
5) Arvioi jokaisen hypoteesin osalta miten jokainen kerätty todiste tukee tämän, esim. +1 jos tukee tai -2 jos on erittäin painava ristiriidassa oleva todiste, tai 0 jos sillä ei ole vaikutusta kyseiseen hypoteesiin, ja kirjaa arviot taulukkoon;
6) Laske yhteen tulokset, ja varsinaisesti erikseen ns. "miinuspisteet", ja valitse hypoteesi joka osoittautuu vähiten epätodennäköisemmäksi.

   
## Toteutetut toiminnot:
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään analyysilokeroon.- 
- Käyttäjä voi luoda uuden analyysin.
- Käyttäjä pystyy lisämään hypoteesejä analyyseihin.

## Toteutettavat toiminnot:
- Käyttäjä pystyy luomaan ryhmän ja kuuluvat ryhmätunnukset.
- Käyttäjä pystyy liittymään ryhmään johon sillä on tunnus.
- Käyttäjä pystyy lisäämään todisteita analyysilokeroon ja analyyseihin.
- Käyttäjä pystyy määrittämään kenelle lisäämänsä todiste näkyy.
- Käyttäjä pystyy hakemaan todisteita. 
- Käyttäjä voi antaa luotuihin ananyyseihinsä kirjoitusoikeudet tämän kuulumille ryhmien muille käyttäjille.
- Käyttäjä voi arvioida analyysien, johon on pääsy, lisättyjen todisteiden merkittävyys,
- Tuloksien laskeminen todisteiden arvioinnin perusteella ja lisääminen analyysiin,
- Käyttäjä voi julkaista analyysinsä niin, että kaikilla käyttäjillä tai vain tietyt käyttäjän kuulumilla ryhmillä on pääsy niihin.
- Käyttäjä voi avata analyysit joihin on pääsy.
- Käyttäjillä on omat sivunsa joissa heille näkyy luomansa sekä kuulumansa ryhmät, sekä analyysit johon on pääsy.
- Käyttäjä pystyy myös hakemaan analyysejä.
- Käyttäjä pystyy eroamaan ryhmistä.
- Käyttäjän omilla sivuilla näkyy jotain tilastoja tämän aktiviteetista.


## Mahdollisesti lisättävät toiminnot:

- Analyysien tulostaminen .pdf-tiedostoon.
- Todisteiden luotettavuuden määrittäminen.
- Kaikille julkiset analyysit päivittyvät käyttäjien omilla sivuilla niin että vain viimeiset näkyvät.
- Käyttäjä voi tallentaa analyysejä, jotta samaa analyysiä ei tarvitsisi etsiä toistamiseen, ja ryhmittää tallennetut analyysit.
- Käyttäjä pystyy piilottamaan analyysejä näkymästä omalla sivullaan.
- Käyttäjä pystyy piilottamaan ryhmiä näkymästä omalla sivullaan.
- Skenaarioiden kirjoittaminen analyysin perusteella.
- Analyysien versionhallinta.

## Sovelluksen asennus & käynnistys:
1) Mene komentorivillä hakemistoon johon haluat asentaa sovelluksen, ja lataa se lomennolla:
```
git clone https://github.com/jrhel/Analyysilokero.git
```
2) Luo hakemistoon Pythonin virtuaaliympäristön koomennolla ( a) Unix / b) Windows):
```
a) python3 -m venv venv   /   b) pip install virtualenv
```
3) Käynnistä virtuaaliympäristö koomennolla ( a) Unix / b) Windows):
```
a) source venv/bin/activate   /   b) venv\Scripts\activate.bat
```
4) Asenna [flask](https://github.com/pallets/flask/tree/main)-kirjasto komennolla:

```
pip install flask
```
5) Käynnistä sovellus komennolla:
```
flask run
```
6) Avaa sovelluksen käyttöliittymä selaimeessasi ositteella:
```
127.0.0.1:5000
```

## Sovelluksen testaus/käyttö:
Käyttääksesi sovelluksen joudut kirjautumaan sisään. Mikäli et ole luonut tunnuksia, voit luoda niitä aloitussivun alapäässä olevasta linkistä "Luo tunnus". Kun olet luonut tunnuksen, sovellus siirtää sinut automaattisesti omalle sivullesi josta voit käyttää sovellusta, ja kirjautua ulos. Jos haluat poistaa tunnuksesi, tai aloittaa alusta, voit poistaa tietokantatiedoston `database.db` samasta hakemistosta johon asensit sovelluksen. Sovellus luo automaattisesti sovelluksen tarvitsema tietokanta, ja huolehtii sen toiminnasta, mutta kaikkia siihen tallennetut tiedot ei vielä pääse käyttöliittymästä muokkaamaan. Tietokanta on kuitenkin sinänsä käytettävissä sqlite:lla. Tämä onnistuu käynnistämällä tietokannan sovelluksen hakemistosta komennolla `sqlite3 database.db` , jonka jälkeen voi syöttää suoraan tietokannalle SQL-komentoja. Esim. `SELECT * FROM User;` listaa kaikki käyttäjät ja näiden salasanojen hash-arvot.
