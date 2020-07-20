from requests import get
import json
import random
import os
from umafoto_ae.exceptions import ServiceNotFound, ReachingAPILimit


class PhotoHunter:
    """This class is responsable for taking the user request and return a image."""

    def __init__(self, user_request):
        print('Pedindo Foto ao PhotoHunter')
        self.query = user_request.GET.get('query', '')
        self.orientation = user_request.GET.get('orientation', 'all')
        self.color = user_request.GET.get('color', 'all')
        self.photo_info = {}
        self.provider = random.choice(list(ApiGetter.request_limit.keys()))

    def get_photo(self):
        try:
            ResponseProcesser().pick_photo(self)
            return self.photo_info
        except IndexError:
            return {'status': False}


class ResponseProcesser:
    """This class is responsable for interpreting and storing the API Response."""
    
    jsons_storage='./umafoto_ae/jsons/'

    def fill_photo_info(self, photo_form, ph: PhotoHunter):
        if ph.provider == 'unsplash':
            ph.photo_info['url'] = photo_form['urls']['regular']
            ph.photo_info['link'] = photo_form['links']['html']
            ph.photo_info['author_name'] = photo_form['user']['name']
            ph.photo_info['license'] = 'https://unsplash.com/license'
            ph.photo_info['provider'] = 'Unsplash'
            ph.photo_info['author_url'] = photo_form['user']['links']['html']
            ph.photo_info['provider_logo'] = 'unsplash.svg'
            ph.photo_info['status'] = True
        elif ph.provider == 'pixabay':
            ph.photo_info['url'] = photo_form['largeImageURL']
            ph.photo_info['link'] = photo_form['pageURL']
            ph.photo_info['author_name'] = photo_form['user']
            ph.photo_info['license'] = 'https://pixabay.com/service/license/'
            ph.photo_info['provider'] = 'Pixabay'
            ph.photo_info['author_url'] = f'https://pixabay.com/pt/users/{photo_form["user"]}'
            ph.photo_info['provider_logo'] = 'pixabay.svg'
            ph.photo_info['status'] = True

    def pick_random_photo(self, json_form, ph: PhotoHunter):
        photo_list = []
        if ph.provider == 'unsplash':
            photo_list = json_form['results']
        elif ph.provider == 'pixabay':
            photo_list = json_form['hits']

        return random.choice(photo_list)

    def pick_photo(self, ph: PhotoHunter):

        try:
            with open(f'{self.jsons_storage}{ph.provider}_{ph.query}_{ph.orientation}_{ph.color}.json', 'rt') as file:
                response = json.load(file)
                print('Entregando JSON armazenado')
        except FileNotFoundError:
            response = ApiGetter(ph).get_response()
            print('Entregando JSON novo')
            self.store_json(response, ph)
        
        
        print('Escolhendo Foto')
        photo = self.pick_random_photo(response, ph)
        self.fill_photo_info(photo, ph)

    def store_json(self, json_form, ph: PhotoHunter):
        with open(f'{self.jsons_storage}{ph.provider}_{ph.query}_{ph.orientation}_{ph.color}.json', 'at') as file:
            json.dump(json_form, file)

class ApiGetter:
    """This class is responsable for getting photos from the APIs."""

    request_limit = {
        'unsplash': 50,
        'pixabay': 5000
    }

    PER_PAGE = '&per_page=30'

    def __init__(self, ph: PhotoHunter):
        self.query = ph.query
        self.orientation = ph.orientation
        self.color = ph.color
        self.provider = ph.provider
        self.limit = self.request_limit[self.provider]

    def unsplash(self):
        print('Pedindo foto ao unsplash')
        orientations = {
            "horizontal": "landscape",
            "vertical": "portrait"}
        colors = {
            "grayscale": "black_and_white",
            "red": "red",
            "orange": "orange",
            "yellow": "yellow",
            "green": "green",
            "turquoise": "teal",
            "blue": "blue",
            "lilac": "purple",
            "pink": "magenta",
            "white": "white",
            "black": "black"}
        query = f'&query={self.query}' if self.query else '&query=photo'
        color = f'&color={colors[self.color]}' if self.color != 'all' else ''
        orientation = f'&orientation={orientations[self.orientation]}' if self.orientation != 'all' else ''
        api_request = ''.join(['https://api.unsplash.com/search/photos', os.environ.get(
            "UNSPLASH_KEY"), self.PER_PAGE, query, orientation, color])
        response = get(api_request)

        return self.prepare_response(response)

    def pixabay(self):
        print('Pedindo foto ao pixabay')
        query = f'&q={self.query}' if self.query else ''
        orientation = f'&orientation={self.orientation}'
        color = f'&colors={self.color}'
        api_request = ''.join(['https://pixabay.com/api/', os.environ.get(
            "PIXABAY_KEY"), self.PER_PAGE, query, orientation, color, '&image_type=photo'])
        response = get(api_request)

        return self.prepare_response(response)

    def prepare_response(self, response):
        if response.status_code != 200:
            raise ServiceNotFound('Resposta inesperada do servidor')
        else:
            self.request_limit[self.provider] = response.headers['X-RateLimit-Remaining']
            return json.loads(response.content)

    def get_response(self):
        if self.limit > 5:
            
            return eval(f'self.{self.provider}')()
        else:
            raise ReachingAPILimit('The API is near its limits.')


