from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)


    def __str__(self):
        return "%s %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'a lot of subscribers'

