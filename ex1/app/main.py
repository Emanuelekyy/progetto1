from fastapi import FastAPI
import random

app = FastAPI()

db = {"lanome" : ""}

@app.get("/salute")
def salute_c():
    print("qualcuno ha controllato la probe!")
    return{"status" : "ok"}

@app.get("/saluta/{nome}")
def saluta_c(nome: str):
    db["lanome"] = nome
    print(f"sto salutenado {nome}")
    return{"messagio" : f"ciao {nome}"}

@app.get("/salva/{nome}")
def salva_c(nome : str):
    print(f"sto salvando {nome}")
    with open("data/log.txt", "a") as file:
            file.write(f"attività di {nome} registrata\n")
    return{"risultato" : f"movimenti di {nome} salvata nel file"}

@app.get("/agenda")
def agenda_c():
     lista1 = ["docker", "dormire", "spesa"]
     azione = random.choice(lista1)

     return{"nome" : db["lanome"], "azione_assegnata" : azione}