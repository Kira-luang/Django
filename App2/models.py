from django.db import models
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    age = models.IntegerField(default=1)
    id = models.ForeignKey('Class', on_delete=models.CASCADE, related_name='test')
    objects = models.Manager()


class Class(models.Model):
    class_id = models.IntegerField(primary_key=True, auto_created=True)
    item = models.CharField(max_length=255, null=False)

    @classmethod
    def add_class(cls, class_id=4, item='地理'):
        return cls(class_id=class_id, item=item)


class Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(girl__gt=10)


class Company(models.Model):
    company = models.CharField(max_length=18, primary_key=True)
    boy = models.IntegerField(default=10)
    girl = models.IntegerField(default=5)
    manage = Manager()

    class Meta:
        db_table = 'Company'
