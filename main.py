
from social import Vk_user
from drive import YaDisk

if __name__ == '__main__':
    user_id = input('Введите id или screen-name пользователя: ')
    Vk = Vk_user('a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd', '5.131')
    photos_list = Vk.get_photos_list(user_id)
    count_photos = int(input('Сколько фотографий сохранить?: '))
    ya_token = input('Введите ключ для Яндекс Диска: ')
    Ya = YaDisk(ya_token)
    Ya.check_token()
    Ya.create_folder_id(user_id)
    Ya.upload_photos(photos_list,count_photos,user_id)
