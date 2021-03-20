from django.db import models


class ServiceCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    service = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='clients')
    notice = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    title = models.CharField(max_length=255)
    service = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='orders')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    total_cost = models.DecimalField(decimal_places=2, max_digits=10)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    notice = models.TextField(null=True, blank=True)
    site_url = models.CharField(max_length=255, null=True, blank=True)
    git_url = models.CharField(null=True, blank=True, max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    payment_sum = models.DecimalField(max_digits=10, decimal_places=2)
    notice = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.payment_sum} - {self.date}'


class Task(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=255)
    text = models.TextField()
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Key(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    login = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    field_1 = models.CharField(null=True, blank=True, max_length=255)
    field_2 = models.CharField(null=True, blank=True, max_length=255)
    notice = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






