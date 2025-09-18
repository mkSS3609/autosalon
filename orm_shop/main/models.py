from django.db.models import *


class Client(Model):
    name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    middle_name = CharField(max_length=50)
    date_of_birth = DateField()
    phone_number = CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(Model):
    id = AutoField(primary_key=True)
    model = CharField(max_length=50)
    year = IntegerField()
    color = CharField(max_length=50)
    mileage = IntegerField()
    volume = DecimalField(decimal_places=1, max_digits=5)
    body_type = CharField(max_length=50, choices=BODY_TYPE_CHOICES)
    drive_unit = CharField(max_length=50, choices=DRIVE_UNIT_CHOICES)
    gearbox = CharField(max_length=50, choices=GEARBOX_CHOICES)
    fuel_type = CharField(max_length=50, choices=FUEL_TYPE_CHOICES)
    price = IntegerField()
    image = ImageField(upload_to='images/')

class Sale(Model):
    id = AutoField(primary_key=True)
    client = ForeignKey(Client, on_delete=PROTECT)
    car = ForeignKey(Car, on_delete=PROTECT)
    created_at = DateField(auto_now_add=True)
