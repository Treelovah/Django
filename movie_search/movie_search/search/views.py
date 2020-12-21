from django.shortcuts import render
import requests
import json
import argparse
import os




class Movie:
    def __init__(self):
        pass

    ## Globals
    page = 0
    year = 0
    name = ""
    m_hash = ""
    rating = 0
    image = ""

## POC

def home(request):

    if request.POST == '':
        pass
    else:
        if request.POST.get('movie') == None:
            pass
        else:
            movies = []
            movie = request.POST.get('movie')
            r = requests.get(f'https://yts.mx/api/v2/list_movies.json?query_term={movie}&sort_by=rating').json()
            i = 0
            for i in range(0, 20):
                try:
                    movie = Movie()
                    movie.name = json.dumps(r['data']['movies'][i]['title_long'], indent=2)
                    movie.imdb = json.dumps(r['data']['movies'][i]['imdb_code'], indent=2).strip("\"")
                    movie.summary = json.dumps(r['data']['movies'][i]['summary'], indent=2)
                    movie.year = json.dumps(r['data']['movies'][i]['year'], indent=2)
                    movie.m_hash = json.dumps(r['data']['movies'][i]['torrents'][0]['hash'], indent=2)
                    mh = movie.m_hash.strip(' \" ')
                    movie.m_hash = f"https://yts.mx/torrent/download/{mh}"
                    movie.rating = json.dumps(r['data']['movies'][i]['rating'], indent=2)
                    movies.append(movie)
                except IndexError or KeyError:
                    pass
            context = {
                'movies': movies,
                'title': 'Private Torrents',
            }
            return render(request, 'search/index.html', context)

            print(f"searching torrent: {request.POST.get('movie')}")
            request.POST.get('movie')
        
        if request.POST.get('movie_name') == None:
            pass
        else:
            print(request.POST.get('movie_name'))
            # os.system(f"qbittorrent-nox {request.POST.get('movie_name')} --save-path={os.environ('TOR')} --skip-dialog=true")
            return (render(request, 'search/success.html'))

    return render(request, 'search/index.html', {'title' : 'Private Torrentz'} )
