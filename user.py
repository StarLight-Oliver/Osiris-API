
a = {
        "76561198110564499": True,
}

def IsValid(steamID):
        return steamID in a
def InValid():
    return 'Sadly you are not authorized<br><a href="http://localhost:5000/auth">Login with steam</a>'
