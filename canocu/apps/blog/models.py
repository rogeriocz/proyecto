from django.db import models
from django.conf import settings

class EntradaQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publicado=True)

class Entrada(models.Model):

	titulo = models.CharField(max_length=300)
	imagen = models.ImageField(upload_to = 'bloger')
	contenido = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	publicado = models.BooleanField(default=True)
	creado = models.DateField(auto_now_add=True)
	modificado = models.DateField(auto_now=True)
	creador = models.ForeignKey(settings.AUTH_USER_MODEL)



	object = EntradaQuerySet.as_manager()

	def __unipad__(self):
		return self.titulo


	class Meta:
		verbose_name='Blog Entrada'
		verbose_name_plural ='Blog Entradas'
		ordering = ["-creado"]