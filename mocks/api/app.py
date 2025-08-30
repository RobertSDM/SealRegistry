from flask import Flask, request

from data import api_seals


app = Flask(__name__)


@app.get("/")
def home():
    return "Server Online"


@app.post("/transport/seal/checks")
def seal_check():
    seals = request.get_json()
    seals = set(seals)

    not_registered = list()

    for s in seals:
        if s not in api_seals["seals"]:
            not_registered.append(s)

    return not_registered
