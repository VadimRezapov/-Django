from django.db import models


class Client(models.Model):
    name = models.TextField(max_length=20)
    mail = models.EmailField()
    phone = models.TextField(max_length=12)
    address = models.TextField(max_length=50)
    reg_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.phone}"


class Product(models.Model):
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.price}"

    def __eq__(self, other):
        return self.creation_date == other.creation_date

    def __gt__(self, other):
        return self.creation_date > other.creation_date

    def __lt__(self, other):
        return self.creation_date < other.creation_date

    def __ge__(self, other):
        return self.creation_date >= other.creation_date

    def __le__(self, other):
        return self.creation_date <= other.creation_date

    @property
    def full_info(self):
        return f'{self.title}, {self.description}, {self.price}, {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="order")
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer}, {self.products}"