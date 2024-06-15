from api import PetFriends
from settings import valid_email, valid_password,invalid_email,invalid_password
import os

pf = PetFriends()

def test_successfully_adding_new_pet_without_photo(name='Кузя', animal_type='наглый кот', age=2):
    """Проверяем возможность добвления питомца без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_successful_add_photo_of_pet_with_valid_data(pet_photo='images/Murzik.jpg'):
    """Проверяем возможность добавления фото к имеющемуся питомцу"""
    #Получаем ключ, получаем список своих питомцев, указываем полный путь к файлу с картинкой.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = my_pets['pets'][0]['id']
    #Проверяем -  список своих питомцев, если не пустой - добавляем фото питомцу:
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)
    #Проверяем список своих питомцев:
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
    else:
        raise Exception('У вас пока нет питомцев!')

def test_get_api_key_for_invalid_email_user(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 и в результате не содержится слово key"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert 'key' not in result

def test_get_api_key_for_invalid_password_user(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 и в результате не содержится слово key"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert 'key' not in result

def test_get_api_key_for_invalid_user(email=invalid_email, password=invalid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 и в результате не содержится слово key"""
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert 'key' not in result

def test_post_add_new_pet_no_name(name='', animal_type='сибирский кот', age=2, pet_photo='images/Cat.jpg'):
    """Проверяем что нельзя  добавить питомца с некорректными данными (оставляем пустым обязательное поле name)"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученные данные с ожидаемым результатом
    assert status != 200
    assert result['name'] != name

def test_post_add_new_pet_no_animal_type(name='Бусик', animal_type='', age=2, pet_photo='images/Cat.jpg'):
    """Проверяем что нельзя  добавить питомца с некорректными данными (оставляем пустым обязательное поле animal_type)"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key. Указываем путь к файлу с фото питомца.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Добавляем питомца
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученные данные с ожидаемым результатом
    assert status != 200
    assert result['animal_type'] != animal_type

def test_post_add_new_pet_no_age(name='Бусик', animal_type='cat', age='', pet_photo='images/Cat.jpg'):
    """Проверяем что нельзя  добавить питомца с некорректными данными (оставляем пустым обязательное поле age)"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key. Указываем путь к файлу с фото питомца.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    # Добавляем питомца
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученные данные с ожидаемым результатом
    assert status != 200
    assert result['age'] != age

def test_post_add_new_pet_invalid_photo(name='Sam', animal_type='cat', age='10', pet_photo='images/Sam.gif'):
    """Проверяем что нельзя  добавить питомца с некорректными данными (фото питомца отличное по формату от разрешённых: JPG, JPEG or PNG)"""
    # Запрашиваем ключ api и сохраняем в переменую auth_key. Указываем путь к файлу с фото питомца.
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    #Добавляем питомца
    status, result = pf.post_add_new_pet(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученные данные с ожидаемым результатом
    assert status != 200
    assert result['pet_photo'] != pet_photo

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=-5):
    """Проверяем невозможность замены на некорректные данные, информации о питомце. В запросе параметр age - отрицательное число. """

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['age'] != age
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("У вас нет питомцев!")











