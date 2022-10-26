# Objetivo - Manipular lista de mangás de um usuario no site yabu e com isso deixar essa lista em nuvem (O site trabalha apenas com cookies e não tem serviço em nuvem)
# URL Base - para fase de desenvolvimento usaremos o localhost
# Endpoints :
#
#   - localhost/user (GET) : Mostrar informações do usuario (nick, mangás e etc)
#   - localhost/user/favorites (GET) : pegar todos os mangás favoritados do usuario
#   - localhost/user/favorites (POST) : adicionar um novo mangá ao favoritos
#   - localhost/user/favorites (DELETE) : deletar um mangá favoritado
#   - localhost/user/read (GET) : pegar todos os mangás lidos
#   - localhost/user/read (POST) : adicionar todos os mangás lidos
#   - localhost/user/read (DELETE) : deletar todos os mangás lidos
#
# Funcionalidades - Gerenciamento de conta na nuvem

from flask import Flask, jsonify, request

app = Flask(__name__)

mangas_favs_test = [

    {
        "id": 1,
        "name": "Solo Leveling",
        "url": "https://mangayabu.top/manga/solo-leveling/"
    },
    {
        "id": 2,
        "name": "Kaijuu 8 gou",
        "url": "https://mangayabu.top/manga/kaijuu-8-gou/ "
    },
    {
        "id": 3,
        "name": "Chainsaw Man",
        "url": "https://mangayabu.top/manga/chainsaw-man/ "
    },
    {
        "id": 4,
        "name": "Aku no Hana",
        "url": "https://mangayabu.top/manga/aku-no-hana/ ",
    }
]

users = [
    {
        "id" : 1,
        "username" : "nyco",
        "mangaFavs" : []
    }
]


# O que será mostrado na URL "localhost:8080/"
@app.route("/", methods=["GET"])
def emptyPage():
    return "Nada por aqui."


# Endpoint da URL "localhost:8080/user/favorites" para mostrar todos os mangás favoritados
@app.route("/user/fav", methods=["GET"])
def getMangasFavs():
    return jsonify(mangas_favs_test)


# Endpoint da URL "localhost:8080/user/favorite" para adicionar um novo mangá favorito
@app.route("/user/fav", methods=["POST"])
def addMangaFav():
    newManga = request.get_json()
    mangas_favs_test.append(newManga)
    return getMangasFavs()


# Endpoint para desfavoritar um mangá
@app.route("/user/fav/<string:name>", methods=["DELETE"])
def removeMangaFavByName(name : str):
    for index, manga in enumerate(mangas_favs_test):
        if manga.get("name").lower() == name.replace("-", " ").lower():
            del mangas_favs_test[index]

            return getMangasFavs()
    return "Nenhum mangá encontrado"


# Endpoint que retorna as informações de um usert
@app.route("/user/<username>", methods=["GET"]) # Isso aqui funciona
def getUserInfo(username: str):
    for user in users:
        if user.get("username").lower() == username.lower():
            return user
    return "Nenhum usuário encontrado"


app.run(host="localhost", port=8080, debug=True)
