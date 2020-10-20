from flask import Flask, redirect, request, session, render_template
from json import dumps
import urllib
from collections import OrderedDict
app = Flask(__name__)
app.debug = True
app.secret_key = "idkhph5pWPwQxNpxnJci2EK3ylY19udBVa9Ki5oW9kJZrZxUEsjGmRDawEBxuvh89rclpzirtlMNGa5EfSrIqdMYz8mtbAWIAO0WpGm4zBEQShZliQ08afaIFpADpyjC6NtitQAZpqHrSGXFEFlrD4hgOic6BInFTK6L5D6jztYbkdXwY2ilZW4W9Tv8vCKp3t9TcT11tWaaZTIxDKQrPRTYbVhDmaLHs6EBIK35LaQiZ7weBuYb1rSCjRdNjWY1QEQ4gVBs3E6tYIP3rv6P5u4kiEKWVlZC74otGOAYVqQOsA94wBueYF2MU6QVMgbh8UzCIWcHVvzC1zcghl1AOfNaQZzjk4MBlhqSC9V9qu19E9WZ0lVtQM6msG2x20UjwrQpGkpH1rfDnwNlrIPw2DUEBgudYriEaZsiLiTeqDrUc6IH4WQXAi7qojc5uErDb2h6DsX22B9sIDiAPxV8yytk6Y5H9wDrEFI33h5tvZD7ofw7H8GHgkmljxlp9McFXUjrbcNJcErTw7ZEFQ6TUMgMqQrmbprcXKzPlc0NkF0anDEzrJMHBbjjPaqhyTn88B0VNFqJBaqW15DUj9wULUmDkEUMOgT63OoQcIN7CVUxLPPK0iy01AIF72yn6hsKGPDw9ROAF7KbgARk27lott8wqZGZihqO80tD2P5O3pYXJHp2mlrWvFAuOOFTWCEUC9CLu14kmFjurm7MTNnfPTSF3VAzOBrCEw3iUG5agPaC67nFpoOQO1ewyhguxuWtBHW3Hl0y29zfnLKC5TnFQtnmGDOIgytOhosplNB7UTHexykW3BjVB9MoOHhywEMTMbQcB9oQCoRbBDwedSAvHifgNqqr4s9Dya7OpYtWMgIGtRBX8PFfHXbvthpU7vJPWmcbO3MVaOFWCduvw2YgO1EzVl5iFtvyprSC78kybIaASiX0NrGxlNMZjSS8GVc3qbP05tdEXkIFMXhbJFhLEl34leOWoHyZOiq7vi2QMOfAzATLjRXQGWj8p1vr2Dky"
steam_openid_url = 'https://steamcommunity.com/openid/login'

import user
import servers

@app.route("/")
def hello():
    return '<a href="http://localhost:5000/auth">Login with steam</a>'

@app.route("/auth")
def auth_with_steam():

    params = {
        'openid.ns': "http://specs.openid.net/auth/2.0",
        'openid.identity': "http://specs.openid.net/auth/2.0/identifier_select",
        'openid.claimed_id': "http://specs.openid.net/auth/2.0/identifier_select",
        'openid.mode': 'checkid_setup',
        'openid.return_to': 'http://127.0.0.1:5000/authorize',
        'openid.realm': 'http://127.0.0.1:5000'
    }

    query_string = urllib.parse.urlencode(params)
    auth_url = steam_openid_url + "?" + query_string
    return redirect(auth_url)

@app.route("/authorize")
def authorize():
    steamID = request.args["openid.claimed_id"].replace("https://steamcommunity.com/openid/id/", "")
    if user.IsValid(steamID):
        session["steamid"] = steamID
        return redirect("/web/")
    else:
        return user.InValid()

@app.route("/web/servers/get/<id>")
def serversGet(id):
    if not user.IsValid(session["steamid"]):
        return user.InValid()

    if id != "all":
        return ""
    else:
        serverList = servers.GetAll()
        print(serverList)
        return render_template("server.html", serverList = serverList)


@app.route("/web/")
def web():

    if not user.IsValid(session["steamid"]):
        return user.InValid()

    return "<button>Servers</button><button>Bans</button><a>Log Out</a>"

@app.route("/api/")
def api():
    print("Aye")
    return "Aye you found the API"


if __name__ == "__main__":
    app.run()
