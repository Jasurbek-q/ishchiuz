from django.db import models

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