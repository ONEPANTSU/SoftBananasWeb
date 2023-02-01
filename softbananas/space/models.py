from django.db import models


# Create your models here.

class Category(models.Model):
    category = models.TextField(max_length=30)


class Client(models.Model):
    name = models.TextField(max_length=25)
    mail = models.TextField(max_length=45)
    connection = models.TextField(max_length=100)


class Dialog(models.Model):
    start_date = models.DateTimeField(auto_now=True)


class Draft(models.Model):
    user_id = models.IntegerField
    text = models.TextField(max_length=150)
    finale_order_id = models.IntegerField()
    date = models.DateTimeField(auto_now=True)


class Draft_file(models.Model):
    file_id = models.IntegerField()
    draft_id = models.IntegerField()


class File(models.Model):
    link = models.FileField()


class Final_order(models.Model):
    name = models.TextField(max_length=25)
    deadline = models.DateTimeField(auto_now=True)
    status_id = models.IntegerField()


class Massege(models.Model):
    to_from_admin = models.IntegerField
    text = models.TextField(max_length=1500)
    is_read = models.IntegerField()
    date = models.DateTimeField(auto_now=True)


class Order_category(models.Model):
    order_id = models.IntegerField()
    category_id = models.IntegerField()


class Order_file(models.Model):
    file_id = models.IntegerField()
    order_id = models.IntegerField()


class Order_request(models.Model):
    description = models.TextField(blank=True, max_length=1000)
    client_id = models.IntegerField()
    budget = models.IntegerField()


class Projects(models.Model):
    name = models.TextField(max_length=70)
    text = models.TextField(max_length=10000)
    photo_id = models.IntegerField()
    link = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now=True)


class Role(models.Model):
    role = models.TextField(max_length=25)


class Status(models.Model):
    status = models.TextField(max_length=15)


class User(models.Model):
    username = models.TextField(max_length=30)
    password = models.TextField(max_length=30)
    mail = models.TextField(max_length=40)
    name = models.TextField(max_length=25)
    surname = models.TextField(max_length=25)
    photo_id = models.IntegerField()


class User_role(models.Model):
    user_id = models.IntegerField()
    role_id = models.IntegerField()