# scarica_documenti
Script in Python per scaricare dal Portale Antenati immagini ad alta risoluzione identificate tramite codice.

## installazione
- Posizionare il file scarica_documenti.py in una cartella di propria scelta.
- Verificare se sul proprio sistema è già installato Python v3.*
- Installare i moduli **requests** e **pillow** (usate google se non sapete come fare)

## esecuzione
Per eseguire lo script e scaricare un certo numero di immagini da Antenati occorre anzitutto inserirne i codici, uno per ogni riga, all'interno di un file di testo con nome "atti.txt".  
Ad esempio, se nel file atti.txt sono stati inseriti 3 codici (LoZnvPj, wEJEjBd, La6Vj9b) eseguendo questo script si scaricheranno 3 file nella cartella corrente:  

LoZnvPj &rarr; immagine 00.jpg  
wEJEjBd &rarr; immagine 01.jpg  
La6Vj9b &rarr; immagine 02.jpg  

Per l'esecuzione dello script suggerisco anzitutto di aprire un terminale nella cartella usata per lo script.  

Quindi, se si usa Windows digitare:  
`python3 -m scarica_documenti`

Se invece si usa Linux:  
`./scarica_documenti.py`
