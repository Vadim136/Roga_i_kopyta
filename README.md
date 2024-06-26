Реализованый магазин на Django c базой данных PostgreSql



Тестовое задание
	Необходимо реализовать на языке Python backend часть для интернет магазина «Рога и Копыта». У него существует около 100 позиций товаров. Пользователь должен иметь возможность посмотреть каталог товаров, добавить товар в корзину и купить его.
	Что обязательно должно быть сделано:
1. Спроектирована база данных, созданы необходимые модели и реализовано взаимодействие с ними через средства ORM. 
2. Создано API с эндпоинтами:
POST /products — получение продуктов по категории, 
GET /product — получение карточки конкретного продукта,
GET, POST, PUT, DELETE  /cart — для получения, добавления, изменения и удаления товаров в корзине, пользователь может получить только свою корзину,
POST /order— создание заказа. Заказ должен сохранится в бд. После вызова эндпоинта корзина должна быть очищена.
3. Приложение должно быть выложено в любое хранилище репозиториев. Предпочтительны: GitLab, GitHub.
Дополнительным плюсом будет:
- подключение сваггера/любого другого формата автодокументации;
- при получении продуктов иметь возможность фильтровать и сортировать по цене (не менее заданного значения и не более заданного значения).
- составить иерархию категорий и отдавать их в виде дерева, эндпоинт GET /categories, один товар может находится в нескольких категориях.
- покрыть юнит тестами основные эндпоинты
- настроить сборку приложения через docker контейнер
Рекомендуемый стек технологий:
•	Django
•	MySql / PostgreSql
•	PyUnit
•	Приветствуется использование других библиотек
