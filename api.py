import requests
import json

class PetFriends():
    """апи библиотека к веб приложению Pet Friends"""
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self,email,password):
        """ Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON с уникальным ключом пользователя,
        найденного по указанным email  и паролем"""

        headers = {
            'email':email,
            'password':password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status,result

    def get_list_of_pets(self, auth_key, filter):
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком питомцев, совпадающих с фильтром.
        На данный момент фильтр может иметь либо пустое значение - получить список всех питомцев, либо 'my_pets'- получить список собственных питомцев."""
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url + 'api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result

    def post_add_new_pet(self,auth_key,name,animal_type,age,pet_photo):
        """Метод делает запрос к API сервера и отправляет данные в теле запроса, возвращает статус запроса
        и результат в формате JSON с данными добавленного питомца."""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo':(pet_photo, open(pet_photo,'rb'),'images/jpeg')}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key:json,pet_id: str):
        """Метод удаляет питомца с указанным id и возвращает статус запроса и ответ в формате JSON об успешном удалении """
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + 'api/pet/' + pet_id,headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text

        return status, result








