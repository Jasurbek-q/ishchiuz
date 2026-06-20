from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.hashers import make_password


class Foydalanuvchi(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225 , default='')

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

class Ishchi(models.Model):
    name        = models.CharField(max_length=100, verbose_name="Ism")
    surname     = models.CharField(max_length=100, verbose_name="Familiya")
    age         = models.IntegerField(verbose_name="Yosh")
    sohasi      = models.CharField(max_length=100, verbose_name="Sohasi")
    rasm        = models.ImageField(upload_to='rasmlar/', verbose_name="Rasm")
    description = models.TextField(verbose_name="O'zi haqida")
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Ishchi"
        verbose_name_plural = "Ishchilar"