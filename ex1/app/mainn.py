from fastapi import FastAPI
import logging
import os

app = FastAPI()

livello_scelto = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=livello_scelto)

@app.get("/salute")
def salute_controllo():
    logging.debug("La probe /salute stata chiamata!")
    return {"status" : "ok"}

@app.get("/saluta/{nome}")
def saluta_c(nome: str):
    
    logging.info(f"Sto salutando {nome}")
    return {"messaggio" : f"ciao {nome}"}

@app.get("/salva/{nome}")
def salva_c(nome: str):
    if nome.isdigit():
        logging.error(f"Errore: l'utente ha inserito dei numeri ({nome}) invece di un nome!")
        return {"errore": "Inserisci un nome valido fatto di lettere, non numeri"}

    logging.info(f"Avvio salvataggio per {nome}")
    
    with open("data/log.txt", "a") as file:
        file.write(f"{nome} registrato\n")
        
    return {"risultato" : f"movimenti di {nome} salvati nel file"}

@app.post("/agenda")
def agenda_c(dati_grezzi: dict):
    print(f"JSON in entrata: {dati_grezzi}")

    return {"dati_ricevuti": dati_grezzi}