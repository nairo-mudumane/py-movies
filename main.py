import requests as req
import json

movie = None
def requestMovie(title):
    try:
        res = req.get('http://www.omdbapi.com/?apikey=[c39bdab8]&t='+str(title))
        res_json = json.loads(res.text)
        return res_json
    except Exception as err:
        print('Error:', err)
        return None
def print_details(movie):
    print('Titulo:',movie['Title'])
    print('Ano:',movie['Year'])
    print('Director:',movie['Director'])
    print('Actores:',movie['Actors'])
    print('Nota:',movie['imdbRating'])
    print('')  
    
exit = False
while not exit:
    opt = input('Esreva o nome de um filme ou SAIR para fechar: ')
    if opt == 'SAIR':
        exit = True
    else:
        movie = requestMovie(opt)
        if movie['Response'] == False:
            print('Filme nao encontrado!')
        else:
            print_details(movie)