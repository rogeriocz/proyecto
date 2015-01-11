from django.db import models
from django.template.defaultfilters import slugify

from django.conf import settings

class Fecha_Materia(models.Model):

	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Categoria(models.Model):

	name = models.CharField(max_length=100)
	slug = models.SlugField(editable=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Categoria, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

class Materias(Fecha_Materia):

	name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(editable=False)
	summary = models.TextField(max_length=255)
	content = models.TextField()
	categoria = models.ForeignKey(Categoria)
	place = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to = 'materia')
	is_free = models.BooleanField(default=True)
	amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	views = models.PositiveIntegerField(default=0)
	organizer = models.ForeignKey(settings.AUTH_USER_MODEL)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Materias, self).save(*args, **kwargs)
	def __unicode__(self):
		return self.name

class Assistant(Fecha_Materia):
	assistant = models.ForeignKey(settings.AUTH_USER_MODEL) 
	event = models.ManyToManyField(Materias)

	attended = models.BooleanField(default = False)
	has_pain = models.BooleanField(default = False)

	def __unicode__(self):
		return "%S %S" % (self.assistant.username , self.event.name)

class Comments(Fecha_Materia):

	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	event = models.ForeignKey(Materias)

	content = models.TextField()

	def __unicode__(self):
		return "%S %S" % (self.user.username, self.even.name)

class Semestre(Fecha_Materia):
	name = models.CharField(max_length=50)
	mater = models.ForeignKey(Materias)
	
	def __unicode__(self):
		return self.name

class Carrera(Fecha_Materia):

	nombre = models.TextField(max_length=100)
	mat = models.ForeignKey(Materias)

	def __unicode__(self):
		return self.nombre