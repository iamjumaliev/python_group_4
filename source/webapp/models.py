from django.db import models

class Mission(models.Model):

    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Краткое описание')

    description = models.CharField(max_length=3000, null=False, blank=True, verbose_name='Полное описание')

    status = models.ForeignKey('webapp.Status', related_name='mission_status',null=True, blank=False,
                               on_delete=models.PROTECT,verbose_name='Status')

    type = models.ForeignKey('webapp.Type', related_name='mission_type', on_delete=models.PROTECT,
                             verbose_name='Type')

    project = models.ForeignKey('webapp.Project',related_name='mission_project', on_delete=models.PROTECT,
                                verbose_name='Project')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')



    def __str__(self):
        return self.summary

class Status(models.Model):
    status = models.CharField(max_length=20, verbose_name='Status')

    def __str__(self):
        return self.status


class Type(models.Model):
    type = models.CharField(max_length=20, verbose_name='Type')

    def __str__(self):
        return self.type



class Project(models.Model):

    name = models.CharField(max_length=200,ull=False, blank=False, verbose_name='Название проекта')

    description = models.CharField(max_length=2000, null=False, blank=True, verbose_name='Описание')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.name