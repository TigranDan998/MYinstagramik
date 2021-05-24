from django.db import models
class Articles(models.Model):

    title = models.CharField('Название', max_length=50, default = 'Новость')

    anons = models.CharField('Анонс', max_length=250)

    full_text = models.TextField('Статья')

    date = models.DateTimeField('Дата публикации')

    image = models.ImageField(upload_to='media', default='Изображение')

    def get_absolute_url(self):
        return f'/mainnews/{self.id}'

# Create your models here.
