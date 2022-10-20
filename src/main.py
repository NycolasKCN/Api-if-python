# Objetivo - Manipular lista de mangás de um usuario no site yabu e com isso deixar essa lista em nuvem (O site trabalha apenas com cookies e não tem serviço em nuvem)
# URL Base - para fase de desenvolvimento usaremos o localhost
# Endpoints : 
#
#   - localhost/user/favorites (GET) : pegar todos os mangás favoritados do usuario
#   - localhost/user/favorites (POST) : adicionar um novo mangá ao favoritos
#   - localhost/user/favorites (DELETE) : deletar um mangá favoritado
#   - localhost/user/read (GET) : pegar todos os mangás lidos
#   - localhost/user/read (POST) : adicionar todos os mangás lidos
#   - localhost/user/read (DELETE) : deletar todos os mangás lidos
#  
# Funcionalidades - Gerenciamento de conta na nuvem

from flask import Flask, jsonify, request

api = Flask(__name__)

mangas_favs_test = [
    
    {
        "id" : "",
        "name" : "Solo Leveling",
        "url" : "https://mangayabu.top/manga/solo-leveling/"
    },
    {   
        "id" : "",
        "name" : "Kaijuu 8-gou",
        "url" : "https://mangayabu.top/manga/kaijuu-8-gou/ "
    },
    {
        "id" : "",
        "name ": "Chainsaw Man ",
        "url ": "https://mangayabu.top/manga/chainsaw-man/ "
    },
    {
        "id" : "",
        "name ": "Aku no Hana ",
        "url ": "https://mangayabu.top/manga/aku-no-hana/ ",
    }
]