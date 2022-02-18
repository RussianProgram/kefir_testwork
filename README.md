# Тестовое задание для Kefir

##Задачи:

:heavy_check_mark: 1) Аутентификация в сервисе происходит с помощью cookie.    
:heavy_check_mark: 2) Администраторы могут видеть все данные пользователей и изменять их.    
:heavy_check_mark: 3) Простые пользователи могут видеть лишь ограниченное число данных обо всех пользователях и редактировать часть своих данных.    

##Задачи по желанию

:heavy_check_mark: 1) Тесты (Мой первый опыт с тестами)    
:heavy_check_mark: 2) Документация    
:x: 3) Swagger    
:x: 4) Docker    

#HOW TO:
##Запуск на локальном сервере
###Клонируем
```
git clone https://github.com/RussianProgram/kefir_testwork.git
```
### Первоначальная установка 
```
cd kefir_testwork
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

#API DOCUMENTATION:
##API FOR USER:
###User list (Only GET)
```shell
curl http://localhost:8000/api/users
```
##Если юзер аутентифицирован
###User Update (GET, PUT)
```shell
curl http://localhost:8000/api/users/{int:pk}
```

##API FOR ADMIN:
###User list (GET)
```shell
curl http://localhost:8000/api/private/users/ -H "Authorization: Basic cm9vdDplZ28=" 
```
###User list (POST) создать юзера
```shell
curl -X POST http://localhost:8000/api/private/users/ -H "Authorization: Basic someid" -H "Content-Type: application/json" -d '{somedata}'
```
###User Detail (GET)
```shell
curl http://localhost:8000/api/private/users/{int:pk} -H "Authorization: Basic someid" 
```
###User Detail (PUT) Изменить данные юзера
```shell
curl -X PUT http://localhost:8000/api/private/users/{int:pk} -H "Authorization: Basic someid" -H "Content-Type: application/json" -d '{somedata}'
```
###User Detail (DELETE) Удалить юзера
```shell
curl -X DELETE http://localhost:8000/api/private/users/{int:pk} -H "Authorization: Basic someid" 
```
### Плюс всё из API FOR USER/


