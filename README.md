## Проект Тестирования API Stellar Burgers

Этот проект предназначен для автоматизированного тестирования API сервиса Stellar Burgers. 
Тесты написаны с использованием Pytest и Allure для отчетности.

### Установите необходимые зависимости:
pip install -r requirements.txt

### Запуск тестов
Для запуска тестов с генерацией отчета о покрытии и Allure отчетов выполните следующие команды:

Запуск тестов с генерацией Allure отчетов:
pytest --alluredir=allure-results

Генерация и просмотр Allure отчета:
allure serve allure-results


### Структура проекта
data.py - содержит базовые URL и конечные точки API.

conftest.py - фикстуры для тестов, включая создание и аутентификацию пользователя.

test_auth.py - тесты для проверки регистрации и авторизации.

test_orders.py - тесты для проверки операций с заказами.

test_user.py - тесты для проверки операций с пользователем.
