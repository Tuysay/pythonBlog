from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField("Заголовок записи", max_length=100)
    description = models.TextField("Текскт записи")
    author = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата")
    img = models.ImageField(" Фотка", upload_to='files')

    def __str__(self):
        return f'{self.title}, {self.author}'



    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"



class Commit(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=60)
    text = models.TextField("Текст", max_length=1500)
    post = models.ForeignKey(Post, verbose_name="Публикации", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'



    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
