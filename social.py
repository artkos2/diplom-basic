import requests
import time


class Vk_user:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }
    def get_id(self, screen_name):
        name_url = self.url + 'users.get'
        name_params = {
            'user_ids': screen_name
        }
        res = requests.get(name_url, params={**self.params, **name_params}).json()
        return res['response'][0]['id']

    def get_photos_list(self, user_id):
        photos_list = []
        photos_url = self.url + 'photos.get'
        if user_id.isdigit():
            user_id = user_id
        else:
            user_id = Vk_user.get_id(self, user_id)

        frends_params = {
            'user_id': user_id,
            'album_id': 'profile',
            'extended': 'likes'
        }
        print('Ищем фотографии пользователя - id' + str(user_id))
        time.sleep(1)#чтобы было ощущение что что-то происходит :)
        res = requests.get(photos_url, params={**self.params, **frends_params}).json()
        for photo in res['response']['items']:
            photos_list.append([photo['sizes'][-1]['url'],photo['sizes'][-1]['type'],photo['likes']['count']])
            photos_list = sorted(photos_list, key=lambda x: x[1], reverse=True)
        print(f'Найдено фотографий - ' + str(res['response']['count']))
        return(photos_list)

class Insta_user():
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }

class Ok_user():
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }


