from django.db import models

#create a blog models
#title
#pub_date
#body(text)
#image

#Add the blog app to settings
#create a migration
#migrate
#Add to the admin


class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %y')

