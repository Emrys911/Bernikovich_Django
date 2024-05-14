from .models import Person, Hotel

# Создаем отели
hotels_data = [
    {"name": "Отель А", "stars": 5, "address": "Адрес 1", "city": "Город A", "phone": "111-111"},
    {"name": "Отель Б", "stars": 4, "address": "Адрес 2", "city": "Город B", "phone": "222-222"},
    {"name": "Отель В", "stars": 3, "address": "Адрес 3", "city": "Город C", "phone": "333-333"},
    {"name": "Отель Г", "stars": 5, "address": "Адрес 4", "city": "Город D", "phone": "444-444"},
    {"name": "Отель Д", "stars": 2, "address": "Адрес 5", "city": "Город E", "phone": "555-555"},
    {"name": "Отель Е", "stars": 4, "address": "Адрес 6", "city": "Город F", "phone": "666-666"},
    {"name": "Отель Ж", "stars": 3, "address": "Адрес 7", "city": "Город G", "phone": "777-777"},
    {"name": "Отель З", "stars": 5, "address": "Адрес 8", "city": "Город H", "phone": "888-888"},
    {"name": "Отель И", "stars": 2, "address": "Адрес 9", "city": "Город I", "phone": "999-999"},
    {"name": "Отель К", "stars": 4, "address": "Адрес 10", "city": "Город J", "phone": "000-000"},
]

# Добавляем отели в базу данных
for data in hotels_data:
    hotel = Hotel.objects.create(**data)

# Создаем пользователей
persons_data = [
    {"name": "Петр", "age": 25},
    {"name": "Иван", "age": 35},
    {"name": "Мария", "age": 45},
    {"name": "Анна", "age": 55},
    {"name": "Алексей", "age": 30},
    {"name": "Елена", "age": 40},
    {"name": "Сергей", "age": 50},
    {"name": "Ольга", "age": 20},
    {"name": "Дмитрий", "age": 60},
    {"name": "Наталья", "age": 65},
]

# Добавляем пользователей в базу данных
for data in persons_data:
    person = Person.objects.create(**data)

# Выводим всех пользователей сайта
all_users = Person.objects.all()
for user in all_users:
    print(user.name, user.age)

# Выводим отели с более чем 3 звёздами
high_rated_hotels = Hotel.objects.filter(stars__gt=3)
for hotel in high_rated_hotels:
    print(hotel.name, hotel.stars)

# Находим пользователей старше 40 лет и имя которых начинается с "P"
selected_users = Person.objects.filter(age__gt=40, name__startswith='P')
for user in selected_users:
    print(user.name, user.age)

# Находим всех пользователей с именем "Nick" или "Suzan"
selected_users = Person.objects.filter(name__in=["Nick", "Suzan"])
for user in selected_users:
    print(user.name, user.age)

# Выводим первых 5 самых младших людей на сайте
youngest_people = Person.objects.order_by('age')[:5]
for person in youngest_people:
    print()
