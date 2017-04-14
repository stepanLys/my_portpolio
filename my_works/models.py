from django.db import models


class Work(models.Model):
    name = models.CharField(max_length=50)
    # img = models.ImageField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Робота: %s " % (self.name)

    class Meta:
        verbose_name = 'Робота'
        verbose_name_plural = 'Мої роботи'

    def save(self, *args, **kwargs):
        super(Work, self).save(*args, **kwargs)


class WorkImage(models.Model):
    product = models.ForeignKey(Work, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='works_photo/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотографія'
        verbose_name_plural = 'Фотографії'