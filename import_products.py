import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dancemotion.settings")
django.setup()

from shop.models import Category, Product

PRODUCTS = [
    {"id":1, "title":"Туфли Рейтинг с ремешками - Белые (Кожа)", "price":350000, "category":"Девочкам", "discount":0, "isNew":True, "img":"w3.jpg"},
    {"id":2, "title":"Туфли Рейтинг с ремешками - Светло-Бежевые (Сатин)", "price":350000, "category":"Девочкам", "discount":0, "isNew":True, "img":"B2.jpg"},
    {"id":3, "title":"Туфли Рейтинг с ремешками - Коричневые (Кожа)", "price":350000, "category":"Девочкам", "discount":0, "isNew":False, "img":"B.jpg"},
    {"id":4, "title":"Туфли Рейтинг с ремешками - Красные (Кожа)", "price":350000, "category":"Девочкам", "discount":0, "isNew":True, "img":"R.jpg"},
    {"id":5, "title":"Туфли Рейтинг с ремешками - Черные (Сатин)", "price":350000, "category":"Девочкам", "discount":0, "isNew":True, "img":"BL.jpg"},
    {"id":6, "title":"Туфли Рейтинг с ремешками - Коричневые (Сатин)", "price":350000, "category":"Девочкам", "discount":10, "isNew":True, "img":"BR.jpg"},
    {"id":7, "title":"Согревающие Чуни (Серые)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"S.png"},
    {"id":8, "title":"Согревающие Чуни (Небесно-голубой)", "price":250000, "category":"Женщинам", "discount":0, "isNew":True, "img":"BCH.png"},
    {"id":9, "title":"Согревающие Чуни (Темно-Фиолетовые)", "price":250000, "category":"Женщинам", "discount":0, "isNew":True, "img":"FCH.PNG"},
    {"id":10, "title":"Согревающие Чуни (Черные)", "price":250000, "category":"Женщинам", "discount":0, "isNew":True, "img":"BLCH.PNG"},
    {"id":11, "title":"Согревающие Чуни (Градиент)", "price":250000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GCH.PNG"},
    {"id":12, "title":"Согревающие Чуни (Розовые)", "price":250000, "category":"Женщинам", "discount":0, "isNew":True, "img":"PCH.png"},
    {"id":13, "title":"Стандартные туфли - (Шампань)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"SHST.PNG"},
    {"id":14, "title":"Стандартные туфли - (Белые)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"WHST.PNG"},
    {"id":15, "title":"Стандартные туфли - (Сатин)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"SST.PNG"},
    {"id":16, "title":"Латинские туфли - (Светло-Бежевые)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GLT.PNG"},
    {"id":17, "title":"Латинские туфли - (Черные)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"BLT.PNG"},
    {"id":18, "title":"Латинские туфли - (Сатин)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"SLT.PNG"},
    {"id":19, "title":"Латинские туфли - (Шампань)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"SHLT.PNG"},
    {"id":20, "title":"Латинские туфли - (Градиент)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GRLT.PNG"},
    {"id":21, "title":"Тренировочные туфли (Золотые Поцелуи)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GT.PNG"},
    {"id":22, "title":"Тренировочные туфли (Красные Поцелуи)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"RT.PNG"},
    {"id":23, "title":"Тренировочные туфли (Градиентовые Поцелуи)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GRT.PNG"},
    {"id":24, "title":"Туфли Рейтинг - (Сатин)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"SR.PNG"},
    {"id":25, "title":"Туфли Рейтинг - (Белые)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"WHR.PNG"},
    {"id":26, "title":"Туфли Рейтинг - (Черные)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"BRT.PNG"},
    {"id":27, "title":"Туфли Рейтинг плетение - (Персиковые)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"PR.PNG"},
    {"id":28, "title":"Туфли Рейтинг плетение - (Белые)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"WHRT.PNG"},
    {"id":29, "title":"Туфли Рейтинг - (Черные)", "price":350000, "category":"Женщинам", "discount":0, "isNew":True, "img":"BLRT.PNG"},
    {"id":30, "title":"Гетры - (Черные)", "price":120000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GET.PNG"},
    {"id":31, "title":"Гетры - (Белые)", "price":120000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GETWH.PNG"},
    {"id":32, "title":"Гетры - (Фирменный цвет DanceMotion)", "price":120000, "category":"Женщинам", "discount":0, "isNew":True, "img":"GETB.PNG"},
]

for item in PRODUCTS:

    cat_name = item["category"]

    category, _ = Category.objects.get_or_create(
        name=cat_name,
        slug=cat_name.lower()
    )

    product = Product.objects.create(
        category=category,
        title=item["title"],
        price=item["price"],
        discount=item["discount"],
        is_new=item["isNew"],
        image=f"products/{item['img']}"
    )

    print(f"Добавлен товар: {product.title}")

print("\nИмпорт завершён успешно!")
