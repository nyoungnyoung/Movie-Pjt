import requests
import json

API_KEY = '487b617acdcef17f4628cd13e62a835c'
def get_json_movies():
    result = []
    for page in range(1,30):
        URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko&page={page}'
        data = requests.get(URL).json()['results']
        movies=[]
        for movie in data:
            fields = {
                'tmdb_id' : movie['id'],
                'title' : movie['title'],
                'overview' : movie['overview'],
                'genres' : movie['genre_ids'],
                'language' : movie['original_language'],
                'poster_path' : movie['poster_path'],
                'popularity' : movie['popularity'],
                'vote_average' : movie['vote_average'],
                'release_date' : movie['release_date'],
                'adult' : movie['adult'],
            }
            if fields['release_date']!="" and fields['adult']==False:
                for c in ['형수','여친','딸','엄마']:
                    if c in fields['title']:
                        break
                    else:
                        temp = {
                            'model' : 'movies.movie',
                            'fields' : fields,
                        }
                        if temp not in movies:
                            movies.append(temp)
        result += movies
    with open('data/movies.json','w', encoding='utf=8') as file :
        json.dump(result,file,ensure_ascii=False, indent = '\t')
get_json_movies()

def get_json_genres():
    URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'
    data = requests.get(URL).json()['genres']
    genres = []
    for genre in data :
        temp = {
            'model' : 'movies.genre',
            'fields': genre,
        }
        genres.append(temp)
    with open('data/genres.json', 'w', encoding='utf-8') as file:
        json.dump(genres, file, ensure_ascii=False, indent='\t')
get_json_genres()
