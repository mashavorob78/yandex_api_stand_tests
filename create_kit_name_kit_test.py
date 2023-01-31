import sender_stand_request
import data

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def positive_assert(name):
    # В переменную name сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def negative_assert(name):
    # В переменную name сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400


def negative_assert_no_name(kit_body):
    auth_token = get_new_user_token()
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400


def test_create_kit_1_letter_name_get_success_response():
    positive_assert("a")

def test_create_kit_511_letter_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_0_letter_name_get_error_response():
    negative_assert("")

def test_create_kit_512_letter_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_english_letter_name_get_success_response():
    positive_assert("QWErty")

def test_create_kit_rus_letter_name_get_success_response():
    positive_assert("Мария")

def test_create_kit_symbol_letter_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_kit_space_letter_name_get_success_response():
    positive_assert("Человек и КО")

def test_create_kit_digit_letter_name_get_success_response():
    positive_assert("123")

def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)

def test_create_kit_type_digit_letter_name_get_error_response():
    negative_assert(123)


