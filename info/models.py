from django.db import models

# Create your models here.
class FairInfo(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовок")
    description = models.TextField(null=True, blank=True,verbose_name="Описание")
    target = models.TextField( null=True, blank=True,verbose_name="Цель")
    mission = models.TextField( null=True, blank=True,verbose_name="Миссии")
    task = models.TextField( null=True, blank=True,verbose_name="Задачи")
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о ярмарке вакансий'
        verbose_name_plural = 'Информация о ярмарке вакансий'

class Organizer(models.Model):
    full_name = models.CharField(max_length=255,null=True,verbose_name="ФИО или название")
    description = models.TextField(null=True, blank=True,verbose_name="Описание")
    logo_url = models.ImageField(null=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Организаторы'

class Sponsor(models.Model):
    full_name = models.CharField(max_length=255,null=True,verbose_name="Название компании")
    description = models.TextField(null=True, blank=True,verbose_name="Описание")
    logo_url = models.ImageField(null=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Спонсоры'

class Partner(models.Model):
    type = models.ForeignKey(CompanyType, null=True, on_delete=models.SET_NULL, related_name='type')
    full_name = models.CharField(max_length=255,verbose_name="Название компании")
    description = models.TextField(null=True, blank=True,verbose_name="Описание")
    logo_url = models.ImageField(null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Партнёры'


class Employer(models.Model):
    full_name = models.CharField(max_length=255,null=True,verbose_name="ФИО или название")
    description = models.TextField(null=True, blank=True,verbose_name="Описание")
    logo_url = models.ImageField(null=True)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Работодатели'

class Shedule(models.Model):
    time = models.TimeField(verbose_name="Время",null=False,blank=False)
    subject=models.CharField(max_length=200,verbose_name="Тема",null=False,blank=False)
    speaker = models.CharField(max_length=255,verbose_name="Спикер",null=True,blank=True)
    place=models.CharField(max_length=100,verbose_name="Место",null=False,blank=False)

    def __str__(self):
        return '{}'.format(self.time)


    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

class CompanyType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name