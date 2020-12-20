from django.shortcuts import render
import requests
import json
import argparse
import os

movies = []

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

name = "clouds" ## Allow user to pass string (title) parameter

r = requests.get(f'https://yts.mx/api/v2/list_movies.json?query_term={name}&sort_by=rating').json()
i = 0
for i in range(0, 20):
    try:
        movie = Movie()
        movie.name = json.dumps(r['data']['movies'][i]['title_long'], indent=2)
        movie.year = json.dumps(r['data']['movies'][i]['year'], indent=2)
        movie.m_hash = json.dumps(r['data']['movies'][i]['torrents'][0]['hash'], indent=2)
        mh = movie.m_hash.strip(' \" ')
        movie.m_hash = f"https://yts.mx/torrent/download/{mh}"
        movie.rating = json.dumps(r['data']['movies'][i]['rating'], indent=2)
        movies.append(movie)
    except IndexError:
        pass

def home(request):
    if request.POST == '':
        pass
    else:
        os.system(f"qbittorrent-nox {request.POST.get('movie_name')} --save-path=/home/tree/Documents/plex/movies/ --skip-dialog=true")
    context = {
        'movies': movies,
        'title': 'Private Torrents',
    }
    return render(request, 'search/index.html', context)
