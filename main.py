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
    
movie = requestMovie('interstelar')
print(movie)