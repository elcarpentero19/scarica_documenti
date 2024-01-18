#!/usr/bin/python3
# coding=utf-8

'''
*******************************************************************************
* Nome dello script: scarica_documenti.py
* Versione: 1.0
* Data: 18 gennaio 2024
*
* Descrizione:
* Questo script è distribuito gratuitamente su TuttoGenealogia.it 
* Forum per gli appassionati di genealogia italiana
* per condivisione e utilizzo da parte della comunità. È possibile
* modificarlo e ridistribuirlo a proprio piacimento, ma si prega di mantenere
* questa intestazione inalterata e di fornire un credito appropriato
* all'autore originale.
*
* Autore: Alessandro Simonetti 
* Profilo: https://www.tuttogenealogia.it/memberlist.php?mode=viewprofile&u=27451
*
* Avvertenza:
* Questo script viene fornito "così com'è" senza alcuna garanzia,
* implicita o esplicita. L'autore non è responsabile per eventuali danni
* derivanti dall'uso di questo script.
*******************************************************************************

Devono essere installati i seguenti moduli:

- requests 
- pillow
    
'''

import requests
from PIL import Image
from io import BytesIO

try:
    codici = filter(lambda x: x != "", open("atti.txt","r").read().split('\n'))

except OSError:
    print("Errore: non riesco a trovare il file 'atti.txt' nella cartella corrente.")
    print("Non posso scaricare nulla.\n")
    exit(1)

print("Leggo i codici riportati nelle righe del file atti.txt")

for num, codice in enumerate(codici):
    url = f'https://iiif-antenati.cultura.gov.it/iiif/2/{codice}/full/full/0/default.jpg'
    
    try:
        response = requests.get(url)

    except requests.exceptions.RequestException as e:
        print("Errore di connessione\n------\ndi seguito sono riportate informazioni di dettaglio:\n")
        raise SystemExit(e)
    
    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print("Errore HTTP\n------\ndi seguito sono riportate informazioni di dettaglio:\n")
        raise SystemExit(err)

    print(f"codice {codice}", end=" - ")
    img = Image.open(BytesIO(response.content))
    img.save(f'immagine {num:02}.jpg')
    print(f'ho scaricato: immagine {num:02}.jpg')

print("fine!")
