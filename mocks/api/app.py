from flask import Flask, request, abort

from data import api_seals


app = Flask(__name__)


@app.get("/")
def home():
    return "Server Online"


@app.get("/transport/seal/check")
def seal_check():
    try:
        seal = int(request.args.get("seal", 0))

        if seal not in api_seals["seals"]:
            return "", 404

        return "", 200
    except ValueError as e:
        return "", 422


@app.post("/transport/seal/register")
def seal_register():
    try:
        seal = int(request.args.get("seal", 0))

        if seal == 0:
            return "", 422

        api_seals["seals"].add(seal)

        return "", 200
    except ValueError as e:
        return "", 422
