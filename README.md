# Тестовое для Hubnero
###### https://hh.ru/vacancy/107472518

```text
Необходимо создать базовый Django проект, который при вызове "/get-current-usd/" будет возвращать актуальный курс 
доллара к рублю в формате JSON и 10 последних запросов курсов. Для получения курса используйте внешнее API (выберите 
подходящее самостоятельно). Между каждым запросом курса должна быть пауза не менее 10 секунд. 

1. Разбить на подзадачи 
2. Реализовать на Django 
3. Подготовить блок вопросов, которые бы ты задал: 
 - продакт менеджеру 
 - TL 
4. Подготовить тайминги по компонентам: 
 - первичная оценка 
 - фактическое время выполнения.
```
1. Подзадачи:
   1. Создание базового Django проекта:
      - Инициализация проекта.
      - Настройка приложения, создание моделей, миграции.
      
   2. Подключение к внешнему API для получения курса доллара:
      - Найти API для получения курса (например, free.currconv.com, openexchangerates.org, или другой подходящий сервис).
      - Реализовать функцию запроса курса с API.

   3. Создание представления /get-current-usd/:
      - Настроить URL для маршрута.
      - Реализовать обработчик, который делает запрос к API и возвращает данные в формате JSON.
      
   4. Реализация хранения 10 последних запросов:
      - Создать модель для хранения истории запросов.
      - Реализовать логику сохранения и извлечения последних 10 запросов из базы данных.
      
   5. Обеспечение задержки между запросами:
      - Добавить логику с использованием Python или Django (например, time.sleep(10) для задержки).
      
   6. Тестирование:
      - Убедиться, что приложение корректно обрабатывает запросы и правильно отображает данные.
      
2. currency_project http://127.0.0.1:8000/get-current-usd/
3. Блок вопросов:
   - Вопросы для продакт-менеджера:
     1. С какой периодичностью планируется обновление данных в реальном проекте?
     2. Есть ли ограничения по времени ответа от внешнего API?
     3. Каковы требования к мониторингу и логированию ошибок?
  
   - Вопросы для Team Lead:
     1. Какой подход вы используете для работы с внешними API в продакшене (например, повторные попытки, кэширование)? 
     2. Какие принципы обработки ошибок и логирования приняты в проекте? 
     3. Какие библиотеки и инструменты для тестирования предпочитаются в команде?

4. Тайминги:
   - Первичная оценка
     - Инициализация проекта: 30 минут. 
     - Подключение к API: 1 час. 
     - Реализация модели и маршрутов: 1.5 часа. 
     - Добавление задержки и тестирование: 1 час. 
     - Вопросы и документация: 30 минут.
   - Фактическое время будет зависеть от сложности подключения к API и возможных проблем при разработке.


### Дополнительные пояснения к проекту:
- Использование библиотеки python-decouple 
  - В файле settings.py используется библиотека python-decouple (или аналогичная) для отделения чувствительных данных, таких как SECRET_KEY, из кода проекта. Это делается с помощью строки:
    ```python
    SECRET_KEY = config('SECRET_KEY')
    ```
  - Зачем это нужно? Это отделяет секретные данные из кода и хранит их в отдельном файле, который не попадает в систему контроля версий (например, Git). Это помогает предотвратить утечку ключей безопасности и других конфиденциальных данных.
- В файле admin.py модель CurrencyRequest зарегистрирована с кастомизацией отображения что даёт возможность фильтрации, поиска и отображения полей.
- Пример ответа http://127.0.0.1:8000/get-current-usd/ в формате JSON:
```json
{
  "current_usd_to_rub": 96.94,
  "last_10_requests": [
    {
      "id": 12,
      "timestamp": "2024-10-11T10:19:14.190Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 11,
      "timestamp": "2024-10-11T10:18:57.238Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 10,
      "timestamp": "2024-10-11T10:18:44.236Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 9,
      "timestamp": "2024-10-11T10:18:31.802Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 8,
      "timestamp": "2024-10-11T10:18:19.561Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 7,
      "timestamp": "2024-10-11T10:18:05.912Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 6,
      "timestamp": "2024-10-11T09:37:15.967Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 5,
      "timestamp": "2024-10-11T09:35:57.843Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 4,
      "timestamp": "2024-10-11T09:34:13.748Z",
      "usd_to_rub": 96.94
    },
    {
      "id": 3,
      "timestamp": "2024-10-11T09:33:39.378Z",
      "usd_to_rub": 96.94
    }
  ]
}
```