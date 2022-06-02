import requests
import urllib.parse
import json

def create_json(photos_list, count):
    result_json = {}
    result_list = []
    for photo in photos_list[0:count]:
        result_list.append({'file_name':str(photo[2])+'.jpg', 'size': photo[1] })
        result_json['photos'] = result_list
    with open('results.json', mode='w') as f:
        f.write(json.dumps(result_json, indent=4))

class YaDisk:
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    path_ya = ''
    def __init__(self, token: str):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'}
    def upload_photos(self, photos_list, count, user):
        url = self.url + 'upload?path='
        print(f'Начинаем загрузку файлов')
        for photo in photos_list[:count]:
            res = requests.post(url+urllib.parse.quote('BackUp/'+user+'/'+str(photo[2]))+'.jpg&url='+urllib.parse.quote(photo[0]), headers=self.headers)
            if res.status_code == 202:
                print(f'Файл {photo[2]}.jpg успешно загружен')
            else:
                print(f'Ошибка загрузки файла - {res.status_code}')
        create_json(photos_list,count)

    def create_folder_id(self,id_folder_name, folder_name = 'BackUp'):
        print('Создаем папку BackUp на диске')
        url = self.url + '?path=' +folder_name
        res = requests.put(url, headers=self.headers)
        if res.status_code == 201:
                print(f'Успешно')
        elif res.status_code == 409:
            print('Папка уже существует')
        else:
            print('Ошибка создания папки - ' + res.status_code)
        print('Создаем папку ' +id_folder_name+' на диске')

        url = self.url + '?path=' + urllib.parse.quote(folder_name+'/'+id_folder_name)
        res = requests.put(url, headers=self.headers)
        if res.status_code == 201:
                print(f'Успешно')
        elif res.status_code == 409:
            print('Папка уже существует')
        else:
            print('Ошибка создания папки - ' + res.status_code)
    def check_token(self):
        print('Проверяем ключ')
        url = 'https://cloud-api.yandex.net/v1/disk'
        res = requests.get(url, headers=self.headers).json()
        if 'user' in res:
            print('Успешная авторизация пользователя - '+ res['user']['login'])
        else:
            print('Неправильный ключ, ошибка - '+ res['error'])
            exit()

