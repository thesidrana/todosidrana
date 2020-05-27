from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here. Database created here as classes. Each class is one table.

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_on = models.DateField(default = timezone.now ) #Function is passed on as def value
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) # Returns full path as a string



#Use of Cascade : If a user is deleted, all of their posts will be deleted.
                # But, if a post is deleted, user will not be deleted.

#There is a one to many rel. between Author and Post
#An author can write many posts but
#one post can only have one author


#View SQL Code: python manage.py sqlmigrate 'app_name' 'migration_number'
