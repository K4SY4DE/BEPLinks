from django.db import models



# Create your models here.


class Tema(models.Model):
    titulo = models.CharField(max_length=100)
    resumo = models.TextField()

    def __str__(self):
        return self.titulo


class Recurso(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='recursos')
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    tipo = models.CharField(max_length=100)
    url = models.URLField()
    data_catalogacao = models.DateTimeField(auto_now_add=True)
    gratuito = models.BooleanField(default=True)
    prestigio = models.IntegerField(default=0)

    def __str__(self):
        return self.nome