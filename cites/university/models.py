from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Customer", on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.id})

    class Meta:
        ordering = ['-id']

class Customer(models.Model):
    name = models.CharField(max_length=400, verbose_name="name")
    title = models.TextField()
    url_name = models.URLField(max_length=500, verbose_name="Url name")
    image = models.ImageField(upload_to='image', verbose_name='rasm')
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} || {self.title}'


    def get_absolute_url(self):
        return "/"  + str(self.id)  + "/"

    class Meta:
        ordering = ['-id']




class Users(models.Model):
    id=models.IntegerField(primary_key=True)
    email=models.CharField(max_length=200, blank=False, null=False)
    name=models.CharField(max_length=200, blank=False, null=False)
    number = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField()


    def __str__(self):
        return f"{self.id} || {self.name} || {self.email} "

    class Meta:
        ordering = ['-id']