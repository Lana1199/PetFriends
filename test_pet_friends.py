import requests

from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email,password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result

    status,result = pf.get_api_key(email,password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
        Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
        запрашиваем список всех питомцев и проверяем что список не пустой.
        Доступное значение параметра filter - 'my_pets' либо '' """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status,result = pf.get_list_of_pets(auth_key,filter)
    assert status == 200
    assert len(result['pets']) > 0

# def test_add_photo(pet_photo='images/Cat.jpg'):
#     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
#     status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
#     assert status == 200
#     assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']

def test_post_add_new_pet_with_valid_data(name ='Барсик',animal_type= 'сибирский кот',age= '2', pet_photo= 'images/Cat.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status,result = pf.post_add_new_pet(auth_key,name,animal_type,age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_delete_pets_with_valid_id():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key,'my_pets')

    # Проверяем - если список своих питомцев пустой,то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.post_add_new_pet(auth_key,'Lord','cat',
                            '3', 'images/Lord.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key,'my_pets')

        # Берём id первого питомца из списка и отправляем запрос на удаление

    pet_id = my_pets['pets'][0]['id']
    status,_ = pf.delete_pet(auth_key,pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key,
                                     "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()












