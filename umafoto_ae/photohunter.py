import requests, json, random, os
from datetime import datetime
from umafoto_ae.exceptions import ServiceNotFound


class ApiGetter:
    #Unsplash API
    unsplash_api = 'https://api.unsplash.com/'
    unsplash_key = os.environ.get("UNSPLASH_API")
    unsplash_limit = 50

    #Pixabay API
    pixabay_api = 'https://pixabay.com/api/'
    pixabay_key = os.environ.get("PIXABAY_API")
    pixabay_limit = 5000


    #Configurações da busca
    per_page = 30
    services = ['unsplash', 'pixabay']


    #Define dicionátio a ser passado para o views
    photo_info = {}

    def get_photo(self, tag, orientation, color):
        #Define limites de cada serviço de fotos
        unsplash = self.unsplash_limit
        pixabay = self.pixabay_limit

        while True:
            sel = random.choice(self.services)
            if eval(sel) > 10: 
                try:
                    self.pick_photo(sel, tag, orientation, color)
                    return self.photo_info
                except IndexError:
                    return {'status':False}

    def request_unsplash(self, tag, orientation, color):
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
            "turquoise":"teal",
            "blue": "blue",
            "lilac": "purple",
            "pink": "magenta",
            "white": "white",
            "black":"black"}
        tag = f'&query={tag}' if tag else f'&query=photo'
        orientation = f'&orientation={orientations[orientation]}' if orientation != 'all' else ''
        color = f'&color={colors[color]}' if color != 'all' else ''
        request = self.unsplash_api + 'search/photos' + self.unsplash_key + f'&per_page={self.per_page}' + tag + orientation + color
        response = requests.get(request)
        if response.status_code != 200:
            raise ServiceNotFound('Resposta inesperada do servidor')
        else:
            self.unsplash_limit = response.headers['X-RateLimit-Remaining']
            return json.loads(response.content)
            

    def request_pixabay(self, tag,  orientation, color):
        print('Pedindo foto ao pixabay')
        tag = f'&q={tag}' if tag else ''
        orientation = f'&orientation={orientation}'
        color = f'&colors={color}'
        request = self.pixabay_api + self.pixabay_key + f'&per_page={self.per_page}' + tag + orientation + color + '&image_type=photo'
        response = requests.get(request)

        if response.status_code != 200:
            raise ServiceNotFound('Resposta inesperada do servidor')
        else:
            self.pixabay_limit = response.headers['X-RateLimit-Remaining']
            return json.loads(response.content)
            

    def fill_photo_info(self, photo_form, api_provider):
        if api_provider == 'unsplash':
            self.photo_info['url'] = photo_form['urls']['regular']
            self.photo_info['link'] = photo_form['links']['html']
            self.photo_info['author_name'] = photo_form['user']['name']
            self.photo_info['license'] = 'https://unsplash.com/license'
            self.photo_info['provider'] = 'Unsplash'
            self.photo_info['author_url'] = photo_form['user']['links']['html']
            self.photo_info['provider_logo'] = '/static/assets/img/unsplash.svg'
            self.photo_info['status'] = True
        elif api_provider == 'pixabay':
            self.photo_info['url'] = photo_form['largeImageURL']
            self.photo_info['link'] = photo_form['pageURL']
            self.photo_info['author_name'] = photo_form['user']
            self.photo_info['license'] = 'https://pixabay.com/service/license/'
            self.photo_info['provider'] = 'Pixabay'
            self.photo_info['author_url'] = f'https://pixabay.com/pt/users/{photo_form["user"]}'
            self.photo_info['provider_logo'] = '/static/assets/img/pixabay.svg'
            self.photo_info['status'] = True
            


    def pick_random(self, json_form, api_provider):
        photo_list = []
        if api_provider == 'unsplash':
            photo_list = json_form['results']
        elif api_provider == 'pixabay':
            photo_list = json_form['hits']
        
        return random.choice(photo_list)
    
    def pick_photo(self, api_provider, tag, orientation, color):
        unsplash = self.request_unsplash
        pixabay = self.request_pixabay

        try:
            with open(f'./umafoto_ae/jsons/{api_provider}_{tag}_{orientation}_{color}.json', 'rt') as file:
                response = json.load(file)
                print('Entregando JSON armazenado')
        except FileNotFoundError:
            response = eval(api_provider)(tag, orientation, color)
            print('Entregando JSON novo')
            self.store_json(response,api_provider, tag, orientation, color)
        finally:
            print('Escolhendo Foto')
            photo = self.pick_random(response, api_provider)
            self.fill_photo_info(photo, api_provider)
            


    def store_json(self, json_form, api_provider, tag, orientation, color):
        with open(f'./umafoto_ae/jsons/{api_provider}_{tag}_{orientation}_{color}.json', 'at') as file:
            json.dump(json_form, file)
        
        
#https://pixabay.com/api/?key=16987749-8d411cadaab71f440da579ff0&q=AOSGBASÇFLGJASPFGNAS&image_type=photo