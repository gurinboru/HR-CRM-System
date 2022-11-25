from django.contrib.auth.models import User
from django.db import models


# Статусы -----------------------------------------------
class DenialStatus(models.Model):
    CHOICES = (
        (0, 'Активный'),
        (1, 'Отказ рекрутёра'),
        (2, 'Отказ соискателя'),
        (3, 'Отказ заказчика'),
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'denialStatus'
        verbose_name = 'DenialStatus'
        verbose_name_plural = 'DenialStatus'

class CallStatus(models.Model):
    CHOICES = (
        (0, 'Состоялось'),
        (1, 'Перезвонить'),
        (2, 'Недозвон')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'callStatus'
        verbose_name = 'CallStatus'
        verbose_name_plural = 'CallStatus'


class MeetStatus(models.Model):
    CHOICES = (
        (0, 'Запланировано'),
        (1, 'Состоялось'),
        (2, 'Не состоялось')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'meetStatus'
        verbose_name = 'MeetStatus'
        verbose_name_plural = 'MeetStatus'


class MeetEmpStatus(models.Model):
    CHOICES = (
        (0, 'Состоялось'),
        (1, 'Перезвонить'),
        (2, 'Недозвон')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'meetEmpStatus'
        verbose_name = 'MeetEmpStatus'
        verbose_name_plural = 'MeetEmpStatus'


class TestStatus(models.Model):
    CHOICES = (
        (0, 'В работе'),
        (1, 'Не выполнено'),
        (2, 'Отказ от выполнения'),
        (3, 'Выполнено'),
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'testStatus'
        verbose_name = 'TestStatus'
        verbose_name_plural = 'TestStatus'

class StatusJob(models.Model):
    CHOICES = (
        ('Открыта', 'Открыта'),
        ('Закрыта', 'Закрыта'),
        ('Заморожена', 'Заморожена')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'statusjob'
        verbose_name = 'StatusJob'
        verbose_name_plural = 'StatusJob'


# Сущности ----------------------------------------------

class Job(models.Model):
    name = models.TextField()
    salary = models.IntegerField()
    expirence = models.IntegerField()
    employment = models.TextField()
    # definition = models.TextField()
    id_status = models.ForeignKey('StatusJob',on_delete=models.DO_NOTHING,db_column='id_status')
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'jobs'
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    # def save(self, *args, **kwargs):
    #     self.id_status = StatusJob.objects.get(pk=0)
    #     super().save(*args,**kwargs)

class Candidate(models.Model):
    name = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    sex = models.TextField()
    photo = models.FileField()
    birthdate = models.DateField()
    cv = models.FileField()

    class Meta:
        db_table = 'candidates'
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

class JobSeek(models.Model):
    job = models.ForeignKey('Job',on_delete=models.DO_NOTHING, db_column='job')
    candidate = models.ForeignKey('Candidate',on_delete=models.DO_NOTHING,db_column='candidate')
    offer = models.IntegerField()
    offer_definition = models.TextField()
    release_date = models.DateField()
    denial_status = models.ForeignKey
    call_tatus = models.ForeignKey('CallStatus',on_delete=models.DO_NOTHING, db_column='call_tatus')
    call_tatus_defenition = models.TextField()
    test_status = models.ForeignKey('TestStatus',on_delete=models.DO_NOTHING, db_column='test_status')
    test_status_defenition = models.TextField()
    meet_status = models.ForeignKey('MeetStatus',on_delete=models.DO_NOTHING, db_column='meet_status')
    meet_status_defenition = models.TextField()
    meetemp_status = models.ForeignKey('MeetEmpStatus',on_delete=models.DO_NOTHING, db_column='meetemp_status')
    meetemp_status_defenition = models.TextField()

    class Meta:
        db_table = 'jobseek'
        verbose_name = 'JobSeek'
        verbose_name_plural = 'JobSeek'


class ActionHistory(models.Model):
    job_seek = models.ForeignKey('JobSeek',on_delete=models.DO_NOTHING, db_column='job_seek')
    action_name = models.TextField()
    value_before = models.TextField()
    value_after = models.TextField()
    data = models.DateField()

    class Meta:
        db_table = 'actionHistory'
        verbose_name = 'ActionHistory'
        verbose_name_plural = 'ActionHistory'
